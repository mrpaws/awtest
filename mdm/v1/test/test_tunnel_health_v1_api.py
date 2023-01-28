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
from mdmv1.api.tunnel_health_v1_api import TunnelHealthV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestTunnelHealthV1Api(unittest.TestCase):
    """TunnelHealthV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.tunnel_health_v1_api.TunnelHealthV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_tunnel_health_v1_health_async(self):
        """Test case for tunnel_health_v1_health_async

        New - Return health information for tunnel connectivity.  # noqa: E501
        """
        pass

    def test_tunnel_health_v1_health_downstream_async(self):
        """Test case for tunnel_health_v1_health_downstream_async

        New - Return health information for tunnel downstream connectivity from microservice.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
