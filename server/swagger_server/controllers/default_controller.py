import connexion
import json
import requests
import six
from collections import OrderedDict

from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.object import Object  # noqa: E501
from swagger_server.models.submit_application_response import SubmitApplicationResponse  # noqa: E501
from swagger_server.models.validation_error_response import ValidationErrorResponse  # noqa: E501
from swagger_server.models.validation_success_response import ValidationSuccessResponse  # noqa: E501
from swagger_server import util

with open('swagger_server/responses/draft_response.json') as json_file:
    draft_response = json.load(json_file)
with open('swagger_server/responses/validate_response_1.json') as json_file:
    validate_response_1 = json.load(json_file)
with open('swagger_server/responses/validate_response_2.json') as json_file:
    validate_response_2 = json.load(json_file)
with open('swagger_server/responses/submit_response.json') as json_file:
    submit_response = json.load(json_file)
with open('swagger_server/responses/notification_1.json') as json_file:
    notification_1 = json.load(json_file)

def applications_draft_post(body):  # noqa: E501
    """applications_draft_post

    Draft a new application and optionally create a new notification topic for the title # noqa: E501

    :param body: Details of the application to draft.
    :type body: list | bytes

    :rtype: ValidationSuccessResponse
    """
    if connexion.request.is_json:
        body = [Object.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    # return json.dumps(str(draft_response))
    return draft_response, 400


def applications_submit_post(body):  # noqa: E501
    """applications_submit_post

    Validate and submit an application to change the register # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: SubmitApplicationResponse
    """
    if connexion.request.is_json:
        body = [Object.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    try:
        response = requests.post('http://localhost:5555/AGL117262', headers={"content-type": "application/json"}, data=json.dumps(notification_1))
        response.raise_for_status()
    except Exception as err:
        print(f'Error occurred: {err}')
    return submit_response, 202


def applications_validate_put(body):  # noqa: E501
    """applications_validate_put

    Validate an application before submission. # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: ValidationSuccessResponse
    """
    if connexion.request.is_json:
        body = [Object.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    if not body[0]['transferors'][1].get('trustee'):
        return validate_response_1, 400
    else:
        return validate_response_2, 200
    return 'Something went wrong'
