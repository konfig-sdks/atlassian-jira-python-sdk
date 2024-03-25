from atlassian_jira_python_sdk.paths.rest_api_3_issuetype_id.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_issuetype_id.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_issuetype_id.delete import ApiFordelete


class RestApi3IssuetypeId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
