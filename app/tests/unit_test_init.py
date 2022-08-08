from urllib.parse import urlencode
import pytest
import json
from flask import url_for
from app import app as test_app
from flask_login import FlaskLoginClient



@pytest.fixture
def app():
    ctx = test_app.app_context()
    ctx.push()
    return test_app

@pytest.fixture
def client(app) :
    app.test_client_class = FlaskLoginClient
    app.testing = True
    return app.test_client()


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
    
