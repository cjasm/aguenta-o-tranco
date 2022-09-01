from faker import Faker
from locust import HttpUser, task, constant, TaskSet, events
import logging


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logging.info('Load Test is starting')


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    logging.info('Load Test is ending')


@task
def list_meals(user):
    user.client.get('meals/')


@task
def create_meals(user):
    meal_name = user.faker.bothify(text='??????????####')
    data = {
        'sku': meal_name,
        'slug': meal_name,
        'title': 'Grandma Soup',
        'description': 'My Favorite Grandma Soup',
        'category': 'mains',
        'start_date': '2022-07-31',
        'end_date': '2030-07-31'
    }

    user.client.post('meals/', json=data)


class Unauthorized(TaskSet):
    data = {}

    @task
    def list_meals_not_found(self):
        self.client.request_name = 'Unauthorized'
        with self.client.post('meals/', data=self.data, catch_response=True) as response:
            expected_text = 'Authentication credentials were not provided.'
            if response.status_code != 401:
                response.failure(f'Response {response.status_code} not as expected')
                return

            if response.json().get('detail') != expected_text:
                response.failure('Unauthorized message not expected')
                return

            response.success()
            return

    def stop(self):
        self.interrupt()


class AnonymousUser(HttpUser):
    tasks = [list_meals, Unauthorized]
    weight = 1


class MyFoodUser(HttpUser):
    wait_time = constant(1)
    tasks = {list_meals: 1, create_meals: 3}
    weight = 2
    faker = Faker()

    def on_start(self):
        # Send login request
        response = self.client.post(
            'token/',
            json={
                'username': 'foo',
                'password': 'bar'
            }
        )
        # set 'token' from response body
        token = response.json().get('access')
        self.client.headers.update({'Authorization': f'Bearer {token}'})
