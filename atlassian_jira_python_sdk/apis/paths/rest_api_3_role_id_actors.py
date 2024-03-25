from atlassian_jira_python_sdk.paths.rest_api_3_role_id_actors.get import ApiForget
from atlassian_jira_python_sdk.paths.rest_api_3_role_id_actors.post import ApiForpost
from atlassian_jira_python_sdk.paths.rest_api_3_role_id_actors.delete import ApiFordelete


class RestApi3RoleIdActors(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
