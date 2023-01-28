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


class IActionResult(object):
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
        'request_query': 'IRequestQuery',
        'request_message': 'object',
        'http_status_code': 'int',
        'retry_after': 'str',
        'model': 'object',
        'stream': 'Stream',
        'partial_content_range': 'RangeHeaderValue',
        'byte_array': 'str',
        'file_name': 'str',
        'media_type': 'str',
        'on_stream_available': 'Action3',
        'e_tag_header_value': 'EntityTagHeaderValue',
        'accepts_byte_ranges': 'bool',
        'send_e_tag_header_value': 'bool',
        'location_header_value': 'str',
        'cache_control_value': 'CacheControlHeaderValue',
        'content_length': 'int',
        'response_date_time_format': 'str',
        'http_response_message': 'object'
    }

    attribute_map = {
        'request_query': 'RequestQuery',
        'request_message': 'RequestMessage',
        'http_status_code': 'HttpStatusCode',
        'retry_after': 'RetryAfter',
        'model': 'Model',
        'stream': 'Stream',
        'partial_content_range': 'PartialContentRange',
        'byte_array': 'ByteArray',
        'file_name': 'FileName',
        'media_type': 'MediaType',
        'on_stream_available': 'OnStreamAvailable',
        'e_tag_header_value': 'ETagHeaderValue',
        'accepts_byte_ranges': 'AcceptsByteRanges',
        'send_e_tag_header_value': 'SendETagHeaderValue',
        'location_header_value': 'LocationHeaderValue',
        'cache_control_value': 'CacheControlValue',
        'content_length': 'ContentLength',
        'response_date_time_format': 'ResponseDateTimeFormat',
        'http_response_message': 'HttpResponseMessage'
    }

    def __init__(self, request_query=None, request_message=None, http_status_code=None, retry_after=None, model=None, stream=None, partial_content_range=None, byte_array=None, file_name=None, media_type=None, on_stream_available=None, e_tag_header_value=None, accepts_byte_ranges=None, send_e_tag_header_value=None, location_header_value=None, cache_control_value=None, content_length=None, response_date_time_format=None, http_response_message=None, _configuration=None):  # noqa: E501
        """IActionResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._request_query = None
        self._request_message = None
        self._http_status_code = None
        self._retry_after = None
        self._model = None
        self._stream = None
        self._partial_content_range = None
        self._byte_array = None
        self._file_name = None
        self._media_type = None
        self._on_stream_available = None
        self._e_tag_header_value = None
        self._accepts_byte_ranges = None
        self._send_e_tag_header_value = None
        self._location_header_value = None
        self._cache_control_value = None
        self._content_length = None
        self._response_date_time_format = None
        self._http_response_message = None
        self.discriminator = None

        if request_query is not None:
            self.request_query = request_query
        if request_message is not None:
            self.request_message = request_message
        if http_status_code is not None:
            self.http_status_code = http_status_code
        if retry_after is not None:
            self.retry_after = retry_after
        if model is not None:
            self.model = model
        if stream is not None:
            self.stream = stream
        if partial_content_range is not None:
            self.partial_content_range = partial_content_range
        if byte_array is not None:
            self.byte_array = byte_array
        if file_name is not None:
            self.file_name = file_name
        if media_type is not None:
            self.media_type = media_type
        if on_stream_available is not None:
            self.on_stream_available = on_stream_available
        if e_tag_header_value is not None:
            self.e_tag_header_value = e_tag_header_value
        if accepts_byte_ranges is not None:
            self.accepts_byte_ranges = accepts_byte_ranges
        if send_e_tag_header_value is not None:
            self.send_e_tag_header_value = send_e_tag_header_value
        if location_header_value is not None:
            self.location_header_value = location_header_value
        if cache_control_value is not None:
            self.cache_control_value = cache_control_value
        if content_length is not None:
            self.content_length = content_length
        if response_date_time_format is not None:
            self.response_date_time_format = response_date_time_format
        if http_response_message is not None:
            self.http_response_message = http_response_message

    @property
    def request_query(self):
        """Gets the request_query of this IActionResult.  # noqa: E501

        Gets or sets the RequestQuery.  # noqa: E501

        :return: The request_query of this IActionResult.  # noqa: E501
        :rtype: IRequestQuery
        """
        return self._request_query

    @request_query.setter
    def request_query(self, request_query):
        """Sets the request_query of this IActionResult.

        Gets or sets the RequestQuery.  # noqa: E501

        :param request_query: The request_query of this IActionResult.  # noqa: E501
        :type: IRequestQuery
        """

        self._request_query = request_query

    @property
    def request_message(self):
        """Gets the request_message of this IActionResult.  # noqa: E501

        Gets or sets the RequestMessage.  # noqa: E501

        :return: The request_message of this IActionResult.  # noqa: E501
        :rtype: object
        """
        return self._request_message

    @request_message.setter
    def request_message(self, request_message):
        """Sets the request_message of this IActionResult.

        Gets or sets the RequestMessage.  # noqa: E501

        :param request_message: The request_message of this IActionResult.  # noqa: E501
        :type: object
        """

        self._request_message = request_message

    @property
    def http_status_code(self):
        """Gets the http_status_code of this IActionResult.  # noqa: E501

        Gets or sets HttpStatusCode.  # noqa: E501

        :return: The http_status_code of this IActionResult.  # noqa: E501
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this IActionResult.

        Gets or sets HttpStatusCode.  # noqa: E501

        :param http_status_code: The http_status_code of this IActionResult.  # noqa: E501
        :type: int
        """
        allowed_values = [100, 101, 200, 201, 202, 203, 204, 205, 206, 300, 301, 302, 303, 304, 305, 306, 307, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 426, 500, 501, 502, 503, 504, 505]  # noqa: E501
        if (self._configuration.client_side_validation and
                http_status_code not in allowed_values):
            raise ValueError(
                "Invalid value for `http_status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(http_status_code, allowed_values)
            )

        self._http_status_code = http_status_code

    @property
    def retry_after(self):
        """Gets the retry_after of this IActionResult.  # noqa: E501

        Gets or sets retry-after value.  # noqa: E501

        :return: The retry_after of this IActionResult.  # noqa: E501
        :rtype: str
        """
        return self._retry_after

    @retry_after.setter
    def retry_after(self, retry_after):
        """Sets the retry_after of this IActionResult.

        Gets or sets retry-after value.  # noqa: E501

        :param retry_after: The retry_after of this IActionResult.  # noqa: E501
        :type: str
        """

        self._retry_after = retry_after

    @property
    def model(self):
        """Gets the model of this IActionResult.  # noqa: E501

        Gets or sets Model.  # noqa: E501

        :return: The model of this IActionResult.  # noqa: E501
        :rtype: object
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this IActionResult.

        Gets or sets Model.  # noqa: E501

        :param model: The model of this IActionResult.  # noqa: E501
        :type: object
        """

        self._model = model

    @property
    def stream(self):
        """Gets the stream of this IActionResult.  # noqa: E501

        Gets or sets Stream.  # noqa: E501

        :return: The stream of this IActionResult.  # noqa: E501
        :rtype: Stream
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this IActionResult.

        Gets or sets Stream.  # noqa: E501

        :param stream: The stream of this IActionResult.  # noqa: E501
        :type: Stream
        """

        self._stream = stream

    @property
    def partial_content_range(self):
        """Gets the partial_content_range of this IActionResult.  # noqa: E501

        Gets or sets partial content range.  # noqa: E501

        :return: The partial_content_range of this IActionResult.  # noqa: E501
        :rtype: RangeHeaderValue
        """
        return self._partial_content_range

    @partial_content_range.setter
    def partial_content_range(self, partial_content_range):
        """Sets the partial_content_range of this IActionResult.

        Gets or sets partial content range.  # noqa: E501

        :param partial_content_range: The partial_content_range of this IActionResult.  # noqa: E501
        :type: RangeHeaderValue
        """

        self._partial_content_range = partial_content_range

    @property
    def byte_array(self):
        """Gets the byte_array of this IActionResult.  # noqa: E501

        Gets or sets ByteArray.  # noqa: E501

        :return: The byte_array of this IActionResult.  # noqa: E501
        :rtype: str
        """
        return self._byte_array

    @byte_array.setter
    def byte_array(self, byte_array):
        """Sets the byte_array of this IActionResult.

        Gets or sets ByteArray.  # noqa: E501

        :param byte_array: The byte_array of this IActionResult.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                byte_array is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', byte_array)):  # noqa: E501
            raise ValueError(r"Invalid value for `byte_array`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._byte_array = byte_array

    @property
    def file_name(self):
        """Gets the file_name of this IActionResult.  # noqa: E501

        Gets or sets FileName {Will be set in the content-disposition header}.  # noqa: E501

        :return: The file_name of this IActionResult.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this IActionResult.

        Gets or sets FileName {Will be set in the content-disposition header}.  # noqa: E501

        :param file_name: The file_name of this IActionResult.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def media_type(self):
        """Gets the media_type of this IActionResult.  # noqa: E501

        Gets or sets MediaType.  # noqa: E501

        :return: The media_type of this IActionResult.  # noqa: E501
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this IActionResult.

        Gets or sets MediaType.  # noqa: E501

        :param media_type: The media_type of this IActionResult.  # noqa: E501
        :type: str
        """

        self._media_type = media_type

    @property
    def on_stream_available(self):
        """Gets the on_stream_available of this IActionResult.  # noqa: E501

        Gets or sets OnStreamAvailable.  # noqa: E501

        :return: The on_stream_available of this IActionResult.  # noqa: E501
        :rtype: Action3
        """
        return self._on_stream_available

    @on_stream_available.setter
    def on_stream_available(self, on_stream_available):
        """Sets the on_stream_available of this IActionResult.

        Gets or sets OnStreamAvailable.  # noqa: E501

        :param on_stream_available: The on_stream_available of this IActionResult.  # noqa: E501
        :type: Action3
        """

        self._on_stream_available = on_stream_available

    @property
    def e_tag_header_value(self):
        """Gets the e_tag_header_value of this IActionResult.  # noqa: E501

        Gets or sets ETagHeaderValue.  # noqa: E501

        :return: The e_tag_header_value of this IActionResult.  # noqa: E501
        :rtype: EntityTagHeaderValue
        """
        return self._e_tag_header_value

    @e_tag_header_value.setter
    def e_tag_header_value(self, e_tag_header_value):
        """Sets the e_tag_header_value of this IActionResult.

        Gets or sets ETagHeaderValue.  # noqa: E501

        :param e_tag_header_value: The e_tag_header_value of this IActionResult.  # noqa: E501
        :type: EntityTagHeaderValue
        """

        self._e_tag_header_value = e_tag_header_value

    @property
    def accepts_byte_ranges(self):
        """Gets the accepts_byte_ranges of this IActionResult.  # noqa: E501

        Gets or sets a value indicating whether gets or sets a value which indicates whether a range byte request for a stream is accepted or not.  # noqa: E501

        :return: The accepts_byte_ranges of this IActionResult.  # noqa: E501
        :rtype: bool
        """
        return self._accepts_byte_ranges

    @accepts_byte_ranges.setter
    def accepts_byte_ranges(self, accepts_byte_ranges):
        """Sets the accepts_byte_ranges of this IActionResult.

        Gets or sets a value indicating whether gets or sets a value which indicates whether a range byte request for a stream is accepted or not.  # noqa: E501

        :param accepts_byte_ranges: The accepts_byte_ranges of this IActionResult.  # noqa: E501
        :type: bool
        """

        self._accepts_byte_ranges = accepts_byte_ranges

    @property
    def send_e_tag_header_value(self):
        """Gets the send_e_tag_header_value of this IActionResult.  # noqa: E501

        Gets or sets a value indicating whether gets or sets the option to include ETagHeaderValue.  # noqa: E501

        :return: The send_e_tag_header_value of this IActionResult.  # noqa: E501
        :rtype: bool
        """
        return self._send_e_tag_header_value

    @send_e_tag_header_value.setter
    def send_e_tag_header_value(self, send_e_tag_header_value):
        """Sets the send_e_tag_header_value of this IActionResult.

        Gets or sets a value indicating whether gets or sets the option to include ETagHeaderValue.  # noqa: E501

        :param send_e_tag_header_value: The send_e_tag_header_value of this IActionResult.  # noqa: E501
        :type: bool
        """

        self._send_e_tag_header_value = send_e_tag_header_value

    @property
    def location_header_value(self):
        """Gets the location_header_value of this IActionResult.  # noqa: E501

        Gets or sets LocationHeaderValue.  # noqa: E501

        :return: The location_header_value of this IActionResult.  # noqa: E501
        :rtype: str
        """
        return self._location_header_value

    @location_header_value.setter
    def location_header_value(self, location_header_value):
        """Sets the location_header_value of this IActionResult.

        Gets or sets LocationHeaderValue.  # noqa: E501

        :param location_header_value: The location_header_value of this IActionResult.  # noqa: E501
        :type: str
        """

        self._location_header_value = location_header_value

    @property
    def cache_control_value(self):
        """Gets the cache_control_value of this IActionResult.  # noqa: E501

        Gets or sets CacheControlValue.  # noqa: E501

        :return: The cache_control_value of this IActionResult.  # noqa: E501
        :rtype: CacheControlHeaderValue
        """
        return self._cache_control_value

    @cache_control_value.setter
    def cache_control_value(self, cache_control_value):
        """Sets the cache_control_value of this IActionResult.

        Gets or sets CacheControlValue.  # noqa: E501

        :param cache_control_value: The cache_control_value of this IActionResult.  # noqa: E501
        :type: CacheControlHeaderValue
        """

        self._cache_control_value = cache_control_value

    @property
    def content_length(self):
        """Gets the content_length of this IActionResult.  # noqa: E501

        Gets or sets ContentLength.  # noqa: E501

        :return: The content_length of this IActionResult.  # noqa: E501
        :rtype: int
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this IActionResult.

        Gets or sets ContentLength.  # noqa: E501

        :param content_length: The content_length of this IActionResult.  # noqa: E501
        :type: int
        """

        self._content_length = content_length

    @property
    def response_date_time_format(self):
        """Gets the response_date_time_format of this IActionResult.  # noqa: E501

        Gets or sets dateTime format for response.  # noqa: E501

        :return: The response_date_time_format of this IActionResult.  # noqa: E501
        :rtype: str
        """
        return self._response_date_time_format

    @response_date_time_format.setter
    def response_date_time_format(self, response_date_time_format):
        """Sets the response_date_time_format of this IActionResult.

        Gets or sets dateTime format for response.  # noqa: E501

        :param response_date_time_format: The response_date_time_format of this IActionResult.  # noqa: E501
        :type: str
        """

        self._response_date_time_format = response_date_time_format

    @property
    def http_response_message(self):
        """Gets the http_response_message of this IActionResult.  # noqa: E501

        Gets or sets HttpResponseMessage.  # noqa: E501

        :return: The http_response_message of this IActionResult.  # noqa: E501
        :rtype: object
        """
        return self._http_response_message

    @http_response_message.setter
    def http_response_message(self, http_response_message):
        """Sets the http_response_message of this IActionResult.

        Gets or sets HttpResponseMessage.  # noqa: E501

        :param http_response_message: The http_response_message of this IActionResult.  # noqa: E501
        :type: object
        """

        self._http_response_message = http_response_message

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
        if issubclass(IActionResult, dict):
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
        if not isinstance(other, IActionResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IActionResult):
            return True

        return self.to_dict() != other.to_dict()
