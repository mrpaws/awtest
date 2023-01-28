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
from mdmv1.api.tags_api import TagsApi  # noqa: E501
from mdmv1.rest import ApiException


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self):
        self.api = mdmv1.api.tags_api.TagsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tags_add_devices_to_tag_async(self):
        """Test case for tags_add_devices_to_tag_async

        Add devices to the tag.  # noqa: E501
        """
        pass

    def test_tags_add_tag(self):
        """Test case for tags_add_tag

        Add a new tag.  # noqa: E501
        """
        pass

    def test_tags_delete_tag_async(self):
        """Test case for tags_delete_tag_async

        Delete a tag.  # noqa: E501
        """
        pass

    def test_tags_devices_for_tag_async(self):
        """Test case for tags_devices_for_tag_async

        Retrieves all the devices with the specified tag.  # noqa: E501
        """
        pass

    def test_tags_remove_devices_from_tag_async(self):
        """Test case for tags_remove_devices_from_tag_async

        Remove devices from the tag.  # noqa: E501
        """
        pass

    def test_tags_update_tag(self):
        """Test case for tags_update_tag

        Updates a tag name, tag type or tag avatar.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
