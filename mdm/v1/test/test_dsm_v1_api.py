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
from mdmv1.api.dsm_v1_api import DsmV1Api  # noqa: E501
from mdmv1.rest import ApiException


class TestDsmV1Api(unittest.TestCase):
    """DsmV1Api unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.dsm_v1_api.DsmV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_dsm_v1_override_resources(self):
        """Test case for dsm_v1_override_resources

        Overrides the resource behaviour on the specified device.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
