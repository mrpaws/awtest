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
from systemv1.api.tags_api import TagsApi  # noqa: E501
from systemv1.rest import ApiException


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = systemv1.api.tags_api.TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tags_create_tag_for_og(self):
        """Test case for tags_create_tag_for_og

        Retrieves a particular tag for the specified organization group.  # noqa: E501
        """
        pass

    def test_tags_delete_tag(self):
        """Test case for tags_delete_tag

        Deletes a tag for the specified organization group.  <br />Tag is a custom identifier that can be associated to a device(Example: Refursbished, Repaired).  # noqa: E501
        """
        pass

    def test_tags_get_tag(self):
        """Test case for tags_get_tag

        Retrieves the tag details for a given tag in an organization group.  # noqa: E501
        """
        pass

    def test_tags_get_tags_by_og(self):
        """Test case for tags_get_tags_by_og

        Retrieves the tags for the specified organization group.  # noqa: E501
        """
        pass

    def test_tags_update_tag_for_og(self):
        """Test case for tags_update_tag_for_og

        Updates a tag for the specified organization group.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
