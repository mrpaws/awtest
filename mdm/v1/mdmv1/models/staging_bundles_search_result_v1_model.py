# coding: utf-8

"""
    MDM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv1.configuration import Configuration


class StagingBundlesSearchResultV1Model(object):
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
        'staging_bundle_details': 'list[StagingBundleDetailsModel_]',
        'additional_info': 'HypermediaModel_',
        'total_results': 'int'
    }

    attribute_map = {
        'staging_bundle_details': 'StagingBundleDetails',
        'additional_info': 'AdditionalInfo',
        'total_results': 'TotalResults'
    }

    def __init__(self, staging_bundle_details=None, additional_info=None, total_results=None, _configuration=None):  # noqa: E501
        """StagingBundlesSearchResultV1Model - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._staging_bundle_details = None
        self._additional_info = None
        self._total_results = None
        self.discriminator = None

        if staging_bundle_details is not None:
            self.staging_bundle_details = staging_bundle_details
        if additional_info is not None:
            self.additional_info = additional_info
        if total_results is not None:
            self.total_results = total_results

    @property
    def staging_bundle_details(self):
        """Gets the staging_bundle_details of this StagingBundlesSearchResultV1Model.  # noqa: E501

        Gets or sets agent Packages Details.  # noqa: E501

        :return: The staging_bundle_details of this StagingBundlesSearchResultV1Model.  # noqa: E501
        :rtype: list[StagingBundleDetailsModel_]
        """
        return self._staging_bundle_details

    @staging_bundle_details.setter
    def staging_bundle_details(self, staging_bundle_details):
        """Sets the staging_bundle_details of this StagingBundlesSearchResultV1Model.

        Gets or sets agent Packages Details.  # noqa: E501

        :param staging_bundle_details: The staging_bundle_details of this StagingBundlesSearchResultV1Model.  # noqa: E501
        :type: list[StagingBundleDetailsModel_]
        """

        self._staging_bundle_details = staging_bundle_details

    @property
    def additional_info(self):
        """Gets the additional_info of this StagingBundlesSearchResultV1Model.  # noqa: E501

        Gets or sets Hypermedia content for the result.  # noqa: E501

        :return: The additional_info of this StagingBundlesSearchResultV1Model.  # noqa: E501
        :rtype: HypermediaModel_
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this StagingBundlesSearchResultV1Model.

        Gets or sets Hypermedia content for the result.  # noqa: E501

        :param additional_info: The additional_info of this StagingBundlesSearchResultV1Model.  # noqa: E501
        :type: HypermediaModel_
        """

        self._additional_info = additional_info

    @property
    def total_results(self):
        """Gets the total_results of this StagingBundlesSearchResultV1Model.  # noqa: E501

        Gets or sets total result.  # noqa: E501

        :return: The total_results of this StagingBundlesSearchResultV1Model.  # noqa: E501
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this StagingBundlesSearchResultV1Model.

        Gets or sets total result.  # noqa: E501

        :param total_results: The total_results of this StagingBundlesSearchResultV1Model.  # noqa: E501
        :type: int
        """

        self._total_results = total_results

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
        if issubclass(StagingBundlesSearchResultV1Model, dict):
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
        if not isinstance(other, StagingBundlesSearchResultV1Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StagingBundlesSearchResultV1Model):
            return True

        return self.to_dict() != other.to_dict()
