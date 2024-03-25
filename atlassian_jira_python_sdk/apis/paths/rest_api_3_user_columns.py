from atlassian_jira_python_sdk.paths.rest_api_3_user_columns.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_user_columns.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_user_columns.delete import ApiFordelete


class RestApi3UserColumns(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
