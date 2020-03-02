# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.proprietor_address import ProprietorAddress  # noqa: F401,E501
from swagger_server import util


class Organisation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, proprietor_type: str=None, organisation_type: str=None, sequence: int=None, name: str=None, company_registration_number: str=None, location: str=None, legacy_name_id: str=None, addresses: List[ProprietorAddress]=None):  # noqa: E501
        """Organisation - a model defined in Swagger

        :param proprietor_type: The proprietor_type of this Organisation.  # noqa: E501
        :type proprietor_type: str
        :param organisation_type: The organisation_type of this Organisation.  # noqa: E501
        :type organisation_type: str
        :param sequence: The sequence of this Organisation.  # noqa: E501
        :type sequence: int
        :param name: The name of this Organisation.  # noqa: E501
        :type name: str
        :param company_registration_number: The company_registration_number of this Organisation.  # noqa: E501
        :type company_registration_number: str
        :param location: The location of this Organisation.  # noqa: E501
        :type location: str
        :param legacy_name_id: The legacy_name_id of this Organisation.  # noqa: E501
        :type legacy_name_id: str
        :param addresses: The addresses of this Organisation.  # noqa: E501
        :type addresses: List[ProprietorAddress]
        """
        self.swagger_types = {
            'proprietor_type': str,
            'organisation_type': str,
            'sequence': int,
            'name': str,
            'company_registration_number': str,
            'location': str,
            'legacy_name_id': str,
            'addresses': List[ProprietorAddress]
        }

        self.attribute_map = {
            'proprietor_type': 'proprietor_type',
            'organisation_type': 'organisation_type',
            'sequence': 'sequence',
            'name': 'name',
            'company_registration_number': 'company_registration_number',
            'location': 'location',
            'legacy_name_id': 'legacy_name_id',
            'addresses': 'addresses'
        }
        self._proprietor_type = proprietor_type
        self._organisation_type = organisation_type
        self._sequence = sequence
        self._name = name
        self._company_registration_number = company_registration_number
        self._location = location
        self._legacy_name_id = legacy_name_id
        self._addresses = addresses

    @classmethod
    def from_dict(cls, dikt) -> 'Organisation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Organisation of this Organisation.  # noqa: E501
        :rtype: Organisation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def proprietor_type(self) -> str:
        """Gets the proprietor_type of this Organisation.

        Coarse classification of a proprietor. Used to easily distinguish between a private individual and an organisation.  # noqa: E501

        :return: The proprietor_type of this Organisation.
        :rtype: str
        """
        return self._proprietor_type

    @proprietor_type.setter
    def proprietor_type(self, proprietor_type: str):
        """Sets the proprietor_type of this Organisation.

        Coarse classification of a proprietor. Used to easily distinguish between a private individual and an organisation.  # noqa: E501

        :param proprietor_type: The proprietor_type of this Organisation.
        :type proprietor_type: str
        """
        allowed_values = ["organisation"]  # noqa: E501
        if proprietor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `proprietor_type` ({0}), must be one of {1}"
                .format(proprietor_type, allowed_values)
            )

        self._proprietor_type = proprietor_type

    @property
    def organisation_type(self) -> str:
        """Gets the organisation_type of this Organisation.

        Fine-grained classification of an organisation  # noqa: E501

        :return: The organisation_type of this Organisation.
        :rtype: str
        """
        return self._organisation_type

    @organisation_type.setter
    def organisation_type(self, organisation_type: str):
        """Sets the organisation_type of this Organisation.

        Fine-grained classification of an organisation  # noqa: E501

        :param organisation_type: The organisation_type of this Organisation.
        :type organisation_type: str
        """
        allowed_values = ["county_council", "limited_company_or_public_limited_company", "limited_liability_partnership", "local_authority"]  # noqa: E501
        if organisation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `organisation_type` ({0}), must be one of {1}"
                .format(organisation_type, allowed_values)
            )

        self._organisation_type = organisation_type

    @property
    def sequence(self) -> int:
        """Gets the sequence of this Organisation.

        The position of the proprietor within the register.  # noqa: E501

        :return: The sequence of this Organisation.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence: int):
        """Sets the sequence of this Organisation.

        The position of the proprietor within the register.  # noqa: E501

        :param sequence: The sequence of this Organisation.
        :type sequence: int
        """

        self._sequence = sequence

    @property
    def name(self) -> str:
        """Gets the name of this Organisation.

        Name of the organisation. If it's a charity, the charity name will appear here.  # noqa: E501

        :return: The name of this Organisation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Organisation.

        Name of the organisation. If it's a charity, the charity name will appear here.  # noqa: E501

        :param name: The name of this Organisation.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def company_registration_number(self) -> str:
        """Gets the company_registration_number of this Organisation.

        Number which is a unique identifier assigned to a company when it is registered at companies house. Although the name of the company may change, the company registration number will remain the same.   # noqa: E501

        :return: The company_registration_number of this Organisation.
        :rtype: str
        """
        return self._company_registration_number

    @company_registration_number.setter
    def company_registration_number(self, company_registration_number: str):
        """Sets the company_registration_number of this Organisation.

        Number which is a unique identifier assigned to a company when it is registered at companies house. Although the name of the company may change, the company registration number will remain the same.   # noqa: E501

        :param company_registration_number: The company_registration_number of this Organisation.
        :type company_registration_number: str
        """

        self._company_registration_number = company_registration_number

    @property
    def location(self) -> str:
        """Gets the location of this Organisation.


        :return: The location of this Organisation.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location: str):
        """Sets the location of this Organisation.


        :param location: The location of this Organisation.
        :type location: str
        """
        allowed_values = ["england_or_wales", "scotland", "northern_ireland", "overseas"]  # noqa: E501
        if location not in allowed_values:
            raise ValueError(
                "Invalid value for `location` ({0}), must be one of {1}"
                .format(location, allowed_values)
            )

        self._location = location

    @property
    def legacy_name_id(self) -> str:
        """Gets the legacy_name_id of this Organisation.


        :return: The legacy_name_id of this Organisation.
        :rtype: str
        """
        return self._legacy_name_id

    @legacy_name_id.setter
    def legacy_name_id(self, legacy_name_id: str):
        """Sets the legacy_name_id of this Organisation.


        :param legacy_name_id: The legacy_name_id of this Organisation.
        :type legacy_name_id: str
        """

        self._legacy_name_id = legacy_name_id

    @property
    def addresses(self) -> List[ProprietorAddress]:
        """Gets the addresses of this Organisation.

        A list of addresses relating to the proprietor. May be the same address as other proprietors present on the title.   # noqa: E501

        :return: The addresses of this Organisation.
        :rtype: List[ProprietorAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses: List[ProprietorAddress]):
        """Sets the addresses of this Organisation.

        A list of addresses relating to the proprietor. May be the same address as other proprietors present on the title.   # noqa: E501

        :param addresses: The addresses of this Organisation.
        :type addresses: List[ProprietorAddress]
        """

        self._addresses = addresses