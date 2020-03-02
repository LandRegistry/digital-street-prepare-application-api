# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TransferRequestConsideration(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, consideration_type: str=None, currency: str=None, amount: int=None, other_receipt: str=None):  # noqa: E501
        """TransferRequestConsideration - a model defined in Swagger

        :param consideration_type: The consideration_type of this TransferRequestConsideration.  # noqa: E501
        :type consideration_type: str
        :param currency: The currency of this TransferRequestConsideration.  # noqa: E501
        :type currency: str
        :param amount: The amount of this TransferRequestConsideration.  # noqa: E501
        :type amount: int
        :param other_receipt: The other_receipt of this TransferRequestConsideration.  # noqa: E501
        :type other_receipt: str
        """
        self.swagger_types = {
            'consideration_type': str,
            'currency': str,
            'amount': int,
            'other_receipt': str
        }

        self.attribute_map = {
            'consideration_type': 'consideration_type',
            'currency': 'currency',
            'amount': 'amount',
            'other_receipt': 'other_receipt'
        }
        self._consideration_type = consideration_type
        self._currency = currency
        self._amount = amount
        self._other_receipt = other_receipt

    @classmethod
    def from_dict(cls, dikt) -> 'TransferRequestConsideration':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransferRequest_consideration of this TransferRequestConsideration.  # noqa: E501
        :rtype: TransferRequestConsideration
        """
        return util.deserialize_model(dikt, cls)

    @property
    def consideration_type(self) -> str:
        """Gets the consideration_type of this TransferRequestConsideration.


        :return: The consideration_type of this TransferRequestConsideration.
        :rtype: str
        """
        return self._consideration_type

    @consideration_type.setter
    def consideration_type(self, consideration_type: str):
        """Sets the consideration_type of this TransferRequestConsideration.


        :param consideration_type: The consideration_type of this TransferRequestConsideration.
        :type consideration_type: str
        """
        allowed_values = ["transfer_for_value", "transfer_not_for_value", "other_receipt"]  # noqa: E501
        if consideration_type not in allowed_values:
            raise ValueError(
                "Invalid value for `consideration_type` ({0}), must be one of {1}"
                .format(consideration_type, allowed_values)
            )

        self._consideration_type = consideration_type

    @property
    def currency(self) -> str:
        """Gets the currency of this TransferRequestConsideration.


        :return: The currency of this TransferRequestConsideration.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency: str):
        """Sets the currency of this TransferRequestConsideration.


        :param currency: The currency of this TransferRequestConsideration.
        :type currency: str
        """
        allowed_values = ["gbp", "eur"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def amount(self) -> int:
        """Gets the amount of this TransferRequestConsideration.


        :return: The amount of this TransferRequestConsideration.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this TransferRequestConsideration.


        :param amount: The amount of this TransferRequestConsideration.
        :type amount: int
        """

        self._amount = amount

    @property
    def other_receipt(self) -> str:
        """Gets the other_receipt of this TransferRequestConsideration.


        :return: The other_receipt of this TransferRequestConsideration.
        :rtype: str
        """
        return self._other_receipt

    @other_receipt.setter
    def other_receipt(self, other_receipt: str):
        """Sets the other_receipt of this TransferRequestConsideration.


        :param other_receipt: The other_receipt of this TransferRequestConsideration.
        :type other_receipt: str
        """

        self._other_receipt = other_receipt
