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
from mdmv2.api.pick_lists_v2_api import PickListsV2Api  # noqa: E501
from mdmv2.rest import ApiException


class TestPickListsV2Api(unittest.TestCase):
    """PickListsV2Api unit test stubs"""

    def setUp(self):
        self.api = mdmv2.api.pick_lists_v2_api.PickListsV2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_pick_lists_v2_get_device_certificate_authorities_async(self):
        """Test case for pick_lists_v2_get_device_certificate_authorities_async

        New - Gets the list of Certificate Authorities (CA) for an organization group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
