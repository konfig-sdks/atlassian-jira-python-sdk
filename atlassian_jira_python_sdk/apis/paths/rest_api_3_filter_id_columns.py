from atlassian_jira_python_sdk.paths.rest_api_3_filter_id_columns.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_filter_id_columns.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_filter_id_columns.delete import ApiFordelete


class RestApi3FilterIdColumns(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
