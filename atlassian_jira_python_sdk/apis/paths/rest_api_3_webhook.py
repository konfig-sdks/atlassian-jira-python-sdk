from atlassian_jira_python_sdk.paths.rest_api_3_webhook.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_webhook.post import ApiForpost
from atlassian_jira_python_sdk.paths.rest_api_3_webhook.delete import ApiFordelete


class RestApi3Webhook(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
