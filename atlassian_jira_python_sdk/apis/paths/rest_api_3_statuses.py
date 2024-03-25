from atlassian_jira_python_sdk.paths.rest_api_3_statuses.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_statuses.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_statuses.post import ApiForpost
from atlassian_jira_python_sdk.paths.rest_api_3_statuses.delete import ApiFordelete


class RestApi3Statuses(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
):
    pass
