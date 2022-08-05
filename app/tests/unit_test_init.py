from urllib.parse import urlencode
import pytest
import json
from flask import url_for

from app import app as test_app


@pytest.fixture
def app():
    return test_app


@pytest.fixture
def client(app) :
    return app.test_client()
    email = "test@local.com"
    password = "test_password"
    try:
        user = django_user_model.objects.get(email=email)
    except BaseException as e:
        user = django_user_model.objects.create_user(email=email, password=password)
    client.force_login(user)
    return client

@pytest.fixture(scope="class")
def data_store():
    """
    Save common used values in this store
    This can is used in all test function of class
    """
    return {}


def url_string(app, **url_params):
    with app.test_request_context():
        string = url_for("graphql")

    if url_params:
        string += "?" + urlencode(url_params)

    return string


def response_json(response):
    return json.loads(response.data.decode())


def request_environ(email):
    return {
        "serverless.event": {
            "requestContext": {"authorizer": {"claims": {"email": email}}}
        }
    }