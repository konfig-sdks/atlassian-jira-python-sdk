from atlassian_jira_python_sdk.paths.rest_api_3_priority_id.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_priority_id.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_priority_id.delete import ApiFordelete


class RestApi3PriorityId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
