# coding: utf-8

"""
    rainbond cloud app market OpenAPI.

    the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: 576501057@qq.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from market_client.models.store_app_version_templete import StoreAppVersionTemplete  # noqa: F401,E501
from market_client.models.templete_version import TempleteVersion  # noqa: F401,E501


class StoreAppVersion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'app_key_id': 'str',
        'app_version': 'str',
        'app_version_alias': 'str',
        'create_time': 'datetime',
        'desc': 'str',
        'rainbond_version': 'str',
        'templete': 'StoreAppVersionTemplete',
        'templete_version': 'TempleteVersion',
        'update_time': 'datetime',
        'update_version': 'int'
    }

    attribute_map = {
        'app_key_id': 'app_key_id',
        'app_version': 'app_version',
        'app_version_alias': 'app_version_alias',
        'create_time': 'create_time',
        'desc': 'desc',
        'rainbond_version': 'rainbond_version',
        'templete': 'templete',
        'templete_version': 'templete_version',
        'update_time': 'update_time',
        'update_version': 'update_version'
    }

    def __init__(self, app_key_id=None, app_version=None, app_version_alias=None, create_time=None, desc=None, rainbond_version=None, templete=None, templete_version=None, update_time=None, update_version=None):  # noqa: E501
        """StoreAppVersion - a model defined in Swagger"""  # noqa: E501

        self._app_key_id = None
        self._app_version = None
        self._app_version_alias = None
        self._create_time = None
        self._desc = None
        self._rainbond_version = None
        self._templete = None
        self._templete_version = None
        self._update_time = None
        self._update_version = None
        self.discriminator = None

        if app_key_id is not None:
            self.app_key_id = app_key_id
        if app_version is not None:
            self.app_version = app_version
        if app_version_alias is not None:
            self.app_version_alias = app_version_alias
        if create_time is not None:
            self.create_time = create_time
        if desc is not None:
            self.desc = desc
        if rainbond_version is not None:
            self.rainbond_version = rainbond_version
        if templete is not None:
            self.templete = templete
        if templete_version is not None:
            self.templete_version = templete_version
        if update_time is not None:
            self.update_time = update_time
        if update_version is not None:
            self.update_version = update_version

    @property
    def app_key_id(self):
        """Gets the app_key_id of this StoreAppVersion.  # noqa: E501


        :return: The app_key_id of this StoreAppVersion.  # noqa: E501
        :rtype: str
        """
        return self._app_key_id

    @app_key_id.setter
    def app_key_id(self, app_key_id):
        """Sets the app_key_id of this StoreAppVersion.


        :param app_key_id: The app_key_id of this StoreAppVersion.  # noqa: E501
        :type: str
        """

        self._app_key_id = app_key_id

    @property
    def app_version(self):
        """Gets the app_version of this StoreAppVersion.  # noqa: E501


        :return: The app_version of this StoreAppVersion.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this StoreAppVersion.


        :param app_version: The app_version of this StoreAppVersion.  # noqa: E501
        :type: str
        """

        self._app_version = app_version

    @property
    def app_version_alias(self):
        """Gets the app_version_alias of this StoreAppVersion.  # noqa: E501


        :return: The app_version_alias of this StoreAppVersion.  # noqa: E501
        :rtype: str
        """
        return self._app_version_alias

    @app_version_alias.setter
    def app_version_alias(self, app_version_alias):
        """Sets the app_version_alias of this StoreAppVersion.


        :param app_version_alias: The app_version_alias of this StoreAppVersion.  # noqa: E501
        :type: str
        """

        self._app_version_alias = app_version_alias

    @property
    def create_time(self):
        """Gets the create_time of this StoreAppVersion.  # noqa: E501


        :return: The create_time of this StoreAppVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this StoreAppVersion.


        :param create_time: The create_time of this StoreAppVersion.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def desc(self):
        """Gets the desc of this StoreAppVersion.  # noqa: E501


        :return: The desc of this StoreAppVersion.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this StoreAppVersion.


        :param desc: The desc of this StoreAppVersion.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def rainbond_version(self):
        """Gets the rainbond_version of this StoreAppVersion.  # noqa: E501


        :return: The rainbond_version of this StoreAppVersion.  # noqa: E501
        :rtype: str
        """
        return self._rainbond_version

    @rainbond_version.setter
    def rainbond_version(self, rainbond_version):
        """Sets the rainbond_version of this StoreAppVersion.


        :param rainbond_version: The rainbond_version of this StoreAppVersion.  # noqa: E501
        :type: str
        """

        self._rainbond_version = rainbond_version

    @property
    def templete(self):
        """Gets the templete of this StoreAppVersion.  # noqa: E501


        :return: The templete of this StoreAppVersion.  # noqa: E501
        :rtype: StoreAppVersionTemplete
        """
        return self._templete

    @templete.setter
    def templete(self, templete):
        """Sets the templete of this StoreAppVersion.


        :param templete: The templete of this StoreAppVersion.  # noqa: E501
        :type: StoreAppVersionTemplete
        """

        self._templete = templete

    @property
    def templete_version(self):
        """Gets the templete_version of this StoreAppVersion.  # noqa: E501


        :return: The templete_version of this StoreAppVersion.  # noqa: E501
        :rtype: TempleteVersion
        """
        return self._templete_version

    @templete_version.setter
    def templete_version(self, templete_version):
        """Sets the templete_version of this StoreAppVersion.


        :param templete_version: The templete_version of this StoreAppVersion.  # noqa: E501
        :type: TempleteVersion
        """

        self._templete_version = templete_version

    @property
    def update_time(self):
        """Gets the update_time of this StoreAppVersion.  # noqa: E501


        :return: The update_time of this StoreAppVersion.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this StoreAppVersion.


        :param update_time: The update_time of this StoreAppVersion.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def update_version(self):
        """Gets the update_version of this StoreAppVersion.  # noqa: E501


        :return: The update_version of this StoreAppVersion.  # noqa: E501
        :rtype: int
        """
        return self._update_version

    @update_version.setter
    def update_version(self, update_version):
        """Sets the update_version of this StoreAppVersion.


        :param update_version: The update_version of this StoreAppVersion.  # noqa: E501
        :type: int
        """

        self._update_version = update_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(StoreAppVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StoreAppVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
