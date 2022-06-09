from locust import HttpUser, task


class TestEndpoint(HttpUser):
    @task
    def test_email(self):
        self.client.post("/", json={"email": "exmaple@mail.ru", "uuid": "51847c2e-fa63-4b48-81c7-7ab9a4c56d8c"})
