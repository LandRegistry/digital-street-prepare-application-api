# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.proprietor_address import ProprietorAddress  # noqa: F401,E501
from swagger_server import util


class PrivateIndividual(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, proprietor_type: str=None, sequence: int=None, name: str=None, title: str=None, fore_names: str=None, surname: str=None, decor: str=None, legacy_name_id: str=None, addresses: List[ProprietorAddress]=None):  # noqa: E501
        """PrivateIndividual - a model defined in Swagger

        :param proprietor_type: The proprietor_type of this PrivateIndividual.  # noqa: E501
        :type proprietor_type: str
        :param sequence: The sequence of this PrivateIndividual.  # noqa: E501
        :type sequence: int
        :param name: The name of this PrivateIndividual.  # noqa: E501
        :type name: str
        :param title: The title of this PrivateIndividual.  # noqa: E501
        :type title: str
        :param fore_names: The fore_names of this PrivateIndividual.  # noqa: E501
        :type fore_names: str
        :param surname: The surname of this PrivateIndividual.  # noqa: E501
        :type surname: str
        :param decor: The decor of this PrivateIndividual.  # noqa: E501
        :type decor: str
        :param legacy_name_id: The legacy_name_id of this PrivateIndividual.  # noqa: E501
        :type legacy_name_id: str
        :param addresses: The addresses of this PrivateIndividual.  # noqa: E501
        :type addresses: List[ProprietorAddress]
        """
        self.swagger_types = {
            'proprietor_type': str,
            'sequence': int,
            'name': str,
            'title': str,
            'fore_names': str,
            'surname': str,
            'decor': str,
            'legacy_name_id': str,
            'addresses': List[ProprietorAddress]
        }

        self.attribute_map = {
            'proprietor_type': 'proprietor_type',
            'sequence': 'sequence',
            'name': 'name',
            'title': 'title',
            'fore_names': 'fore_names',
            'surname': 'surname',
            'decor': 'decor',
            'legacy_name_id': 'legacy_name_id',
            'addresses': 'addresses'
        }
        self._proprietor_type = proprietor_type
        self._sequence = sequence
        self._name = name
        self._title = title
        self._fore_names = fore_names
        self._surname = surname
        self._decor = decor
        self._legacy_name_id = legacy_name_id
        self._addresses = addresses

    @classmethod
    def from_dict(cls, dikt) -> 'PrivateIndividual':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PrivateIndividual of this PrivateIndividual.  # noqa: E501
        :rtype: PrivateIndividual
        """
        return util.deserialize_model(dikt, cls)

    @property
    def proprietor_type(self) -> str:
        """Gets the proprietor_type of this PrivateIndividual.

        Coarse classification of a proprietor. Used to easily distinguish between a private individual and an organisation.  # noqa: E501

        :return: The proprietor_type of this PrivateIndividual.
        :rtype: str
        """
        return self._proprietor_type

    @proprietor_type.setter
    def proprietor_type(self, proprietor_type: str):
        """Sets the proprietor_type of this PrivateIndividual.

        Coarse classification of a proprietor. Used to easily distinguish between a private individual and an organisation.  # noqa: E501

        :param proprietor_type: The proprietor_type of this PrivateIndividual.
        :type proprietor_type: str
        """
        allowed_values = ["private_individual"]  # noqa: E501
        if proprietor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `proprietor_type` ({0}), must be one of {1}"
                .format(proprietor_type, allowed_values)
            )

        self._proprietor_type = proprietor_type

    @property
    def sequence(self) -> int:
        """Gets the sequence of this PrivateIndividual.

        The position of the proprietor in the register.  # noqa: E501

        :return: The sequence of this PrivateIndividual.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence: int):
        """Sets the sequence of this PrivateIndividual.

        The position of the proprietor in the register.  # noqa: E501

        :param sequence: The sequence of this PrivateIndividual.
        :type sequence: int
        """
        if sequence is None:
            raise ValueError("Invalid value for `sequence`, must not be `None`")  # noqa: E501

        self._sequence = sequence

    @property
    def name(self) -> str:
        """Gets the name of this PrivateIndividual.

        Full name of the private individual.  # noqa: E501

        :return: The name of this PrivateIndividual.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this PrivateIndividual.

        Full name of the private individual.  # noqa: E501

        :param name: The name of this PrivateIndividual.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def title(self) -> str:
        """Gets the title of this PrivateIndividual.


        :return: The title of this PrivateIndividual.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this PrivateIndividual.


        :param title: The title of this PrivateIndividual.
        :type title: str
        """

        self._title = title

    @property
    def fore_names(self) -> str:
        """Gets the fore_names of this PrivateIndividual.


        :return: The fore_names of this PrivateIndividual.
        :rtype: str
        """
        return self._fore_names

    @fore_names.setter
    def fore_names(self, fore_names: str):
        """Sets the fore_names of this PrivateIndividual.


        :param fore_names: The fore_names of this PrivateIndividual.
        :type fore_names: str
        """

        self._fore_names = fore_names

    @property
    def surname(self) -> str:
        """Gets the surname of this PrivateIndividual.


        :return: The surname of this PrivateIndividual.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname: str):
        """Sets the surname of this PrivateIndividual.


        :param surname: The surname of this PrivateIndividual.
        :type surname: str
        """

        self._surname = surname

    @property
    def decor(self) -> str:
        """Gets the decor of this PrivateIndividual.

        Text which contains the details of any decoration and/or title held by a private individual. e.g. 'OBE','GC', 'KCMG'. For those private individuals holding titles such as 'Duke of ...', 'Lord' etc., the particulars of such titles will be held in this field.  # noqa: E501

        :return: The decor of this PrivateIndividual.
        :rtype: str
        """
        return self._decor

    @decor.setter
    def decor(self, decor: str):
        """Sets the decor of this PrivateIndividual.

        Text which contains the details of any decoration and/or title held by a private individual. e.g. 'OBE','GC', 'KCMG'. For those private individuals holding titles such as 'Duke of ...', 'Lord' etc., the particulars of such titles will be held in this field.  # noqa: E501

        :param decor: The decor of this PrivateIndividual.
        :type decor: str
        """

        self._decor = decor

    @property
    def legacy_name_id(self) -> str:
        """Gets the legacy_name_id of this PrivateIndividual.


        :return: The legacy_name_id of this PrivateIndividual.
        :rtype: str
        """
        return self._legacy_name_id

    @legacy_name_id.setter
    def legacy_name_id(self, legacy_name_id: str):
        """Sets the legacy_name_id of this PrivateIndividual.


        :param legacy_name_id: The legacy_name_id of this PrivateIndividual.
        :type legacy_name_id: str
        """

        self._legacy_name_id = legacy_name_id

    @property
    def addresses(self) -> List[ProprietorAddress]:
        """Gets the addresses of this PrivateIndividual.


        :return: The addresses of this PrivateIndividual.
        :rtype: List[ProprietorAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses: List[ProprietorAddress]):
        """Sets the addresses of this PrivateIndividual.


        :param addresses: The addresses of this PrivateIndividual.
        :type addresses: List[ProprietorAddress]
        """

        self._addresses = addresses
