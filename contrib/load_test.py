from faker import Faker
from locust import HttpUser, task, constant, TaskSet, events


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("Load Test is starting")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("Load Test is ending")


class Unauthorized(TaskSet):
    data = {}

    @task
    def list_meals_not_found(self):
        self.client.request_name = "Unauthorized"
        with self.client.post("meals/", data=self.data, catch_response=True) as response:
            expected_text = "Authentication credentials were not provided."
            if response.status_code == 401:
                if response.json().get("detail") == expected_text:
                    response.success()
                else:
                    response.failure("Unauthorized message not expected")
            else:
                response.failure(f"Response {response.status_code} not as expected")


class ListMeals(TaskSet):

    @task
    def list_meals(self):
        self.client.get('meals/')


class CreateMeals(TaskSet):
    faker = Faker()

    @task
    def create_meals(self):
        meal_name = self.faker.bothify(text='??????????####')
        data = {
            "sku": meal_name,
            "slug": meal_name,
            "title": "Grandma Soup",
            "description": "My Favorite Grandma Soup",
            "category": "mains",
            "start_date": "2022-07-31",
            "end_date": "2030-07-31"
        }

        self.client.post('meals/', json=data)


class AnonymousUser(HttpUser):
    tasks = [ListMeals, Unauthorized]
    weight = 1


class MyFoodUser(HttpUser):
    wait_time = constant(1)
    tasks = {ListMeals: 1, CreateMeals: 3}
    weight = 2

    def on_start(self):
        # Send login request
        response = self.client.post(
            "token/",
            json={
                "username": "cliente",
                "password": "help1234"
            }
        )
        # set "token" from response body
        token = response.json().get('access')
        self.client.headers.update({'Authorization': f'Bearer {token}'})

