# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
#from swagger_server.models.object import Object  # noqa: E501
from swagger_server.models.submit_application_response import SubmitApplicationResponse  # noqa: E501
from swagger_server.models.validation_error_response import ValidationErrorResponse  # noqa: E501
from swagger_server.models.validation_success_response import ValidationSuccessResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_applications_draft_post(self):
        """Test case for applications_draft_post

        
        """
        body = [Object()]
        response = self.client.open(
            '/applications/draft',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_submit_post(self):
        """Test case for applications_submit_post

        
        """
        body = [Object()]
        response = self.client.open(
            '/applications/submit',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_validate_put(self):
        """Test case for applications_validate_put

        
        """
        body = [Object()]
        response = self.client.open(
            '/applications/validate',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
