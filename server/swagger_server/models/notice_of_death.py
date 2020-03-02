# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.assurance_of_death import AssuranceOfDeath  # noqa: F401,E501
from swagger_server.models.private_individual import PrivateIndividual  # noqa: F401,E501
from swagger_server import util


class NoticeOfDeath(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, deceased: PrivateIndividual=None, assurance_of_death: AssuranceOfDeath=None):  # noqa: E501
        """NoticeOfDeath - a model defined in Swagger

        :param deceased: The deceased of this NoticeOfDeath.  # noqa: E501
        :type deceased: PrivateIndividual
        :param assurance_of_death: The assurance_of_death of this NoticeOfDeath.  # noqa: E501
        :type assurance_of_death: AssuranceOfDeath
        """
        self.swagger_types = {
            'deceased': PrivateIndividual,
            'assurance_of_death': AssuranceOfDeath
        }

        self.attribute_map = {
            'deceased': 'deceased',
            'assurance_of_death': 'assurance_of_death'
        }
        self._deceased = deceased
        self._assurance_of_death = assurance_of_death

    @classmethod
    def from_dict(cls, dikt) -> 'NoticeOfDeath':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NoticeOfDeath of this NoticeOfDeath.  # noqa: E501
        :rtype: NoticeOfDeath
        """
        return util.deserialize_model(dikt, cls)

    @property
    def deceased(self) -> PrivateIndividual:
        """Gets the deceased of this NoticeOfDeath.


        :return: The deceased of this NoticeOfDeath.
        :rtype: PrivateIndividual
        """
        return self._deceased

    @deceased.setter
    def deceased(self, deceased: PrivateIndividual):
        """Sets the deceased of this NoticeOfDeath.


        :param deceased: The deceased of this NoticeOfDeath.
        :type deceased: PrivateIndividual
        """
        if deceased is None:
            raise ValueError("Invalid value for `deceased`, must not be `None`")  # noqa: E501

        self._deceased = deceased

    @property
    def assurance_of_death(self) -> AssuranceOfDeath:
        """Gets the assurance_of_death of this NoticeOfDeath.


        :return: The assurance_of_death of this NoticeOfDeath.
        :rtype: AssuranceOfDeath
        """
        return self._assurance_of_death

    @assurance_of_death.setter
    def assurance_of_death(self, assurance_of_death: AssuranceOfDeath):
        """Sets the assurance_of_death of this NoticeOfDeath.


        :param assurance_of_death: The assurance_of_death of this NoticeOfDeath.
        :type assurance_of_death: AssuranceOfDeath
        """
        if assurance_of_death is None:
            raise ValueError("Invalid value for `assurance_of_death`, must not be `None`")  # noqa: E501

        self._assurance_of_death = assurance_of_death