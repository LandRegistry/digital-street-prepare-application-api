# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.schedule_code import ScheduleCode  # noqa: F401,E501
from swagger_server import util


class ScheduleInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: ScheduleCode=None, sequence: int=None, header: Dict[str, str]=None):  # noqa: E501
        """ScheduleInfo - a model defined in Swagger

        :param code: The code of this ScheduleInfo.  # noqa: E501
        :type code: ScheduleCode
        :param sequence: The sequence of this ScheduleInfo.  # noqa: E501
        :type sequence: int
        :param header: The header of this ScheduleInfo.  # noqa: E501
        :type header: Dict[str, str]
        """
        self.swagger_types = {
            'code': ScheduleCode,
            'sequence': int,
            'header': Dict[str, str]
        }

        self.attribute_map = {
            'code': 'code',
            'sequence': 'sequence',
            'header': 'header'
        }
        self._code = code
        self._sequence = sequence
        self._header = header

    @classmethod
    def from_dict(cls, dikt) -> 'ScheduleInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ScheduleInfo of this ScheduleInfo.  # noqa: E501
        :rtype: ScheduleInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> ScheduleCode:
        """Gets the code of this ScheduleInfo.


        :return: The code of this ScheduleInfo.
        :rtype: ScheduleCode
        """
        return self._code

    @code.setter
    def code(self, code: ScheduleCode):
        """Sets the code of this ScheduleInfo.


        :param code: The code of this ScheduleInfo.
        :type code: ScheduleCode
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def sequence(self) -> int:
        """Gets the sequence of this ScheduleInfo.

        The position of the entry within its schedule.  # noqa: E501

        :return: The sequence of this ScheduleInfo.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence: int):
        """Sets the sequence of this ScheduleInfo.

        The position of the entry within its schedule.  # noqa: E501

        :param sequence: The sequence of this ScheduleInfo.
        :type sequence: int
        """
        if sequence is None:
            raise ValueError("Invalid value for `sequence`, must not be `None`")  # noqa: E501

        self._sequence = sequence

    @property
    def header(self) -> Dict[str, str]:
        """Gets the header of this ScheduleInfo.

        The official header text of this schedule.  # noqa: E501

        :return: The header of this ScheduleInfo.
        :rtype: Dict[str, str]
        """
        return self._header

    @header.setter
    def header(self, header: Dict[str, str]):
        """Sets the header of this ScheduleInfo.

        The official header text of this schedule.  # noqa: E501

        :param header: The header of this ScheduleInfo.
        :type header: Dict[str, str]
        """
        if header is None:
            raise ValueError("Invalid value for `header`, must not be `None`")  # noqa: E501

        self._header = header