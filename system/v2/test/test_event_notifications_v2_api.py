# coding: utf-8

"""
    System API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import systemv2
from systemv2.api.event_notifications_v2_api import EventNotificationsV2Api  # noqa: E501
from systemv2.rest import ApiException


class TestEventNotificationsV2Api(unittest.TestCase):
    """EventNotificationsV2Api unit test stubs"""

    def setUp(self):
        self.api = systemv2.api.event_notifications_v2_api.EventNotificationsV2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_event_notifications_v2_create_event_notification_rule(self):
        """Test case for event_notifications_v2_create_event_notification_rule

        New - Creates a new Event Notification rule with events to subscribe to.  # noqa: E501
        """
        pass

    def test_event_notifications_v2_delete_event_notification_rule(self):
        """Test case for event_notifications_v2_delete_event_notification_rule

        New - Deletes an Event Notification Rule identified by the Event Notification Id.  # noqa: E501
        """
        pass

    def test_event_notifications_v2_get_event_notification_by_id(self):
        """Test case for event_notifications_v2_get_event_notification_by_id

        New - Retrieves details of an Event Notification Rule identified by EventNotification Id.  # noqa: E501
        """
        pass

    def test_event_notifications_v2_get_event_notifications_and_subscriptions(self):
        """Test case for event_notifications_v2_get_event_notifications_and_subscriptions

        Get Event Notifications and Subscriptions based on optional OrganizationGroup Id or page size.  # noqa: E501
        """
        pass

    def test_event_notifications_v2_search(self):
        """Test case for event_notifications_v2_search

        New - Searches Event Notifications based on the query information provided.  # noqa: E501
        """
        pass

    def test_event_notifications_v2_update_event_notification_rule(self):
        """Test case for event_notifications_v2_update_event_notification_rule

        New - Updates an Event Notification Rule identified by the Event Notification Id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()