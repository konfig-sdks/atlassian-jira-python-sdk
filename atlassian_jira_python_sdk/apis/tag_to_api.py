import typing_extensions

from atlassian_jira_python_sdk.apis.tags import TagValues
from atlassian_jira_python_sdk.apis.tags.issues_api import IssuesApi
from atlassian_jira_python_sdk.apis.tags.dashboards_api import DashboardsApi
from atlassian_jira_python_sdk.apis.tags.workflow_schemes_api import WorkflowSchemesApi
from atlassian_jira_python_sdk.apis.tags.issue_security_schemes_api import IssueSecuritySchemesApi
from atlassian_jira_python_sdk.apis.tags.issue_field_configurations_api import IssueFieldConfigurationsApi
from atlassian_jira_python_sdk.apis.tags.project_versions_api import ProjectVersionsApi
from atlassian_jira_python_sdk.apis.tags.workflow_scheme_drafts_api import WorkflowSchemeDraftsApi
from atlassian_jira_python_sdk.apis.tags.filters_api import FiltersApi
from atlassian_jira_python_sdk.apis.tags.issue_custom_field_contexts_api import IssueCustomFieldContextsApi
from atlassian_jira_python_sdk.apis.tags.projects_api import ProjectsApi
from atlassian_jira_python_sdk.apis.tags.users_api import UsersApi
from atlassian_jira_python_sdk.apis.tags.issue_type_screen_schemes_api import IssueTypeScreenSchemesApi
from atlassian_jira_python_sdk.apis.tags.issue_type_schemes_api import IssueTypeSchemesApi
from atlassian_jira_python_sdk.apis.tags.workflows_api import WorkflowsApi
from atlassian_jira_python_sdk.apis.tags.issue_fields_api import IssueFieldsApi
from atlassian_jira_python_sdk.apis.tags.permission_schemes_api import PermissionSchemesApi
from atlassian_jira_python_sdk.apis.tags.project_roles_api import ProjectRolesApi
from atlassian_jira_python_sdk.apis.tags.groups_api import GroupsApi
from atlassian_jira_python_sdk.apis.tags.issue_attachments_api import IssueAttachmentsApi
from atlassian_jira_python_sdk.apis.tags.issue_custom_field_options_apps_api import IssueCustomFieldOptionsAppsApi
from atlassian_jira_python_sdk.apis.tags.issue_notification_schemes_api import IssueNotificationSchemesApi
from atlassian_jira_python_sdk.apis.tags.issue_priorities_api import IssuePrioritiesApi
from atlassian_jira_python_sdk.apis.tags.issue_properties_api import IssuePropertiesApi
from atlassian_jira_python_sdk.apis.tags.issue_resolutions_api import IssueResolutionsApi
from atlassian_jira_python_sdk.apis.tags.issue_types_api import IssueTypesApi
from atlassian_jira_python_sdk.apis.tags.issue_worklogs_api import IssueWorklogsApi
from atlassian_jira_python_sdk.apis.tags.project_components_api import ProjectComponentsApi
from atlassian_jira_python_sdk.apis.tags.user_search_api import UserSearchApi
from atlassian_jira_python_sdk.apis.tags.avatars_api import AvatarsApi
from atlassian_jira_python_sdk.apis.tags.issue_custom_field_options_api import IssueCustomFieldOptionsApi
from atlassian_jira_python_sdk.apis.tags.myself_api import MyselfApi
from atlassian_jira_python_sdk.apis.tags.screens_api import ScreensApi
from atlassian_jira_python_sdk.apis.tags.filter_sharing_api import FilterSharingApi
from atlassian_jira_python_sdk.apis.tags.issue_comments_api import IssueCommentsApi
from atlassian_jira_python_sdk.apis.tags.issue_remote_links_api import IssueRemoteLinksApi
from atlassian_jira_python_sdk.apis.tags.jql_api import JQLApi
from atlassian_jira_python_sdk.apis.tags.project_role_actors_api import ProjectRoleActorsApi
from atlassian_jira_python_sdk.apis.tags.screen_tabs_api import ScreenTabsApi
from atlassian_jira_python_sdk.apis.tags.app_properties_api import AppPropertiesApi
from atlassian_jira_python_sdk.apis.tags.issue_link_types_api import IssueLinkTypesApi
from atlassian_jira_python_sdk.apis.tags.issue_search_api import IssueSearchApi
from atlassian_jira_python_sdk.apis.tags.project_categories_api import ProjectCategoriesApi
from atlassian_jira_python_sdk.apis.tags.status_api import StatusApi
from atlassian_jira_python_sdk.apis.tags.time_tracking_api import TimeTrackingApi
from atlassian_jira_python_sdk.apis.tags.webhooks_api import WebhooksApi
from atlassian_jira_python_sdk.apis.tags.ui_modifications_apps_api import UIModificationsAppsApi
from atlassian_jira_python_sdk.apis.tags.issue_comment_properties_api import IssueCommentPropertiesApi
from atlassian_jira_python_sdk.apis.tags.issue_type_properties_api import IssueTypePropertiesApi
from atlassian_jira_python_sdk.apis.tags.issue_watchers_api import IssueWatchersApi
from atlassian_jira_python_sdk.apis.tags.issue_worklog_properties_api import IssueWorklogPropertiesApi
from atlassian_jira_python_sdk.apis.tags.jira_settings_api import JiraSettingsApi
from atlassian_jira_python_sdk.apis.tags.permissions_api import PermissionsApi
from atlassian_jira_python_sdk.apis.tags.project_avatars_api import ProjectAvatarsApi
from atlassian_jira_python_sdk.apis.tags.project_permission_schemes_api import ProjectPermissionSchemesApi
from atlassian_jira_python_sdk.apis.tags.project_properties_api import ProjectPropertiesApi
from atlassian_jira_python_sdk.apis.tags.project_types_api import ProjectTypesApi
from atlassian_jira_python_sdk.apis.tags.screen_tab_fields_api import ScreenTabFieldsApi
from atlassian_jira_python_sdk.apis.tags.screen_schemes_api import ScreenSchemesApi
from atlassian_jira_python_sdk.apis.tags.user_properties_api import UserPropertiesApi
from atlassian_jira_python_sdk.apis.tags.workflow_transition_properties_api import WorkflowTransitionPropertiesApi
from atlassian_jira_python_sdk.apis.tags.issue_links_api import IssueLinksApi
from atlassian_jira_python_sdk.apis.tags.issue_votes_api import IssueVotesApi
from atlassian_jira_python_sdk.apis.tags.license_metrics_api import LicenseMetricsApi
from atlassian_jira_python_sdk.apis.tags.project_classification_levels_api import ProjectClassificationLevelsApi
from atlassian_jira_python_sdk.apis.tags.project_key_and_name_validation_api import ProjectKeyAndNameValidationApi
from atlassian_jira_python_sdk.apis.tags.workflow_transition_rules_api import WorkflowTransitionRulesApi
from atlassian_jira_python_sdk.apis.tags.dynamic_modules_api import DynamicModulesApi
from atlassian_jira_python_sdk.apis.tags.app_migration_api import AppMigrationApi
from atlassian_jira_python_sdk.apis.tags.announcement_banner_api import AnnouncementBannerApi
from atlassian_jira_python_sdk.apis.tags.app_data_policies_eap_api import AppDataPoliciesEAPApi
from atlassian_jira_python_sdk.apis.tags.application_roles_api import ApplicationRolesApi
from atlassian_jira_python_sdk.apis.tags.issue_custom_field_values_apps_api import IssueCustomFieldValuesAppsApi
from atlassian_jira_python_sdk.apis.tags.issue_custom_field_configuration_apps_api import IssueCustomFieldConfigurationAppsApi
from atlassian_jira_python_sdk.apis.tags.issue_navigator_settings_api import IssueNavigatorSettingsApi
from atlassian_jira_python_sdk.apis.tags.issue_security_level_api import IssueSecurityLevelApi
from atlassian_jira_python_sdk.apis.tags.jira_expressions_api import JiraExpressionsApi
from atlassian_jira_python_sdk.apis.tags.jql_functions_apps_api import JQLFunctionsAppsApi
from atlassian_jira_python_sdk.apis.tags.project_email_api import ProjectEmailApi
from atlassian_jira_python_sdk.apis.tags.project_features_api import ProjectFeaturesApi
from atlassian_jira_python_sdk.apis.tags.tasks_api import TasksApi
from atlassian_jira_python_sdk.apis.tags.workflow_scheme_project_associations_api import WorkflowSchemeProjectAssociationsApi
from atlassian_jira_python_sdk.apis.tags.workflow_statuses_api import WorkflowStatusesApi
from atlassian_jira_python_sdk.apis.tags.workflow_status_categories_api import WorkflowStatusCategoriesApi
from atlassian_jira_python_sdk.apis.tags.audit_records_api import AuditRecordsApi
from atlassian_jira_python_sdk.apis.tags.classification_levels_api import ClassificationLevelsApi
from atlassian_jira_python_sdk.apis.tags.group_and_user_picker_api import GroupAndUserPickerApi
from atlassian_jira_python_sdk.apis.tags.labels_api import LabelsApi
from atlassian_jira_python_sdk.apis.tags.server_info_api import ServerInfoApi
from atlassian_jira_python_sdk.apis.tags.service_registry_api import ServiceRegistryApi
from atlassian_jira_python_sdk.apis.tags.issue_security_scheme_api import IssueSecuritySchemeApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ISSUES: IssuesApi,
        TagValues.DASHBOARDS: DashboardsApi,
        TagValues.WORKFLOW_SCHEMES: WorkflowSchemesApi,
        TagValues.ISSUE_SECURITY_SCHEMES: IssueSecuritySchemesApi,
        TagValues.ISSUE_FIELD_CONFIGURATIONS: IssueFieldConfigurationsApi,
        TagValues.PROJECT_VERSIONS: ProjectVersionsApi,
        TagValues.WORKFLOW_SCHEME_DRAFTS: WorkflowSchemeDraftsApi,
        TagValues.FILTERS: FiltersApi,
        TagValues.ISSUE_CUSTOM_FIELD_CONTEXTS: IssueCustomFieldContextsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.USERS: UsersApi,
        TagValues.ISSUE_TYPE_SCREEN_SCHEMES: IssueTypeScreenSchemesApi,
        TagValues.ISSUE_TYPE_SCHEMES: IssueTypeSchemesApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.ISSUE_FIELDS: IssueFieldsApi,
        TagValues.PERMISSION_SCHEMES: PermissionSchemesApi,
        TagValues.PROJECT_ROLES: ProjectRolesApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.ISSUE_ATTACHMENTS: IssueAttachmentsApi,
        TagValues.ISSUE_CUSTOM_FIELD_OPTIONS_APPS: IssueCustomFieldOptionsAppsApi,
        TagValues.ISSUE_NOTIFICATION_SCHEMES: IssueNotificationSchemesApi,
        TagValues.ISSUE_PRIORITIES: IssuePrioritiesApi,
        TagValues.ISSUE_PROPERTIES: IssuePropertiesApi,
        TagValues.ISSUE_RESOLUTIONS: IssueResolutionsApi,
        TagValues.ISSUE_TYPES: IssueTypesApi,
        TagValues.ISSUE_WORKLOGS: IssueWorklogsApi,
        TagValues.PROJECT_COMPONENTS: ProjectComponentsApi,
        TagValues.USER_SEARCH: UserSearchApi,
        TagValues.AVATARS: AvatarsApi,
        TagValues.ISSUE_CUSTOM_FIELD_OPTIONS: IssueCustomFieldOptionsApi,
        TagValues.MYSELF: MyselfApi,
        TagValues.SCREENS: ScreensApi,
        TagValues.FILTER_SHARING: FilterSharingApi,
        TagValues.ISSUE_COMMENTS: IssueCommentsApi,
        TagValues.ISSUE_REMOTE_LINKS: IssueRemoteLinksApi,
        TagValues.JQL: JQLApi,
        TagValues.PROJECT_ROLE_ACTORS: ProjectRoleActorsApi,
        TagValues.SCREEN_TABS: ScreenTabsApi,
        TagValues.APP_PROPERTIES: AppPropertiesApi,
        TagValues.ISSUE_LINK_TYPES: IssueLinkTypesApi,
        TagValues.ISSUE_SEARCH: IssueSearchApi,
        TagValues.PROJECT_CATEGORIES: ProjectCategoriesApi,
        TagValues.STATUS: StatusApi,
        TagValues.TIME_TRACKING: TimeTrackingApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.UI_MODIFICATIONS_APPS: UIModificationsAppsApi,
        TagValues.ISSUE_COMMENT_PROPERTIES: IssueCommentPropertiesApi,
        TagValues.ISSUE_TYPE_PROPERTIES: IssueTypePropertiesApi,
        TagValues.ISSUE_WATCHERS: IssueWatchersApi,
        TagValues.ISSUE_WORKLOG_PROPERTIES: IssueWorklogPropertiesApi,
        TagValues.JIRA_SETTINGS: JiraSettingsApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.PROJECT_AVATARS: ProjectAvatarsApi,
        TagValues.PROJECT_PERMISSION_SCHEMES: ProjectPermissionSchemesApi,
        TagValues.PROJECT_PROPERTIES: ProjectPropertiesApi,
        TagValues.PROJECT_TYPES: ProjectTypesApi,
        TagValues.SCREEN_TAB_FIELDS: ScreenTabFieldsApi,
        TagValues.SCREEN_SCHEMES: ScreenSchemesApi,
        TagValues.USER_PROPERTIES: UserPropertiesApi,
        TagValues.WORKFLOW_TRANSITION_PROPERTIES: WorkflowTransitionPropertiesApi,
        TagValues.ISSUE_LINKS: IssueLinksApi,
        TagValues.ISSUE_VOTES: IssueVotesApi,
        TagValues.LICENSE_METRICS: LicenseMetricsApi,
        TagValues.PROJECT_CLASSIFICATION_LEVELS: ProjectClassificationLevelsApi,
        TagValues.PROJECT_KEY_AND_NAME_VALIDATION: ProjectKeyAndNameValidationApi,
        TagValues.WORKFLOW_TRANSITION_RULES: WorkflowTransitionRulesApi,
        TagValues.DYNAMIC_MODULES: DynamicModulesApi,
        TagValues.APP_MIGRATION: AppMigrationApi,
        TagValues.ANNOUNCEMENT_BANNER: AnnouncementBannerApi,
        TagValues.APP_DATA_POLICIES_EAP: AppDataPoliciesEAPApi,
        TagValues.APPLICATION_ROLES: ApplicationRolesApi,
        TagValues.ISSUE_CUSTOM_FIELD_VALUES_APPS: IssueCustomFieldValuesAppsApi,
        TagValues.ISSUE_CUSTOM_FIELD_CONFIGURATION_APPS: IssueCustomFieldConfigurationAppsApi,
        TagValues.ISSUE_NAVIGATOR_SETTINGS: IssueNavigatorSettingsApi,
        TagValues.ISSUE_SECURITY_LEVEL: IssueSecurityLevelApi,
        TagValues.JIRA_EXPRESSIONS: JiraExpressionsApi,
        TagValues.JQL_FUNCTIONS_APPS: JQLFunctionsAppsApi,
        TagValues.PROJECT_EMAIL: ProjectEmailApi,
        TagValues.PROJECT_FEATURES: ProjectFeaturesApi,
        TagValues.TASKS: TasksApi,
        TagValues.WORKFLOW_SCHEME_PROJECT_ASSOCIATIONS: WorkflowSchemeProjectAssociationsApi,
        TagValues.WORKFLOW_STATUSES: WorkflowStatusesApi,
        TagValues.WORKFLOW_STATUS_CATEGORIES: WorkflowStatusCategoriesApi,
        TagValues.AUDIT_RECORDS: AuditRecordsApi,
        TagValues.CLASSIFICATION_LEVELS: ClassificationLevelsApi,
        TagValues.GROUP_AND_USER_PICKER: GroupAndUserPickerApi,
        TagValues.LABELS: LabelsApi,
        TagValues.SERVER_INFO: ServerInfoApi,
        TagValues.SERVICE_REGISTRY: ServiceRegistryApi,
        TagValues.ISSUE_SECURITY_SCHEME: IssueSecuritySchemeApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ISSUES: IssuesApi,
        TagValues.DASHBOARDS: DashboardsApi,
        TagValues.WORKFLOW_SCHEMES: WorkflowSchemesApi,
        TagValues.ISSUE_SECURITY_SCHEMES: IssueSecuritySchemesApi,
        TagValues.ISSUE_FIELD_CONFIGURATIONS: IssueFieldConfigurationsApi,
        TagValues.PROJECT_VERSIONS: ProjectVersionsApi,
        TagValues.WORKFLOW_SCHEME_DRAFTS: WorkflowSchemeDraftsApi,
        TagValues.FILTERS: FiltersApi,
        TagValues.ISSUE_CUSTOM_FIELD_CONTEXTS: IssueCustomFieldContextsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.USERS: UsersApi,
        TagValues.ISSUE_TYPE_SCREEN_SCHEMES: IssueTypeScreenSchemesApi,
        TagValues.ISSUE_TYPE_SCHEMES: IssueTypeSchemesApi,
        TagValues.WORKFLOWS: WorkflowsApi,
        TagValues.ISSUE_FIELDS: IssueFieldsApi,
        TagValues.PERMISSION_SCHEMES: PermissionSchemesApi,
        TagValues.PROJECT_ROLES: ProjectRolesApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.ISSUE_ATTACHMENTS: IssueAttachmentsApi,
        TagValues.ISSUE_CUSTOM_FIELD_OPTIONS_APPS: IssueCustomFieldOptionsAppsApi,
        TagValues.ISSUE_NOTIFICATION_SCHEMES: IssueNotificationSchemesApi,
        TagValues.ISSUE_PRIORITIES: IssuePrioritiesApi,
        TagValues.ISSUE_PROPERTIES: IssuePropertiesApi,
        TagValues.ISSUE_RESOLUTIONS: IssueResolutionsApi,
        TagValues.ISSUE_TYPES: IssueTypesApi,
        TagValues.ISSUE_WORKLOGS: IssueWorklogsApi,
        TagValues.PROJECT_COMPONENTS: ProjectComponentsApi,
        TagValues.USER_SEARCH: UserSearchApi,
        TagValues.AVATARS: AvatarsApi,
        TagValues.ISSUE_CUSTOM_FIELD_OPTIONS: IssueCustomFieldOptionsApi,
        TagValues.MYSELF: MyselfApi,
        TagValues.SCREENS: ScreensApi,
        TagValues.FILTER_SHARING: FilterSharingApi,
        TagValues.ISSUE_COMMENTS: IssueCommentsApi,
        TagValues.ISSUE_REMOTE_LINKS: IssueRemoteLinksApi,
        TagValues.JQL: JQLApi,
        TagValues.PROJECT_ROLE_ACTORS: ProjectRoleActorsApi,
        TagValues.SCREEN_TABS: ScreenTabsApi,
        TagValues.APP_PROPERTIES: AppPropertiesApi,
        TagValues.ISSUE_LINK_TYPES: IssueLinkTypesApi,
        TagValues.ISSUE_SEARCH: IssueSearchApi,
        TagValues.PROJECT_CATEGORIES: ProjectCategoriesApi,
        TagValues.STATUS: StatusApi,
        TagValues.TIME_TRACKING: TimeTrackingApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.UI_MODIFICATIONS_APPS: UIModificationsAppsApi,
        TagValues.ISSUE_COMMENT_PROPERTIES: IssueCommentPropertiesApi,
        TagValues.ISSUE_TYPE_PROPERTIES: IssueTypePropertiesApi,
        TagValues.ISSUE_WATCHERS: IssueWatchersApi,
        TagValues.ISSUE_WORKLOG_PROPERTIES: IssueWorklogPropertiesApi,
        TagValues.JIRA_SETTINGS: JiraSettingsApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.PROJECT_AVATARS: ProjectAvatarsApi,
        TagValues.PROJECT_PERMISSION_SCHEMES: ProjectPermissionSchemesApi,
        TagValues.PROJECT_PROPERTIES: ProjectPropertiesApi,
        TagValues.PROJECT_TYPES: ProjectTypesApi,
        TagValues.SCREEN_TAB_FIELDS: ScreenTabFieldsApi,
        TagValues.SCREEN_SCHEMES: ScreenSchemesApi,
        TagValues.USER_PROPERTIES: UserPropertiesApi,
        TagValues.WORKFLOW_TRANSITION_PROPERTIES: WorkflowTransitionPropertiesApi,
        TagValues.ISSUE_LINKS: IssueLinksApi,
        TagValues.ISSUE_VOTES: IssueVotesApi,
        TagValues.LICENSE_METRICS: LicenseMetricsApi,
        TagValues.PROJECT_CLASSIFICATION_LEVELS: ProjectClassificationLevelsApi,
        TagValues.PROJECT_KEY_AND_NAME_VALIDATION: ProjectKeyAndNameValidationApi,
        TagValues.WORKFLOW_TRANSITION_RULES: WorkflowTransitionRulesApi,
        TagValues.DYNAMIC_MODULES: DynamicModulesApi,
        TagValues.APP_MIGRATION: AppMigrationApi,
        TagValues.ANNOUNCEMENT_BANNER: AnnouncementBannerApi,
        TagValues.APP_DATA_POLICIES_EAP: AppDataPoliciesEAPApi,
        TagValues.APPLICATION_ROLES: ApplicationRolesApi,
        TagValues.ISSUE_CUSTOM_FIELD_VALUES_APPS: IssueCustomFieldValuesAppsApi,
        TagValues.ISSUE_CUSTOM_FIELD_CONFIGURATION_APPS: IssueCustomFieldConfigurationAppsApi,
        TagValues.ISSUE_NAVIGATOR_SETTINGS: IssueNavigatorSettingsApi,
        TagValues.ISSUE_SECURITY_LEVEL: IssueSecurityLevelApi,
        TagValues.JIRA_EXPRESSIONS: JiraExpressionsApi,
        TagValues.JQL_FUNCTIONS_APPS: JQLFunctionsAppsApi,
        TagValues.PROJECT_EMAIL: ProjectEmailApi,
        TagValues.PROJECT_FEATURES: ProjectFeaturesApi,
        TagValues.TASKS: TasksApi,
        TagValues.WORKFLOW_SCHEME_PROJECT_ASSOCIATIONS: WorkflowSchemeProjectAssociationsApi,
        TagValues.WORKFLOW_STATUSES: WorkflowStatusesApi,
        TagValues.WORKFLOW_STATUS_CATEGORIES: WorkflowStatusCategoriesApi,
        TagValues.AUDIT_RECORDS: AuditRecordsApi,
        TagValues.CLASSIFICATION_LEVELS: ClassificationLevelsApi,
        TagValues.GROUP_AND_USER_PICKER: GroupAndUserPickerApi,
        TagValues.LABELS: LabelsApi,
        TagValues.SERVER_INFO: ServerInfoApi,
        TagValues.SERVICE_REGISTRY: ServiceRegistryApi,
        TagValues.ISSUE_SECURITY_SCHEME: IssueSecuritySchemeApi,
    }
)
