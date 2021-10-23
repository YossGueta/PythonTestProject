

import json
import logging

LOGGER = logging.getLogger(__name__)
# import sys

# from pip._vendor.requests import RequestException
# from werkzeug.exceptions import Forbidden, HTTPException

# from utils import get_random_id
# from flask import jsonify


# def test_response_status_code(client):
#     response = client.get('/tasks')
#     print(response)
#     assert response.status_code == 200


# def test_post_route__success(client, app_ctx):
#     url = '/tasks'
#     data = {

#         "task": "write server mddock",
#         "completed": True

#     }

#     response = client.post(url, data=json.dumps(data), content_type="application/json")
#     print (response)

#     assert response.status_code == 200


# def test_delete_request(client):
#     request_id = {}
#     task_id = request_id['tid']
#     url = '/delete'
#     try:
#         response = client.delete(url + '/tasks' + task_id)
#         assert response.status_code == 200
#     except RequestException as error:
#         sys.stderr.write(error)
#         sys.exit(1)


# def test_error_handler_http_subclass(app):
#     @app.errorhandler(HTTPException)
#     def handle_exception(e):
#         """Return JSON instead of HTML for HTTP errors."""
#         # start with the correct headers and status code from the error
#         response = e.get_response()
#         # replace the body with JSON
#         response.data = json.dumps({
#             "code": e.code,
#             "name": e.name,
#             "description": e.description,
#         })
#         response.content_type = "application/json"
#         return response

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_response_status_code(client):
    response = client.get('/api/tasks')
    print(response)
    assert response.status_code == 200
    
def test_post_route__success(client):
    url = '/api/tasks'
    data = {

        "task": "write server mddock",
        "completed": True

    }

    response = client.post(url, data=json.dumps(data), content_type="application/json")
    LOGGER.critical(response.json)
    assert response.status_code == 200
