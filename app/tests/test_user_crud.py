from .graphql_query import create_user, update_user, delete_user
from .unit_test_init import *
from faker import Faker
import pytest
import json

faker = Faker()


class TestUser:
    @pytest.fixture
    def init(self, client, app):
        self.variables = {
            "email": faker.email(),
            "name": faker.name(),
            "userId": "9"
        }
        self.update_variables = {
            "email": faker.email(),
            "name": faker.name(),
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
                        "name": self.variables['name'],
                        "email": self.variables['email'],
                        "userId": "9"
                    }
                }
            }
        }

    def test_update_user(self, init, app, client):
        response = client.post(
            url_string(
                app,
                query=update_user(),
                variables=json.dumps(self.update_variables),
            ),
            environ_base=request_environ("")
        )
        assert response.status_code == 200
        assert response_json(response) == {
            "data": {
                "updateUser": {
                    "user": {
                        "name": self.update_variables['name'],
                        "email": self.update_variables['email'],
                        "userId": "9"
                    }
                }
            }
        }

    def test_delete_user(self, init, app, client):
        response = client.post(
            url_string(
                app,
                query=delete_user(),
                variables=json.dumps({
                    "userId": "9"
                }),
            ),
            environ_base=request_environ("")
        )
        assert response.status_code == 200
        assert response_json(response) == {
            "data": {
                "deleteUser": {
                    "success": True
                }
            }
        }

    def end(self):
        return True
