# coding: utf-8

"""
    MAM API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mamv2
from mamv2.api.blobs_v2_api import BlobsV2Api  # noqa: E501
from mamv2.rest import ApiException


class TestBlobsV2Api(unittest.TestCase):
    """BlobsV2Api unit test stubs"""

    def setUp(self):
        self.api = mamv2.api.blobs_v2_api.BlobsV2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_blobs_v2_delete(self):
        """Test case for blobs_v2_delete

        New - Deletes a blob by Guid  # noqa: E501
        """
        pass

    def test_blobs_v2_head(self):
        """Test case for blobs_v2_head

        New - Gets a blob contents information by the Guid  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
