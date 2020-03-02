import connexion
import six

from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.object import Object  # noqa: E501
from swagger_server.models.submit_application_response import SubmitApplicationResponse  # noqa: E501
from swagger_server.models.validation_error_response import ValidationErrorResponse  # noqa: E501
from swagger_server.models.validation_success_response import ValidationSuccessResponse  # noqa: E501
from swagger_server import util


def applications_draft_post(body):  # noqa: E501
    """applications_draft_post

    Draft a new application and optionally create a new notification topic for the title # noqa: E501

    :param body: Details of the application to draft.
    :type body: list | bytes

    :rtype: ValidationSuccessResponse
    """
    if connexion.request.is_json:
        body = [Object.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def applications_submit_post(body):  # noqa: E501
    """applications_submit_post

    Validate and submit an application to change the register # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: SubmitApplicationResponse
    """
    if connexion.request.is_json:
        body = [Object.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'


def applications_validate_put(body):  # noqa: E501
    """applications_validate_put

    Validate an application before submission. # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: ValidationSuccessResponse
    """
    if connexion.request.is_json:
        body = [Object.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
    return 'do some magic!'
