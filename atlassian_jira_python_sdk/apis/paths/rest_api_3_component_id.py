from atlassian_jira_python_sdk.paths.rest_api_3_component_id.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_component_id.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_component_id.delete import ApiFordelete


class RestApi3ComponentId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass