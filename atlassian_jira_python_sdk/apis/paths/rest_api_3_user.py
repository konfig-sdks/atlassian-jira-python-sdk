from atlassian_jira_python_sdk.paths.rest_api_3_user.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_user.post import ApiForpost
from atlassian_jira_python_sdk.paths.rest_api_3_user.delete import ApiFordelete


class RestApi3User(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
