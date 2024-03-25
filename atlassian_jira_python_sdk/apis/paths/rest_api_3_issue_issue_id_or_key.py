from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key.put import ApiForput
from atlassian_jira_python_sdk.paths.rest_api_3_issue_issue_id_or_key.delete import ApiFordelete


class RestApi3IssueIssueIdOrKey(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
