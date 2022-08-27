from locust import HttpUser, between, task
import logging
import faker


class MyFoodUser(HttpUser):
    wait_time = between(1, 5)
    faker = faker.Faker()

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

    @task(3)
    def list_meals(self):
        self.client.get('/api/meals/')

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
