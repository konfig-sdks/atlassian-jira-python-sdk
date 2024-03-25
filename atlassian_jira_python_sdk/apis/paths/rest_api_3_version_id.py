from atlassian_jira_python_sdk.paths.rest_api_3_version_id.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_version_id.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_version_id.delete import ApiFordelete


class RestApi3VersionId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
