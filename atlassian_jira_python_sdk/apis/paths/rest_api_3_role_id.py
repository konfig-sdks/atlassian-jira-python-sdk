from atlassian_jira_python_sdk.paths.rest_api_3_role_id.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_role_id.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_role_id.post import ApiForpost
from atlassian_jira_python_sdk.paths.rest_api_3_role_id.delete import ApiFordelete


class RestApi3RoleId(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
