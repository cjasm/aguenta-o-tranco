from locust import HttpUser, between, constant, task, TaskSet, events
import logging
import faker


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logging.info('Estou começando os meus testes de carga')


@events.test_stop.add_listener
def on_test_start(environment, **kwargs):
    logging.info('Estou encerrando os meus testes de carga')


@task
def list_meals(self):
    self.client.get('/api/meals/')


class UnauthorizedTaskSet(TaskSet):

    @task
    def create_meals_unauthorized(self):
        self.client.request_name = 'Unauthorized'
        with self.client.post('/api/meals/', json={}, catch_response=True) as req:
            if req.status_code != 401:
                req.failure('Response with code status not expected')
                return

            req.success()

    @task
    def stop(self):
        self.interrupt(reschedule=True)


class AnonymousUser(HttpUser):
    wait_time = constant(1)
    weight = 3
    tasks = [list_meals, UnauthorizedTaskSet]


class MyFoodUser(HttpUser):
    wait_time = between(1, 5)
    faker = faker.Faker()
    tasks = [list_meals]

    def on_start(self):
        req = self.client.post(
            '/api/token/',
            json={
                'username': 'client',
                'password': 'labcodes123'
            }
        )
        token = req.json().get('access')
        self.client.headers.update({'Authorization': f'Bearer {token}'})

    @task
    def create_meal(self):
        meal_name = self.faker.bothify(text='???####')
        data = {
            "sku": meal_name,
            "slug": meal_name,
            "title": "Grandma Soup",
            "description": "My Favorite Grandma Soup",
            "category": "mains",
            "start_date": "2022-07-31",
            "end_date": "2030-07-31"
        }
        self.client.post('/api/meals/', json=data)
