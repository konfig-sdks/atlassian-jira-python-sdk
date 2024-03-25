from atlassian_jira_python_sdk.paths.rest_api_3_dashboard_id.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_dashboard_id.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_dashboard_id.delete import ApiFordelete


class RestApi3DashboardId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
