from atlassian_jira_python_sdk.paths.rest_api_3_resolution_id.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_resolution_id.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_resolution_id.delete import ApiFordelete


class RestApi3ResolutionId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
