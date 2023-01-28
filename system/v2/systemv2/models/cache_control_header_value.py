# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from systemv2.configuration import Configuration


class CacheControlHeaderValue(object):
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
        'no_cache': 'bool',
        'no_cache_headers': 'list[str]',
        'no_store': 'bool',
        'max_age': 'str',
        'shared_max_age': 'str',
        'max_stale': 'bool',
        'max_stale_limit': 'str',
        'min_fresh': 'str',
        'no_transform': 'bool',
        'only_if_cached': 'bool',
        'public': 'bool',
        'private': 'bool',
        'private_headers': 'list[str]',
        'must_revalidate': 'bool',
        'proxy_revalidate': 'bool',
        'extensions': 'list[NameValueHeaderValue]'
    }

    attribute_map = {
        'no_cache': 'NoCache',
        'no_cache_headers': 'NoCacheHeaders',
        'no_store': 'NoStore',
        'max_age': 'MaxAge',
        'shared_max_age': 'SharedMaxAge',
        'max_stale': 'MaxStale',
        'max_stale_limit': 'MaxStaleLimit',
        'min_fresh': 'MinFresh',
        'no_transform': 'NoTransform',
        'only_if_cached': 'OnlyIfCached',
        'public': 'Public',
        'private': 'Private',
        'private_headers': 'PrivateHeaders',
        'must_revalidate': 'MustRevalidate',
        'proxy_revalidate': 'ProxyRevalidate',
        'extensions': 'Extensions'
    }

    def __init__(self, no_cache=None, no_cache_headers=None, no_store=None, max_age=None, shared_max_age=None, max_stale=None, max_stale_limit=None, min_fresh=None, no_transform=None, only_if_cached=None, public=None, private=None, private_headers=None, must_revalidate=None, proxy_revalidate=None, extensions=None, _configuration=None):  # noqa: E501
        """CacheControlHeaderValue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._no_cache = None
        self._no_cache_headers = None
        self._no_store = None
        self._max_age = None
        self._shared_max_age = None
        self._max_stale = None
        self._max_stale_limit = None
        self._min_fresh = None
        self._no_transform = None
        self._only_if_cached = None
        self._public = None
        self._private = None
        self._private_headers = None
        self._must_revalidate = None
        self._proxy_revalidate = None
        self._extensions = None
        self.discriminator = None

        if no_cache is not None:
            self.no_cache = no_cache
        if no_cache_headers is not None:
            self.no_cache_headers = no_cache_headers
        if no_store is not None:
            self.no_store = no_store
        if max_age is not None:
            self.max_age = max_age
        if shared_max_age is not None:
            self.shared_max_age = shared_max_age
        if max_stale is not None:
            self.max_stale = max_stale
        if max_stale_limit is not None:
            self.max_stale_limit = max_stale_limit
        if min_fresh is not None:
            self.min_fresh = min_fresh
        if no_transform is not None:
            self.no_transform = no_transform
        if only_if_cached is not None:
            self.only_if_cached = only_if_cached
        if public is not None:
            self.public = public
        if private is not None:
            self.private = private
        if private_headers is not None:
            self.private_headers = private_headers
        if must_revalidate is not None:
            self.must_revalidate = must_revalidate
        if proxy_revalidate is not None:
            self.proxy_revalidate = proxy_revalidate
        if extensions is not None:
            self.extensions = extensions

    @property
    def no_cache(self):
        """Gets the no_cache of this CacheControlHeaderValue.  # noqa: E501


        :return: The no_cache of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._no_cache

    @no_cache.setter
    def no_cache(self, no_cache):
        """Sets the no_cache of this CacheControlHeaderValue.


        :param no_cache: The no_cache of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._no_cache = no_cache

    @property
    def no_cache_headers(self):
        """Gets the no_cache_headers of this CacheControlHeaderValue.  # noqa: E501


        :return: The no_cache_headers of this CacheControlHeaderValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._no_cache_headers

    @no_cache_headers.setter
    def no_cache_headers(self, no_cache_headers):
        """Sets the no_cache_headers of this CacheControlHeaderValue.


        :param no_cache_headers: The no_cache_headers of this CacheControlHeaderValue.  # noqa: E501
        :type: list[str]
        """

        self._no_cache_headers = no_cache_headers

    @property
    def no_store(self):
        """Gets the no_store of this CacheControlHeaderValue.  # noqa: E501


        :return: The no_store of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._no_store

    @no_store.setter
    def no_store(self, no_store):
        """Sets the no_store of this CacheControlHeaderValue.


        :param no_store: The no_store of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._no_store = no_store

    @property
    def max_age(self):
        """Gets the max_age of this CacheControlHeaderValue.  # noqa: E501


        :return: The max_age of this CacheControlHeaderValue.  # noqa: E501
        :rtype: str
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """Sets the max_age of this CacheControlHeaderValue.


        :param max_age: The max_age of this CacheControlHeaderValue.  # noqa: E501
        :type: str
        """

        self._max_age = max_age

    @property
    def shared_max_age(self):
        """Gets the shared_max_age of this CacheControlHeaderValue.  # noqa: E501


        :return: The shared_max_age of this CacheControlHeaderValue.  # noqa: E501
        :rtype: str
        """
        return self._shared_max_age

    @shared_max_age.setter
    def shared_max_age(self, shared_max_age):
        """Sets the shared_max_age of this CacheControlHeaderValue.


        :param shared_max_age: The shared_max_age of this CacheControlHeaderValue.  # noqa: E501
        :type: str
        """

        self._shared_max_age = shared_max_age

    @property
    def max_stale(self):
        """Gets the max_stale of this CacheControlHeaderValue.  # noqa: E501


        :return: The max_stale of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._max_stale

    @max_stale.setter
    def max_stale(self, max_stale):
        """Sets the max_stale of this CacheControlHeaderValue.


        :param max_stale: The max_stale of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._max_stale = max_stale

    @property
    def max_stale_limit(self):
        """Gets the max_stale_limit of this CacheControlHeaderValue.  # noqa: E501


        :return: The max_stale_limit of this CacheControlHeaderValue.  # noqa: E501
        :rtype: str
        """
        return self._max_stale_limit

    @max_stale_limit.setter
    def max_stale_limit(self, max_stale_limit):
        """Sets the max_stale_limit of this CacheControlHeaderValue.


        :param max_stale_limit: The max_stale_limit of this CacheControlHeaderValue.  # noqa: E501
        :type: str
        """

        self._max_stale_limit = max_stale_limit

    @property
    def min_fresh(self):
        """Gets the min_fresh of this CacheControlHeaderValue.  # noqa: E501


        :return: The min_fresh of this CacheControlHeaderValue.  # noqa: E501
        :rtype: str
        """
        return self._min_fresh

    @min_fresh.setter
    def min_fresh(self, min_fresh):
        """Sets the min_fresh of this CacheControlHeaderValue.


        :param min_fresh: The min_fresh of this CacheControlHeaderValue.  # noqa: E501
        :type: str
        """

        self._min_fresh = min_fresh

    @property
    def no_transform(self):
        """Gets the no_transform of this CacheControlHeaderValue.  # noqa: E501


        :return: The no_transform of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._no_transform

    @no_transform.setter
    def no_transform(self, no_transform):
        """Sets the no_transform of this CacheControlHeaderValue.


        :param no_transform: The no_transform of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._no_transform = no_transform

    @property
    def only_if_cached(self):
        """Gets the only_if_cached of this CacheControlHeaderValue.  # noqa: E501


        :return: The only_if_cached of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._only_if_cached

    @only_if_cached.setter
    def only_if_cached(self, only_if_cached):
        """Sets the only_if_cached of this CacheControlHeaderValue.


        :param only_if_cached: The only_if_cached of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._only_if_cached = only_if_cached

    @property
    def public(self):
        """Gets the public of this CacheControlHeaderValue.  # noqa: E501


        :return: The public of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this CacheControlHeaderValue.


        :param public: The public of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def private(self):
        """Gets the private of this CacheControlHeaderValue.  # noqa: E501


        :return: The private of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this CacheControlHeaderValue.


        :param private: The private of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def private_headers(self):
        """Gets the private_headers of this CacheControlHeaderValue.  # noqa: E501


        :return: The private_headers of this CacheControlHeaderValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._private_headers

    @private_headers.setter
    def private_headers(self, private_headers):
        """Sets the private_headers of this CacheControlHeaderValue.


        :param private_headers: The private_headers of this CacheControlHeaderValue.  # noqa: E501
        :type: list[str]
        """

        self._private_headers = private_headers

    @property
    def must_revalidate(self):
        """Gets the must_revalidate of this CacheControlHeaderValue.  # noqa: E501


        :return: The must_revalidate of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._must_revalidate

    @must_revalidate.setter
    def must_revalidate(self, must_revalidate):
        """Sets the must_revalidate of this CacheControlHeaderValue.


        :param must_revalidate: The must_revalidate of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._must_revalidate = must_revalidate

    @property
    def proxy_revalidate(self):
        """Gets the proxy_revalidate of this CacheControlHeaderValue.  # noqa: E501


        :return: The proxy_revalidate of this CacheControlHeaderValue.  # noqa: E501
        :rtype: bool
        """
        return self._proxy_revalidate

    @proxy_revalidate.setter
    def proxy_revalidate(self, proxy_revalidate):
        """Sets the proxy_revalidate of this CacheControlHeaderValue.


        :param proxy_revalidate: The proxy_revalidate of this CacheControlHeaderValue.  # noqa: E501
        :type: bool
        """

        self._proxy_revalidate = proxy_revalidate

    @property
    def extensions(self):
        """Gets the extensions of this CacheControlHeaderValue.  # noqa: E501


        :return: The extensions of this CacheControlHeaderValue.  # noqa: E501
        :rtype: list[NameValueHeaderValue]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this CacheControlHeaderValue.


        :param extensions: The extensions of this CacheControlHeaderValue.  # noqa: E501
        :type: list[NameValueHeaderValue]
        """

        self._extensions = extensions

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
        if issubclass(CacheControlHeaderValue, dict):
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
        if not isinstance(other, CacheControlHeaderValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CacheControlHeaderValue):
            return True

        return self.to_dict() != other.to_dict()
