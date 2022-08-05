from .graphql_query import create_user
from .unit_test_init import *
from faker import Faker
import pytest
import json

faker = Faker()


class TestUser:
    @pytest.fixture
    def init(self, client, app):
        self.variables = {
            "email": "test9@gmail.com",
            "name": "test9",
            "userId": "9"
        }

    def test_create_user(self, init, app, client):
        response = client.post(
            url_string(
                app,
                query=create_user(),
                variables=json.dumps(self.variables),
            ),
            environ_base=request_environ("")
        )
        assert response.status_code == 200
        assert response_json(response) == {
            "data": {
                "createUser": {
                    "user": {
                        "name": "test9",
                        "email": "test9@gmail.com",
                        "userId": "10"
                    }
                }
            }
        }

    def end(self):
        return True
