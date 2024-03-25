from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_mypreferences.delete import ApiFordelete


class RestApi3Mypreferences(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
