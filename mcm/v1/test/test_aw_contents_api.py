# coding: utf-8

"""
    MCM API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mcmv1
from mcmv1.api.aw_contents_api import AwContentsApi  # noqa: E501
from mcmv1.rest import ApiException


class TestAwContentsApi(unittest.TestCase):
    """AwContentsApi unit test stubs"""

    def setUp(self):
        self.api = mcmv1.api.aw_contents_api.AwContentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aw_contents_delete_file(self):
        """Test case for aw_contents_delete_file

        New - Delete a Managed content.  # noqa: E501
        """
        pass

    def test_aw_contents_download_file(self):
        """Test case for aw_contents_download_file

        New - Download a Managed content.  # noqa: E501
        """
        pass

    def test_aw_contents_get_file_metadata_async(self):
        """Test case for aw_contents_get_file_metadata_async

        New - Get metadata for a Managed content.  # noqa: E501
        """
        pass

    def test_aw_contents_search_async(self):
        """Test case for aw_contents_search_async

        New - Search managed content.  # noqa: E501
        """
        pass

    def test_aw_contents_update_file_metadata_async(self):
        """Test case for aw_contents_update_file_metadata_async

        New - Update metadata for a Managed content.  # noqa: E501
        """
        pass

    def test_aw_contents_upload_file_async(self):
        """Test case for aw_contents_upload_file_async

        New - Upload a Managed content.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()