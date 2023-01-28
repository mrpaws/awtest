# coding: utf-8

"""
    System API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import systemv1
from systemv1.api.cloud_connector_api import CloudConnectorApi  # noqa: E501
from systemv1.rest import ApiException


class TestCloudConnectorApi(unittest.TestCase):
    """CloudConnectorApi unit test stubs"""

    def setUp(self):
        self.api = systemv1.api.cloud_connector_api.CloudConnectorApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cloud_connector_get_connection_status_async(self):
        """Test case for cloud_connector_get_connection_status_async

        New - Returns the connection status for the AirWatch Cloud Connector configured for the given organization group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()