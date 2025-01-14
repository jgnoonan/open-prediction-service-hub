# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.model import Model  # noqa: F401,E501
from swagger_server import util


class Models(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, models: List[Model]=None):  # noqa: E501
        """Models - a model defined in Swagger

        :param models: The models of this Models.  # noqa: E501
        :type models: List[Model]
        """
        self.swagger_types = {
            'models': List[Model]
        }

        self.attribute_map = {
            'models': 'models'
        }
        self._models = models

    @classmethod
    def from_dict(cls, dikt) -> 'Models':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Models of this Models.  # noqa: E501
        :rtype: Models
        """
        return util.deserialize_model(dikt, cls)

    @property
    def models(self) -> List[Model]:
        """Gets the models of this Models.

        List of models  # noqa: E501

        :return: The models of this Models.
        :rtype: List[Model]
        """
        return self._models

    @models.setter
    def models(self, models: List[Model]):
        """Sets the models of this Models.

        List of models  # noqa: E501

        :param models: The models of this Models.
        :type models: List[Model]
        """

        self._models = models
