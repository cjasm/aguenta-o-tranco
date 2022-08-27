from locust import HttpUser, between, task
import logging


class MyFoodUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        logging.info("Estou iniciando o meu usuário")

    def on_stop(self):
        logging.info("Estou encerrando o meu usuário")

    @task
    def list_meals(self):
        self.client.get('/api/meals/')
