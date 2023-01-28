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


class WorkflowPayloadModel(object):
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
        'comment': 'str',
        'starts_at': 'str',
        'steps': 'dict(str, StepTypeBaseModel)',
        'rollback': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'starts_at': 'starts_at',
        'steps': 'steps',
        'rollback': 'rollback'
    }

    def __init__(self, comment=None, starts_at=None, steps=None, rollback=None, _configuration=None):  # noqa: E501
        """WorkflowPayloadModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._comment = None
        self._starts_at = None
        self._steps = None
        self._rollback = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if starts_at is not None:
            self.starts_at = starts_at
        if steps is not None:
            self.steps = steps
        if rollback is not None:
            self.rollback = rollback

    @property
    def comment(self):
        """Gets the comment of this WorkflowPayloadModel.  # noqa: E501


        :return: The comment of this WorkflowPayloadModel.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this WorkflowPayloadModel.


        :param comment: The comment of this WorkflowPayloadModel.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def starts_at(self):
        """Gets the starts_at of this WorkflowPayloadModel.  # noqa: E501


        :return: The starts_at of this WorkflowPayloadModel.  # noqa: E501
        :rtype: str
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this WorkflowPayloadModel.


        :param starts_at: The starts_at of this WorkflowPayloadModel.  # noqa: E501
        :type: str
        """

        self._starts_at = starts_at

    @property
    def steps(self):
        """Gets the steps of this WorkflowPayloadModel.  # noqa: E501


        :return: The steps of this WorkflowPayloadModel.  # noqa: E501
        :rtype: dict(str, StepTypeBaseModel)
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        """Sets the steps of this WorkflowPayloadModel.


        :param steps: The steps of this WorkflowPayloadModel.  # noqa: E501
        :type: dict(str, StepTypeBaseModel)
        """

        self._steps = steps

    @property
    def rollback(self):
        """Gets the rollback of this WorkflowPayloadModel.  # noqa: E501


        :return: The rollback of this WorkflowPayloadModel.  # noqa: E501
        :rtype: bool
        """
        return self._rollback

    @rollback.setter
    def rollback(self, rollback):
        """Sets the rollback of this WorkflowPayloadModel.


        :param rollback: The rollback of this WorkflowPayloadModel.  # noqa: E501
        :type: bool
        """

        self._rollback = rollback

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
        if issubclass(WorkflowPayloadModel, dict):
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
        if not isinstance(other, WorkflowPayloadModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowPayloadModel):
            return True

        return self.to_dict() != other.to_dict()
