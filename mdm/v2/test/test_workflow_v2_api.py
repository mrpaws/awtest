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
from mdmv2.api.workflow_v2_api import WorkflowV2Api  # noqa: E501
from mdmv2.rest import ApiException


class TestWorkflowV2Api(unittest.TestCase):
    """WorkflowV2Api unit test stubs"""

    def setUp(self):
        self.api = mdmv2.api.workflow_v2_api.WorkflowV2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_workflow_v2_create_workflow_async(self):
        """Test case for workflow_v2_create_workflow_async

        New - Create a new workflow.  # noqa: E501
        """
        pass

    def test_workflow_v2_get_all_workflows_async(self):
        """Test case for workflow_v2_get_all_workflows_async

        New - Get all workflows at this Organization Group.  # noqa: E501
        """
        pass

    def test_workflow_v2_get_workflow_by_id_async(self):
        """Test case for workflow_v2_get_workflow_by_id_async

        New - Get the workflow corresponding to the workflow uuid.  # noqa: E501
        """
        pass

    def test_workflow_v2_update_workflow_async(self):
        """Test case for workflow_v2_update_workflow_async

        New - Update a workflow.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()