from atlassian_jira_python_sdk.paths.rest_api_3_filter_id.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_filter_id.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_filter_id.delete import ApiFordelete


class RestApi3FilterId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass