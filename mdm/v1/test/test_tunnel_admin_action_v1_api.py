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
from mdmv1.api.tunnel_admin_action_v1_api import TunnelAdminActionV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestTunnelAdminActionV1Api(unittest.TestCase):
    """TunnelAdminActionV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.tunnel_admin_action_v1_api.TunnelAdminActionV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_tunnel_admin_action_v1_get_tunnel_admin_actions_info_async(self):
        """Test case for tunnel_admin_action_v1_get_tunnel_admin_actions_info_async

        New - Gets the device access information.  # noqa: E501
        """
        pass

    def test_tunnel_admin_action_v1_perform_console_admin_action_async(self):
        """Test case for tunnel_admin_action_v1_perform_console_admin_action_async

        New - Perform the operation on tunnel device.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
