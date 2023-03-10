# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from mdmv2.configuration import Configuration


class AppleOsXRestrictionSharingPayloadEntity_(object):
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
        'restrict_which_sharing_services_are_enabled': 'bool',
        'air_drop': 'bool',
        'facebook': 'bool',
        'twitter': 'bool',
        'mail': 'bool',
        'messages': 'bool',
        'video_services': 'bool',
        'addtoi_photo': 'bool',
        'addto_aperture': 'bool',
        'addto_reading_list': 'bool',
        'sina_weibo': 'bool',
        'automatically_enable_new_sharing_services': 'bool'
    }

    attribute_map = {
        'restrict_which_sharing_services_are_enabled': 'RestrictWhichSharingServicesAreEnabled',
        'air_drop': 'AirDrop',
        'facebook': 'Facebook',
        'twitter': 'Twitter',
        'mail': 'Mail',
        'messages': 'Messages',
        'video_services': 'VideoServices',
        'addtoi_photo': 'AddtoiPhoto',
        'addto_aperture': 'AddtoAperture',
        'addto_reading_list': 'AddtoReadingList',
        'sina_weibo': 'SinaWeibo',
        'automatically_enable_new_sharing_services': 'AutomaticallyEnableNewSharingServices'
    }

    def __init__(self, restrict_which_sharing_services_are_enabled=None, air_drop=None, facebook=None, twitter=None, mail=None, messages=None, video_services=None, addtoi_photo=None, addto_aperture=None, addto_reading_list=None, sina_weibo=None, automatically_enable_new_sharing_services=None, _configuration=None):  # noqa: E501
        """AppleOsXRestrictionSharingPayloadEntity_ - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._restrict_which_sharing_services_are_enabled = None
        self._air_drop = None
        self._facebook = None
        self._twitter = None
        self._mail = None
        self._messages = None
        self._video_services = None
        self._addtoi_photo = None
        self._addto_aperture = None
        self._addto_reading_list = None
        self._sina_weibo = None
        self._automatically_enable_new_sharing_services = None
        self.discriminator = None

        if restrict_which_sharing_services_are_enabled is not None:
            self.restrict_which_sharing_services_are_enabled = restrict_which_sharing_services_are_enabled
        if air_drop is not None:
            self.air_drop = air_drop
        if facebook is not None:
            self.facebook = facebook
        if twitter is not None:
            self.twitter = twitter
        if mail is not None:
            self.mail = mail
        if messages is not None:
            self.messages = messages
        if video_services is not None:
            self.video_services = video_services
        if addtoi_photo is not None:
            self.addtoi_photo = addtoi_photo
        if addto_aperture is not None:
            self.addto_aperture = addto_aperture
        if addto_reading_list is not None:
            self.addto_reading_list = addto_reading_list
        if sina_weibo is not None:
            self.sina_weibo = sina_weibo
        if automatically_enable_new_sharing_services is not None:
            self.automatically_enable_new_sharing_services = automatically_enable_new_sharing_services

    @property
    def restrict_which_sharing_services_are_enabled(self):
        """Gets the restrict_which_sharing_services_are_enabled of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable restrictions for sharing services.  # noqa: E501

        :return: The restrict_which_sharing_services_are_enabled of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._restrict_which_sharing_services_are_enabled

    @restrict_which_sharing_services_are_enabled.setter
    def restrict_which_sharing_services_are_enabled(self, restrict_which_sharing_services_are_enabled):
        """Sets the restrict_which_sharing_services_are_enabled of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable restrictions for sharing services.  # noqa: E501

        :param restrict_which_sharing_services_are_enabled: The restrict_which_sharing_services_are_enabled of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._restrict_which_sharing_services_are_enabled = restrict_which_sharing_services_are_enabled

    @property
    def air_drop(self):
        """Gets the air_drop of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable AirDrop.  # noqa: E501

        :return: The air_drop of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._air_drop

    @air_drop.setter
    def air_drop(self, air_drop):
        """Sets the air_drop of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable AirDrop.  # noqa: E501

        :param air_drop: The air_drop of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._air_drop = air_drop

    @property
    def facebook(self):
        """Gets the facebook of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable Facebook.  # noqa: E501

        :return: The facebook of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """Sets the facebook of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable Facebook.  # noqa: E501

        :param facebook: The facebook of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._facebook = facebook

    @property
    def twitter(self):
        """Gets the twitter of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable Twitter.  # noqa: E501

        :return: The twitter of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """Sets the twitter of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable Twitter.  # noqa: E501

        :param twitter: The twitter of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._twitter = twitter

    @property
    def mail(self):
        """Gets the mail of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable Mail.  # noqa: E501

        :return: The mail of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        """Sets the mail of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable Mail.  # noqa: E501

        :param mail: The mail of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._mail = mail

    @property
    def messages(self):
        """Gets the messages of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable Messages.  # noqa: E501

        :return: The messages of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable Messages.  # noqa: E501

        :param messages: The messages of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._messages = messages

    @property
    def video_services(self):
        """Gets the video_services of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable Video Services.  # noqa: E501

        :return: The video_services of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._video_services

    @video_services.setter
    def video_services(self, video_services):
        """Sets the video_services of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable Video Services.  # noqa: E501

        :param video_services: The video_services of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._video_services = video_services

    @property
    def addtoi_photo(self):
        """Gets the addtoi_photo of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable the Add to iPhoto.  # noqa: E501

        :return: The addtoi_photo of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._addtoi_photo

    @addtoi_photo.setter
    def addtoi_photo(self, addtoi_photo):
        """Sets the addtoi_photo of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable the Add to iPhoto.  # noqa: E501

        :param addtoi_photo: The addtoi_photo of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._addtoi_photo = addtoi_photo

    @property
    def addto_aperture(self):
        """Gets the addto_aperture of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable the Add to Aperture.  # noqa: E501

        :return: The addto_aperture of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._addto_aperture

    @addto_aperture.setter
    def addto_aperture(self, addto_aperture):
        """Sets the addto_aperture of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable the Add to Aperture.  # noqa: E501

        :param addto_aperture: The addto_aperture of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._addto_aperture = addto_aperture

    @property
    def addto_reading_list(self):
        """Gets the addto_reading_list of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable the Add to Reading List.  # noqa: E501

        :return: The addto_reading_list of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._addto_reading_list

    @addto_reading_list.setter
    def addto_reading_list(self, addto_reading_list):
        """Sets the addto_reading_list of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable the Add to Reading List.  # noqa: E501

        :param addto_reading_list: The addto_reading_list of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._addto_reading_list = addto_reading_list

    @property
    def sina_weibo(self):
        """Gets the sina_weibo of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to enable Sina Weibo.  # noqa: E501

        :return: The sina_weibo of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._sina_weibo

    @sina_weibo.setter
    def sina_weibo(self, sina_weibo):
        """Sets the sina_weibo of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to enable Sina Weibo.  # noqa: E501

        :param sina_weibo: The sina_weibo of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._sina_weibo = sina_weibo

    @property
    def automatically_enable_new_sharing_services(self):
        """Gets the automatically_enable_new_sharing_services of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501

        Gets or sets a value indicating whether whether to allow new sharing services automatically.  # noqa: E501

        :return: The automatically_enable_new_sharing_services of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :rtype: bool
        """
        return self._automatically_enable_new_sharing_services

    @automatically_enable_new_sharing_services.setter
    def automatically_enable_new_sharing_services(self, automatically_enable_new_sharing_services):
        """Sets the automatically_enable_new_sharing_services of this AppleOsXRestrictionSharingPayloadEntity_.

        Gets or sets a value indicating whether whether to allow new sharing services automatically.  # noqa: E501

        :param automatically_enable_new_sharing_services: The automatically_enable_new_sharing_services of this AppleOsXRestrictionSharingPayloadEntity_.  # noqa: E501
        :type: bool
        """

        self._automatically_enable_new_sharing_services = automatically_enable_new_sharing_services

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
        if issubclass(AppleOsXRestrictionSharingPayloadEntity_, dict):
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
        if not isinstance(other, AppleOsXRestrictionSharingPayloadEntity_):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppleOsXRestrictionSharingPayloadEntity_):
            return True

        return self.to_dict() != other.to_dict()
