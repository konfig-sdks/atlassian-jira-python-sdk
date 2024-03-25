from atlassian_jira_python_sdk.paths.rest_api_3_group_user.post import ApiForpost
from atlassian_jira_python_sdk.paths.rest_api_3_group_user.delete import ApiFordelete


class RestApi3GroupUser(
    ApiForpost,
    ApiFordelete,
):
    pass
