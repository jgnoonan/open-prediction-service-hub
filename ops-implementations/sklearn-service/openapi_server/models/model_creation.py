# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.feature import Feature
from openapi_server.models.link import Link
from openapi_server import util

from openapi_server.models.feature import Feature  # noqa: E501
from openapi_server.models.link import Link  # noqa: E501

class ModelCreation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, input_schema=None, output_schema=None, version=None, links=None, metadata=None):  # noqa: E501
        """ModelCreation - a model defined in OpenAPI

        :param name: The name of this ModelCreation.  # noqa: E501
        :type name: str
        :param input_schema: The input_schema of this ModelCreation.  # noqa: E501
        :type input_schema: List[Feature]
        :param output_schema: The output_schema of this ModelCreation.  # noqa: E501
        :type output_schema: Dict[str, object]
        :param version: The version of this ModelCreation.  # noqa: E501
        :type version: str
        :param links: The links of this ModelCreation.  # noqa: E501
        :type links: List[Link]
        :param metadata: The metadata of this ModelCreation.  # noqa: E501
        :type metadata: Dict[str, object]
        """
        self.openapi_types = {
            'name': str,
            'input_schema': List[Feature],
            'output_schema': Dict[str, object],
            'version': str,
            'links': List[Link],
            'metadata': Dict[str, object]
        }

        self.attribute_map = {
            'name': 'name',
            'input_schema': 'input_schema',
            'output_schema': 'output_schema',
            'version': 'version',
            'links': 'links',
            'metadata': 'metadata'
        }

        self._name = name
        self._input_schema = input_schema
        self._output_schema = output_schema
        self._version = version
        self._links = links
        self._metadata = metadata

    @classmethod
    def from_dict(cls, dikt) -> 'ModelCreation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ModelCreation of this ModelCreation.  # noqa: E501
        :rtype: ModelCreation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ModelCreation.

        Name of model  # noqa: E501

        :return: The name of this ModelCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelCreation.

        Name of model  # noqa: E501

        :param name: The name of this ModelCreation.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def input_schema(self):
        """Gets the input_schema of this ModelCreation.

        Input schema of ml model  # noqa: E501

        :return: The input_schema of this ModelCreation.
        :rtype: List[Feature]
        """
        return self._input_schema

    @input_schema.setter
    def input_schema(self, input_schema):
        """Sets the input_schema of this ModelCreation.

        Input schema of ml model  # noqa: E501

        :param input_schema: The input_schema of this ModelCreation.
        :type input_schema: List[Feature]
        """

        self._input_schema = input_schema

    @property
    def output_schema(self):
        """Gets the output_schema of this ModelCreation.

        Model output schema  # noqa: E501

        :return: The output_schema of this ModelCreation.
        :rtype: Dict[str, object]
        """
        return self._output_schema

    @output_schema.setter
    def output_schema(self, output_schema):
        """Sets the output_schema of this ModelCreation.

        Model output schema  # noqa: E501

        :param output_schema: The output_schema of this ModelCreation.
        :type output_schema: Dict[str, object]
        """

        self._output_schema = output_schema

    @property
    def version(self):
        """Gets the version of this ModelCreation.

        version of the model  # noqa: E501

        :return: The version of this ModelCreation.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelCreation.

        version of the model  # noqa: E501

        :param version: The version of this ModelCreation.
        :type version: str
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this ModelCreation.

        optional array of typed linked resources  # noqa: E501

        :return: The links of this ModelCreation.
        :rtype: List[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ModelCreation.

        optional array of typed linked resources  # noqa: E501

        :param links: The links of this ModelCreation.
        :type links: List[Link]
        """

        self._links = links

    @property
    def metadata(self):
        """Gets the metadata of this ModelCreation.

        additional metadata  # noqa: E501

        :return: The metadata of this ModelCreation.
        :rtype: Dict[str, object]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ModelCreation.

        additional metadata  # noqa: E501

        :param metadata: The metadata of this ModelCreation.
        :type metadata: Dict[str, object]
        """

        self._metadata = metadata