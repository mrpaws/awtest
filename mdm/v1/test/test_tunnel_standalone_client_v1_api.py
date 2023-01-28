# coding: utf-8

"""
    MDM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mdmv1
from mdmv1.api.tunnel_standalone_client_v1_api import TunnelStandaloneClientV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestTunnelStandaloneClientV1Api(unittest.TestCase):
    """TunnelStandaloneClientV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.tunnel_standalone_client_v1_api.TunnelStandaloneClientV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_tunnel_standalone_client_v1_create_one_time_token_async(self):
        """Test case for tunnel_standalone_client_v1_create_one_time_token_async

        New - Generates one time token to allow device to obtain authentication certificate  # noqa: E501
        """
        pass

    def test_tunnel_standalone_client_v1_get_tunnel_configuration_async(self):
        """Test case for tunnel_standalone_client_v1_get_tunnel_configuration_async

        New - Retrieves the tunnel configuration for the device.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()