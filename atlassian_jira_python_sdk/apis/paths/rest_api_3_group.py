from atlassian_jira_python_sdk.paths.rest_api_3_group.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_group.post import ApiForpost
from atlassian_jira_python_sdk.paths.rest_api_3_group.delete import ApiFordelete


class RestApi3Group(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
