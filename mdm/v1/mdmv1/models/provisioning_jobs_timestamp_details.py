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


class ProvisioningJobsTimestampDetails(object):
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
        'product_id': 'int',
        'product_name': 'str',
        'job_id': 'int',
        'job_type': 'str',
        'part_of_set': 'str',
        'product_set': 'str',
        'queued_timestamp': 'str',
        'delivered_timestamp': 'str',
        'cancelled_timestamp': 'str',
        'deleted_timestamp': 'str',
        'completed_timestamp': 'str',
        'failed_timestamp': 'str',
        'detached_timestamp': 'str',
        'deferred_timestamp': 'str',
        'started_timestamp': 'str',
        'waiting_timestamp': 'str',
        'orphaned_timestamp': 'str',
        'installing_timestamp': 'str'
    }

    attribute_map = {
        'product_id': 'ProductID',
        'product_name': 'ProductName',
        'job_id': 'JobID',
        'job_type': 'JobType',
        'part_of_set': 'PartOfSet',
        'product_set': 'ProductSet',
        'queued_timestamp': 'QueuedTimestamp',
        'delivered_timestamp': 'DeliveredTimestamp',
        'cancelled_timestamp': 'CancelledTimestamp',
        'deleted_timestamp': 'DeletedTimestamp',
        'completed_timestamp': 'CompletedTimestamp',
        'failed_timestamp': 'FailedTimestamp',
        'detached_timestamp': 'DetachedTimestamp',
        'deferred_timestamp': 'DeferredTimestamp',
        'started_timestamp': 'StartedTimestamp',
        'waiting_timestamp': 'WaitingTimestamp',
        'orphaned_timestamp': 'OrphanedTimestamp',
        'installing_timestamp': 'InstallingTimestamp'
    }

    def __init__(self, product_id=None, product_name=None, job_id=None, job_type=None, part_of_set=None, product_set=None, queued_timestamp=None, delivered_timestamp=None, cancelled_timestamp=None, deleted_timestamp=None, completed_timestamp=None, failed_timestamp=None, detached_timestamp=None, deferred_timestamp=None, started_timestamp=None, waiting_timestamp=None, orphaned_timestamp=None, installing_timestamp=None, _configuration=None):  # noqa: E501
        """ProvisioningJobsTimestampDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_id = None
        self._product_name = None
        self._job_id = None
        self._job_type = None
        self._part_of_set = None
        self._product_set = None
        self._queued_timestamp = None
        self._delivered_timestamp = None
        self._cancelled_timestamp = None
        self._deleted_timestamp = None
        self._completed_timestamp = None
        self._failed_timestamp = None
        self._detached_timestamp = None
        self._deferred_timestamp = None
        self._started_timestamp = None
        self._waiting_timestamp = None
        self._orphaned_timestamp = None
        self._installing_timestamp = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if part_of_set is not None:
            self.part_of_set = part_of_set
        if product_set is not None:
            self.product_set = product_set
        if queued_timestamp is not None:
            self.queued_timestamp = queued_timestamp
        if delivered_timestamp is not None:
            self.delivered_timestamp = delivered_timestamp
        if cancelled_timestamp is not None:
            self.cancelled_timestamp = cancelled_timestamp
        if deleted_timestamp is not None:
            self.deleted_timestamp = deleted_timestamp
        if completed_timestamp is not None:
            self.completed_timestamp = completed_timestamp
        if failed_timestamp is not None:
            self.failed_timestamp = failed_timestamp
        if detached_timestamp is not None:
            self.detached_timestamp = detached_timestamp
        if deferred_timestamp is not None:
            self.deferred_timestamp = deferred_timestamp
        if started_timestamp is not None:
            self.started_timestamp = started_timestamp
        if waiting_timestamp is not None:
            self.waiting_timestamp = waiting_timestamp
        if orphaned_timestamp is not None:
            self.orphaned_timestamp = orphaned_timestamp
        if installing_timestamp is not None:
            self.installing_timestamp = installing_timestamp

    @property
    def product_id(self):
        """Gets the product_id of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Product Id.  # noqa: E501

        :return: The product_id of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProvisioningJobsTimestampDetails.

        Gets or sets Product Id.  # noqa: E501

        :param product_id: The product_id of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Product Name.  # noqa: E501

        :return: The product_name of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ProvisioningJobsTimestampDetails.

        Gets or sets Product Name.  # noqa: E501

        :param product_name: The product_name of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def job_id(self):
        """Gets the job_id of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Job Id.  # noqa: E501

        :return: The job_id of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ProvisioningJobsTimestampDetails.

        Gets or sets Job Id.  # noqa: E501

        :param job_id: The job_id of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: int
        """

        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Job Type.  # noqa: E501

        :return: The job_type of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ProvisioningJobsTimestampDetails.

        Gets or sets Job Type.  # noqa: E501

        :param job_type: The job_type of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._job_type = job_type

    @property
    def part_of_set(self):
        """Gets the part_of_set of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets whether part of a Product Set or not.  # noqa: E501

        :return: The part_of_set of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._part_of_set

    @part_of_set.setter
    def part_of_set(self, part_of_set):
        """Sets the part_of_set of this ProvisioningJobsTimestampDetails.

        Gets or sets whether part of a Product Set or not.  # noqa: E501

        :param part_of_set: The part_of_set of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._part_of_set = part_of_set

    @property
    def product_set(self):
        """Gets the product_set of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Product Set Name.  # noqa: E501

        :return: The product_set of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._product_set

    @product_set.setter
    def product_set(self, product_set):
        """Sets the product_set of this ProvisioningJobsTimestampDetails.

        Gets or sets Product Set Name.  # noqa: E501

        :param product_set: The product_set of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._product_set = product_set

    @property
    def queued_timestamp(self):
        """Gets the queued_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Queued.  # noqa: E501

        :return: The queued_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._queued_timestamp

    @queued_timestamp.setter
    def queued_timestamp(self, queued_timestamp):
        """Sets the queued_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Queued.  # noqa: E501

        :param queued_timestamp: The queued_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._queued_timestamp = queued_timestamp

    @property
    def delivered_timestamp(self):
        """Gets the delivered_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Delivered.  # noqa: E501

        :return: The delivered_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._delivered_timestamp

    @delivered_timestamp.setter
    def delivered_timestamp(self, delivered_timestamp):
        """Sets the delivered_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Delivered.  # noqa: E501

        :param delivered_timestamp: The delivered_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._delivered_timestamp = delivered_timestamp

    @property
    def cancelled_timestamp(self):
        """Gets the cancelled_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Cancelled.  # noqa: E501

        :return: The cancelled_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._cancelled_timestamp

    @cancelled_timestamp.setter
    def cancelled_timestamp(self, cancelled_timestamp):
        """Sets the cancelled_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Cancelled.  # noqa: E501

        :param cancelled_timestamp: The cancelled_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._cancelled_timestamp = cancelled_timestamp

    @property
    def deleted_timestamp(self):
        """Gets the deleted_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Deleted.  # noqa: E501

        :return: The deleted_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._deleted_timestamp

    @deleted_timestamp.setter
    def deleted_timestamp(self, deleted_timestamp):
        """Sets the deleted_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Deleted.  # noqa: E501

        :param deleted_timestamp: The deleted_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._deleted_timestamp = deleted_timestamp

    @property
    def completed_timestamp(self):
        """Gets the completed_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Completed.  # noqa: E501

        :return: The completed_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._completed_timestamp

    @completed_timestamp.setter
    def completed_timestamp(self, completed_timestamp):
        """Sets the completed_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Completed.  # noqa: E501

        :param completed_timestamp: The completed_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._completed_timestamp = completed_timestamp

    @property
    def failed_timestamp(self):
        """Gets the failed_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Failed.  # noqa: E501

        :return: The failed_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._failed_timestamp

    @failed_timestamp.setter
    def failed_timestamp(self, failed_timestamp):
        """Sets the failed_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Failed.  # noqa: E501

        :param failed_timestamp: The failed_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._failed_timestamp = failed_timestamp

    @property
    def detached_timestamp(self):
        """Gets the detached_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Detached.  # noqa: E501

        :return: The detached_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._detached_timestamp

    @detached_timestamp.setter
    def detached_timestamp(self, detached_timestamp):
        """Sets the detached_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Detached.  # noqa: E501

        :param detached_timestamp: The detached_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._detached_timestamp = detached_timestamp

    @property
    def deferred_timestamp(self):
        """Gets the deferred_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Deferred.  # noqa: E501

        :return: The deferred_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._deferred_timestamp

    @deferred_timestamp.setter
    def deferred_timestamp(self, deferred_timestamp):
        """Sets the deferred_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Deferred.  # noqa: E501

        :param deferred_timestamp: The deferred_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._deferred_timestamp = deferred_timestamp

    @property
    def started_timestamp(self):
        """Gets the started_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Started.  # noqa: E501

        :return: The started_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._started_timestamp

    @started_timestamp.setter
    def started_timestamp(self, started_timestamp):
        """Sets the started_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Started.  # noqa: E501

        :param started_timestamp: The started_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._started_timestamp = started_timestamp

    @property
    def waiting_timestamp(self):
        """Gets the waiting_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Waiting.  # noqa: E501

        :return: The waiting_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._waiting_timestamp

    @waiting_timestamp.setter
    def waiting_timestamp(self, waiting_timestamp):
        """Sets the waiting_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Waiting.  # noqa: E501

        :param waiting_timestamp: The waiting_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._waiting_timestamp = waiting_timestamp

    @property
    def orphaned_timestamp(self):
        """Gets the orphaned_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Orphaned.  # noqa: E501

        :return: The orphaned_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._orphaned_timestamp

    @orphaned_timestamp.setter
    def orphaned_timestamp(self, orphaned_timestamp):
        """Sets the orphaned_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Orphaned.  # noqa: E501

        :param orphaned_timestamp: The orphaned_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._orphaned_timestamp = orphaned_timestamp

    @property
    def installing_timestamp(self):
        """Gets the installing_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501

        Gets or sets Date Installing.  # noqa: E501

        :return: The installing_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :rtype: str
        """
        return self._installing_timestamp

    @installing_timestamp.setter
    def installing_timestamp(self, installing_timestamp):
        """Sets the installing_timestamp of this ProvisioningJobsTimestampDetails.

        Gets or sets Date Installing.  # noqa: E501

        :param installing_timestamp: The installing_timestamp of this ProvisioningJobsTimestampDetails.  # noqa: E501
        :type: str
        """

        self._installing_timestamp = installing_timestamp

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
        if issubclass(ProvisioningJobsTimestampDetails, dict):
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
        if not isinstance(other, ProvisioningJobsTimestampDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProvisioningJobsTimestampDetails):
            return True

        return self.to_dict() != other.to_dict()
