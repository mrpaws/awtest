# coding: utf-8

"""
    MAM API V1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mamv1
from mamv1.api.chunk_api import ChunkApi  # noqa: E501
from mamv1.rest import ApiException


class TestChunkApi(unittest.TestCase):
    """ChunkApi unit test stubs"""

    def setUp(self):
        self.api = mamv1.api.chunk_api.ChunkApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_chunk_chunk_async(self):
        """Test case for chunk_chunk_async

        New - upload the chunks.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
