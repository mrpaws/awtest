# coding: utf-8

"""
    MDM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mdmv2
from mdmv2.api.commands_v2_api import CommandsV2Api  # noqa: E501
from mdmv2.rest import ApiException


class TestCommandsV2Api(unittest.TestCase):
    """CommandsV2Api unit test stubs"""

    def setUp(self):
        self.api = mdmv2.api.commands_v2_api.CommandsV2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_commands_v2_bulk_execute_async(self):
        """Test case for commands_v2_bulk_execute_async

        New - Executes command for multiple devices identified by device uuid  # noqa: E501
        """
        pass

    def test_commands_v2_execute_async(self):
        """Test case for commands_v2_execute_async

        New - Executes a command for device by device uuid  # noqa: E501
        """
        pass

    def test_commands_v2_execute_by_alternate_id_async(self):
        """Test case for commands_v2_execute_by_alternate_id_async

        New - Executes a command for device by alternate ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()