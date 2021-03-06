# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DeclarationOfTrust(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, trust_type: str=None, trust_details: str=None):  # noqa: E501
        """DeclarationOfTrust - a model defined in Swagger

        :param trust_type: The trust_type of this DeclarationOfTrust.  # noqa: E501
        :type trust_type: str
        :param trust_details: The trust_details of this DeclarationOfTrust.  # noqa: E501
        :type trust_details: str
        """
        self.swagger_types = {
            'trust_type': str,
            'trust_details': str
        }

        self.attribute_map = {
            'trust_type': 'trust_type',
            'trust_details': 'trust_details'
        }
        self._trust_type = trust_type
        self._trust_details = trust_details

    @classmethod
    def from_dict(cls, dikt) -> 'DeclarationOfTrust':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeclarationOfTrust of this DeclarationOfTrust.  # noqa: E501
        :rtype: DeclarationOfTrust
        """
        return util.deserialize_model(dikt, cls)

    @property
    def trust_type(self) -> str:
        """Gets the trust_type of this DeclarationOfTrust.

        The type of trust  # noqa: E501

        :return: The trust_type of this DeclarationOfTrust.
        :rtype: str
        """
        return self._trust_type

    @trust_type.setter
    def trust_type(self, trust_type: str):
        """Sets the trust_type of this DeclarationOfTrust.

        The type of trust  # noqa: E501

        :param trust_type: The trust_type of this DeclarationOfTrust.
        :type trust_type: str
        """
        allowed_values = ["joint_tenants", "tenants_in_common_in_equal_shares", "held_on_trust"]  # noqa: E501
        if trust_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trust_type` ({0}), must be one of {1}"
                .format(trust_type, allowed_values)
            )

        self._trust_type = trust_type

    @property
    def trust_details(self) -> str:
        """Gets the trust_details of this DeclarationOfTrust.

        The details of the trust or of the trust instrument. Only required if trust_type is 'held_on_trust'  # noqa: E501

        :return: The trust_details of this DeclarationOfTrust.
        :rtype: str
        """
        return self._trust_details

    @trust_details.setter
    def trust_details(self, trust_details: str):
        """Sets the trust_details of this DeclarationOfTrust.

        The details of the trust or of the trust instrument. Only required if trust_type is 'held_on_trust'  # noqa: E501

        :param trust_details: The trust_details of this DeclarationOfTrust.
        :type trust_details: str
        """

        self._trust_details = trust_details
