# coding: utf-8

"""
    The Jira Cloud platform REST API

    Jira Cloud platform REST API documentation

    The version of the OpenAPI document: 1001.0.0-SNAPSHOT-9aad01a33a3dae75a5b6aedf98c77d2cbd2f865d
    Contact: ecosystem@atlassian.com
    Generated by: https://konfigthis.com
"""

from atlassian_jira_python_sdk.paths.rest_api_3_project_category.post import CreateRaw
from atlassian_jira_python_sdk.paths.rest_api_3_project_category_id.delete import DeleteCategoryRaw
from atlassian_jira_python_sdk.paths.rest_api_3_project_category.get import GetAllRaw
from atlassian_jira_python_sdk.paths.rest_api_3_project_category_id.get import GetCategoryByIdRaw
from atlassian_jira_python_sdk.paths.rest_api_3_project_category_id.put import UpdateCategoryRaw


class ProjectCategoriesApiRaw(
    CreateRaw,
    DeleteCategoryRaw,
    GetAllRaw,
    GetCategoryByIdRaw,
    UpdateCategoryRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
