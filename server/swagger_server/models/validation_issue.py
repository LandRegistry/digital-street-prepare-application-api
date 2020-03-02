# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.one_of_validation_issue_value import OneOfValidationIssueValue
# from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class ValidationIssue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, issue_code: str=None, message: str=None, property_name: str=None, value: OneOfValidationIssueValue=None):  # noqa: E501
        """ValidationIssue - a model defined in Swagger

        :param issue_code: The issue_code of this ValidationIssue.  # noqa: E501
        :type issue_code: str
        :param message: The message of this ValidationIssue.  # noqa: E501
        :type message: str
        :param property_name: The property_name of this ValidationIssue.  # noqa: E501
        :type property_name: str
        :param value: The value of this ValidationIssue.  # noqa: E501
        :type value: OneOfValidationIssueValue
        """
        self.swagger_types = {
            'issue_code': str,
            'message': str,
            'property_name': str,
            'value': OneOfValidationIssueValue
        }

        self.attribute_map = {
            'issue_code': 'issue_code',
            'message': 'message',
            'property_name': 'property_name',
            'value': 'value'
        }
        self._issue_code = issue_code
        self._message = message
        self._property_name = property_name
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'ValidationIssue':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ValidationIssue of this ValidationIssue.  # noqa: E501
        :rtype: ValidationIssue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issue_code(self) -> str:
        """Gets the issue_code of this ValidationIssue.

        A code identifying the type of issue that occurred. This allows integrating APIs to try to resolve the issue automatically.  # noqa: E501

        :return: The issue_code of this ValidationIssue.
        :rtype: str
        """
        return self._issue_code

    @issue_code.setter
    def issue_code(self, issue_code: str):
        """Sets the issue_code of this ValidationIssue.

        A code identifying the type of issue that occurred. This allows integrating APIs to try to resolve the issue automatically.  # noqa: E501

        :param issue_code: The issue_code of this ValidationIssue.
        :type issue_code: str
        """
        if issue_code is None:
            raise ValueError("Invalid value for `issue_code`, must not be `None`")  # noqa: E501

        self._issue_code = issue_code

    @property
    def message(self) -> str:
        """Gets the message of this ValidationIssue.

        A message summarising why this property failed to validate.  # noqa: E501

        :return: The message of this ValidationIssue.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ValidationIssue.

        A message summarising why this property failed to validate.  # noqa: E501

        :param message: The message of this ValidationIssue.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def property_name(self) -> str:
        """Gets the property_name of this ValidationIssue.

        The name of the property that this issue was raised for.  # noqa: E501

        :return: The property_name of this ValidationIssue.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name: str):
        """Sets the property_name of this ValidationIssue.

        The name of the property that this issue was raised for.  # noqa: E501

        :param property_name: The property_name of this ValidationIssue.
        :type property_name: str
        """
        if property_name is None:
            raise ValueError("Invalid value for `property_name`, must not be `None`")  # noqa: E501

        self._property_name = property_name

    @property
    def value(self) -> OneOfValidationIssueValue:
        """Gets the value of this ValidationIssue.

        The value of the property that passed validation.  # noqa: E501

        :return: The value of this ValidationIssue.
        :rtype: OneOfValidationIssueValue
        """
        return self._value

    @value.setter
    def value(self, value: OneOfValidationIssueValue):
        """Sets the value of this ValidationIssue.

        The value of the property that passed validation.  # noqa: E501

        :param value: The value of this ValidationIssue.
        :type value: OneOfValidationIssueValue
        """

        self._value = value
