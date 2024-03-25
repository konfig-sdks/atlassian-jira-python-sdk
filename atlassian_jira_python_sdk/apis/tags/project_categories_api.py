# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_project_category.post import Create
from atlassian_jira_python_sdk.paths.rest_api_3_project_category_id.delete import DeleteCategory
from atlassian_jira_python_sdk.paths.rest_api_3_project_category.get import GetAll
from atlassian_jira_python_sdk.paths.rest_api_3_project_category_id.get import GetCategoryById
from atlassian_jira_python_sdk.paths.rest_api_3_project_category_id.put import UpdateCategory
from atlassian_jira_python_sdk.apis.tags.project_categories_api_raw import ProjectCategoriesApiRaw


class ProjectCategoriesApi(
    Create,
    DeleteCategory,
    GetAll,
    GetCategoryById,
    UpdateCategory,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ProjectCategoriesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ProjectCategoriesApiRaw(api_client)