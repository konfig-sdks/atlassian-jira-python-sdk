operation_parameter_map = {
    '/rest/api/3/announcementBanner-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/announcementBanner-PUT': {
        'parameters': [
            {
                'name': 'isDismissible'
            },
            {
                'name': 'isEnabled'
            },
            {
                'name': 'message'
            },
            {
                'name': 'visibility'
            },
        ]
    },
    '/rest/api/3/data-policy/project-GET': {
        'parameters': [
            {
                'name': 'ids'
            },
        ]
    },
    '/rest/api/3/data-policy-GET': {
        'parameters': [
        ]
    },
    '/rest/atlassian-connect/1/migration/properties/{entityType}-PUT': {
        'parameters': [
            {
                'name': 'Atlassian-Transfer-Id'
            },
            {
                'name': 'entityType'
            },
        ]
    },
    '/rest/atlassian-connect/1/migration/field-PUT': {
        'parameters': [
            {
                'name': 'Atlassian-Transfer-Id'
            },
            {
                'name': 'updateValueList'
            },
        ]
    },
    '/rest/atlassian-connect/1/migration/workflow/rule/search-POST': {
        'parameters': [
            {
                'name': 'ruleIds'
            },
            {
                'name': 'workflowEntityId'
            },
            {
                'name': 'Atlassian-Transfer-Id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/forge/1/app/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'addonKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/atlassian-connect/1/addons/{addonKey}/properties-GET': {
        'parameters': [
            {
                'name': 'addonKey'
            },
        ]
    },
    '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}-GET': {
        'parameters': [
            {
                'name': 'addonKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'addonKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/forge/1/app/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/applicationrole-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/applicationrole/{key}-GET': {
        'parameters': [
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/auditing/record-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}-DELETE': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'owningObjectId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'id'
            },
            {
                'name': 'size'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'size'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/rest/api/3/universal_avatar/view/type/{type}-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'size'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/rest/api/3/universal_avatar/type/{type}/owner/{entityId}-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'entityId'
            },
        ]
    },
    '/rest/api/3/avatar/{type}/system-GET': {
        'parameters': [
            {
                'name': 'type'
            },
        ]
    },
    '/rest/api/3/universal_avatar/type/{type}/owner/{entityId}-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'size'
            },
            {
                'name': 'x'
            },
            {
                'name': 'y'
            },
        ]
    },
    '/rest/api/3/classification-levels-GET': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/rest/api/3/dashboard/{dashboardId}/gadget-POST': {
        'parameters': [
            {
                'name': 'dashboardId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'color'
            },
            {
                'name': 'ignoreUriAndModuleKeyValidation'
            },
            {
                'name': 'moduleKey'
            },
            {
                'name': 'position'
            },
            {
                'name': 'uri'
            },
        ]
    },
    '/rest/api/3/dashboard/{id}/copy-POST': {
        'parameters': [
            {
                'name': 'editPermissions'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sharePermissions'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/dashboard-POST': {
        'parameters': [
            {
                'name': 'editPermissions'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sharePermissions'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'dashboardId'
            },
            {
                'name': 'itemId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/dashboard/bulk/edit-PUT': {
        'parameters': [
            {
                'name': 'action'
            },
            {
                'name': 'entityIds'
            },
            {
                'name': 'changeOwnerDetails'
            },
            {
                'name': 'extendAdminPermissions'
            },
            {
                'name': 'permissionDetails'
            },
        ]
    },
    '/rest/api/3/dashboard-GET': {
        'parameters': [
            {
                'name': 'filter'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/dashboard/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties-GET': {
        'parameters': [
            {
                'name': 'dashboardId'
            },
            {
                'name': 'itemId'
            },
        ]
    },
    '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}-GET': {
        'parameters': [
            {
                'name': 'dashboardId'
            },
            {
                'name': 'itemId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/dashboard/gadgets-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/dashboard/{dashboardId}/gadget-GET': {
        'parameters': [
            {
                'name': 'dashboardId'
            },
            {
                'name': 'moduleKey'
            },
            {
                'name': 'uri'
            },
            {
                'name': 'gadgetId'
            },
        ]
    },
    '/rest/api/3/dashboard/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}-DELETE': {
        'parameters': [
            {
                'name': 'dashboardId'
            },
            {
                'name': 'gadgetId'
            },
        ]
    },
    '/rest/api/3/dashboard/search-GET': {
        'parameters': [
            {
                'name': 'dashboardName'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'owner'
            },
            {
                'name': 'groupname'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'status'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'dashboardId'
            },
            {
                'name': 'itemId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/dashboard/{id}-PUT': {
        'parameters': [
            {
                'name': 'editPermissions'
            },
            {
                'name': 'name'
            },
            {
                'name': 'sharePermissions'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}-PUT': {
        'parameters': [
            {
                'name': 'dashboardId'
            },
            {
                'name': 'gadgetId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'color'
            },
            {
                'name': 'position'
            },
        ]
    },
    '/rest/atlassian-connect/1/app/module/dynamic-GET': {
        'parameters': [
        ]
    },
    '/rest/atlassian-connect/1/app/module/dynamic-POST': {
        'parameters': [
            {
                'name': 'modules'
            },
        ]
    },
    '/rest/atlassian-connect/1/app/module/dynamic-DELETE': {
        'parameters': [
            {
                'name': 'moduleKey'
            },
        ]
    },
    '/rest/api/3/filter/{id}/permission-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'id'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'groupname'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'projectRoleId'
            },
            {
                'name': 'rights'
            },
        ]
    },
    '/rest/api/3/filter/{id}/permission/{permissionId}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'permissionId'
            },
        ]
    },
    '/rest/api/3/filter/defaultShareScope-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/filter/{id}/permission/{permissionId}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'permissionId'
            },
        ]
    },
    '/rest/api/3/filter/{id}/permission-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/filter/defaultShareScope-PUT': {
        'parameters': [
            {
                'name': 'scope'
            },
        ]
    },
    '/rest/api/3/filter/{id}/favourite-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/filter/{id}/owner-PUT': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/filter-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'approximateLastUsed'
            },
            {
                'name': 'editPermissions'
            },
            {
                'name': 'favourite'
            },
            {
                'name': 'favouritedCount'
            },
            {
                'name': 'id'
            },
            {
                'name': 'jql'
            },
            {
                'name': 'owner'
            },
            {
                'name': 'searchUrl'
            },
            {
                'name': 'self'
            },
            {
                'name': 'sharePermissions'
            },
            {
                'name': 'sharedUsers'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'viewUrl'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'overrideSharePermissions'
            },
        ]
    },
    '/rest/api/3/filter/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/filter/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'overrideSharePermissions'
            },
        ]
    },
    '/rest/api/3/filter/{id}/columns-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/filter/my-GET': {
        'parameters': [
            {
                'name': 'expand'
            },
            {
                'name': 'includeFavourites'
            },
        ]
    },
    '/rest/api/3/filter/favourite-GET': {
        'parameters': [
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/filter/{id}/favourite-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/filter/{id}/columns-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/filter/search-GET': {
        'parameters': [
            {
                'name': 'filterName'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'owner'
            },
            {
                'name': 'groupname'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'overrideSharePermissions'
            },
        ]
    },
    '/rest/api/3/filter/{id}/columns-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'columns'
            },
        ]
    },
    '/rest/api/3/filter/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'approximateLastUsed'
            },
            {
                'name': 'editPermissions'
            },
            {
                'name': 'favourite'
            },
            {
                'name': 'favouritedCount'
            },
            {
                'name': 'id'
            },
            {
                'name': 'jql'
            },
            {
                'name': 'owner'
            },
            {
                'name': 'searchUrl'
            },
            {
                'name': 'self'
            },
            {
                'name': 'sharePermissions'
            },
            {
                'name': 'sharedUsers'
            },
            {
                'name': 'subscriptions'
            },
            {
                'name': 'viewUrl'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'overrideSharePermissions'
            },
        ]
    },
    '/rest/api/3/groupuserpicker-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'showAvatar'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'issueTypeId'
            },
            {
                'name': 'avatarSize'
            },
            {
                'name': 'caseInsensitive'
            },
            {
                'name': 'excludeConnectAddons'
            },
        ]
    },
    '/rest/api/3/group/user-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'groupname'
            },
            {
                'name': 'groupId'
            },
        ]
    },
    '/rest/api/3/group-POST': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/groups/picker-GET': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'query'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'excludeId'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'caseInsensitive'
            },
            {
                'name': 'userName'
            },
        ]
    },
    '/rest/api/3/group-GET': {
        'parameters': [
            {
                'name': 'groupname'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/group/member-GET': {
        'parameters': [
            {
                'name': 'groupname'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'includeInactiveUsers'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/group/bulk-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'groupName'
            },
            {
                'name': 'accessType'
            },
            {
                'name': 'applicationKey'
            },
        ]
    },
    '/rest/api/3/group-DELETE': {
        'parameters': [
            {
                'name': 'groupname'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'swapGroup'
            },
            {
                'name': 'swapGroupId'
            },
        ]
    },
    '/rest/api/3/group/user-DELETE': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'groupname'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/attachments-POST': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
        ]
    },
    '/rest/api/3/attachment/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/attachment/{id}/expand/human-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/attachment/{id}/expand/raw-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/attachment/content/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'redirect'
            },
        ]
    },
    '/rest/api/3/attachment/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/attachment/meta-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/attachment/thumbnail/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'redirect'
            },
            {
                'name': 'fallbackToDefault'
            },
            {
                'name': 'width'
            },
            {
                'name': 'height'
            },
        ]
    },
    '/rest/api/3/comment/{commentId}/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'commentId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/comment/{commentId}/properties-GET': {
        'parameters': [
            {
                'name': 'commentId'
            },
        ]
    },
    '/rest/api/3/comment/{commentId}/properties/{propertyKey}-GET': {
        'parameters': [
            {
                'name': 'commentId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/comment/{commentId}/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'commentId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/comment-POST': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'author'
            },
            {
                'name': 'body'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'jsdAuthorCanSeeRequest'
            },
            {
                'name': 'jsdPublic'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'renderedBody'
            },
            {
                'name': 'self'
            },
            {
                'name': 'updateAuthor'
            },
            {
                'name': 'updated'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/comment/{id}-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/comment/{id}-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/comment/list-POST': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/comment-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/comment/{id}-PUT': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'author'
            },
            {
                'name': 'body'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'jsdAuthorCanSeeRequest'
            },
            {
                'name': 'jsdPublic'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'renderedBody'
            },
            {
                'name': 'self'
            },
            {
                'name': 'updateAuthor'
            },
            {
                'name': 'updated'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'notifyUsers'
            },
            {
                'name': 'overrideEditableFlag'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/app/field/{fieldIdOrKey}/context/configuration-GET': {
        'parameters': [
            {
                'name': 'fieldIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'fieldContextId'
            },
            {
                'name': 'issueId'
            },
            {
                'name': 'projectKeyOrId'
            },
            {
                'name': 'issueTypeId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/app/field/{fieldIdOrKey}/context/configuration-PUT': {
        'parameters': [
            {
                'name': 'configurations'
            },
            {
                'name': 'fieldIdOrKey'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/issuetype-PUT': {
        'parameters': [
            {
                'name': 'issueTypeIds'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/project-PUT': {
        'parameters': [
            {
                'name': 'projectIds'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issueTypeIds'
            },
            {
                'name': 'projectIds'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}-DELETE': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/mapping-POST': {
        'parameters': [
            {
                'name': 'mappings'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/defaultValue-GET': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/issuetypemapping-GET': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/projectmapping-GET': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context-GET': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'isAnyIssueType'
            },
            {
                'name': 'isGlobalContext'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/project/remove-POST': {
        'parameters': [
            {
                'name': 'projectIds'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove-POST': {
        'parameters': [
            {
                'name': 'issueTypeIds'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/defaultValue-PUT': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'defaultValues'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}-PUT': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/option-POST': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}-DELETE': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'optionId'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/option-GET': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'optionId'
            },
            {
                'name': 'onlyOptions'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/customFieldOption/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/option/move-PUT': {
        'parameters': [
            {
                'name': 'customFieldOptionIds'
            },
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'position'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue-DELETE': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'optionId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'replaceWith'
            },
            {
                'name': 'jql'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/context/{contextId}/option-PUT': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'contextId'
            },
            {
                'name': 'options'
            },
        ]
    },
    '/rest/api/3/field/{fieldKey}/option-POST': {
        'parameters': [
            {
                'name': 'value'
            },
            {
                'name': 'fieldKey'
            },
            {
                'name': 'config'
            },
            {
                'name': 'properties'
            },
        ]
    },
    '/rest/api/3/field/{fieldKey}/option/{optionId}-DELETE': {
        'parameters': [
            {
                'name': 'fieldKey'
            },
            {
                'name': 'optionId'
            },
        ]
    },
    '/rest/api/3/field/{fieldKey}/option/{optionId}/issue-DELETE': {
        'parameters': [
            {
                'name': 'fieldKey'
            },
            {
                'name': 'optionId'
            },
            {
                'name': 'replaceWith'
            },
            {
                'name': 'jql'
            },
            {
                'name': 'overrideScreenSecurity'
            },
            {
                'name': 'overrideEditableFlag'
            },
        ]
    },
    '/rest/api/3/field/{fieldKey}/option-GET': {
        'parameters': [
            {
                'name': 'fieldKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/field/{fieldKey}/option/{optionId}-GET': {
        'parameters': [
            {
                'name': 'fieldKey'
            },
            {
                'name': 'optionId'
            },
        ]
    },
    '/rest/api/3/field/{fieldKey}/option/suggestions/edit-GET': {
        'parameters': [
            {
                'name': 'fieldKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/field/{fieldKey}/option/suggestions/search-GET': {
        'parameters': [
            {
                'name': 'fieldKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/field/{fieldKey}/option/{optionId}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'value'
            },
            {
                'name': 'fieldKey'
            },
            {
                'name': 'optionId'
            },
            {
                'name': 'config'
            },
            {
                'name': 'properties'
            },
        ]
    },
    '/rest/api/3/app/field/{fieldIdOrKey}/value-PUT': {
        'parameters': [
            {
                'name': 'fieldIdOrKey'
            },
            {
                'name': 'updates'
            },
            {
                'name': 'generateChangelog'
            },
        ]
    },
    '/rest/api/3/app/field/value-POST': {
        'parameters': [
            {
                'name': 'updates'
            },
            {
                'name': 'generateChangelog'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme/project-PUT': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'fieldConfigurationSchemeId'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme/{id}/mapping-PUT': {
        'parameters': [
            {
                'name': 'mappings'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/fieldconfiguration-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/fieldconfiguration/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/fieldconfiguration-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'isDefault'
            },
            {
                'name': 'query'
            },
        ]
    },
    '/rest/api/3/fieldconfiguration/{id}/fields-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme/mapping-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'fieldConfigurationSchemeId'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme/project-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme/{id}/mapping/delete-POST': {
        'parameters': [
            {
                'name': 'issueTypeIds'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/fieldconfiguration/{id}/fields-PUT': {
        'parameters': [
            {
                'name': 'fieldConfigurationItems'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/fieldconfiguration/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/fieldconfigurationscheme/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/field-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'type'
            },
            {
                'name': 'description'
            },
            {
                'name': 'searcherKey'
            },
        ]
    },
    '/rest/api/3/field/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/contexts-GET': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/field/search-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'type'
            },
            {
                'name': 'id'
            },
            {
                'name': 'query'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/field-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/field/search/trashed-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'query'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/rest/api/3/field/{id}/trash-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/field/{id}/restore-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}-PUT': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'searcherKey'
            },
        ]
    },
    '/rest/api/3/issueLinkType-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'inward'
            },
            {
                'name': 'name'
            },
            {
                'name': 'outward'
            },
            {
                'name': 'self'
            },
        ]
    },
    '/rest/api/3/issueLinkType/{issueLinkTypeId}-DELETE': {
        'parameters': [
            {
                'name': 'issueLinkTypeId'
            },
        ]
    },
    '/rest/api/3/issueLinkType-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/issueLinkType/{issueLinkTypeId}-GET': {
        'parameters': [
            {
                'name': 'issueLinkTypeId'
            },
        ]
    },
    '/rest/api/3/issueLinkType/{issueLinkTypeId}-PUT': {
        'parameters': [
            {
                'name': 'issueLinkTypeId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'inward'
            },
            {
                'name': 'name'
            },
            {
                'name': 'outward'
            },
            {
                'name': 'self'
            },
        ]
    },
    '/rest/api/3/issueLink-POST': {
        'parameters': [
            {
                'name': 'inwardIssue'
            },
            {
                'name': 'outwardIssue'
            },
            {
                'name': 'type'
            },
            {
                'name': 'comment'
            },
        ]
    },
    '/rest/api/3/issueLink/{linkId}-DELETE': {
        'parameters': [
            {
                'name': 'linkId'
            },
        ]
    },
    '/rest/api/3/issueLink/{linkId}-GET': {
        'parameters': [
            {
                'name': 'linkId'
            },
        ]
    },
    '/rest/api/3/settings/columns-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/settings/columns-PUT': {
        'parameters': [
            {
                'name': 'columns'
            },
        ]
    },
    '/rest/api/3/notificationscheme/{id}/notification-PUT': {
        'parameters': [
            {
                'name': 'notificationSchemeEvents'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/notificationscheme-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'notificationSchemeEvents'
            },
        ]
    },
    '/rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}-DELETE': {
        'parameters': [
            {
                'name': 'notificationSchemeId'
            },
            {
                'name': 'notificationId'
            },
        ]
    },
    '/rest/api/3/notificationscheme/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/notificationscheme/project-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'notificationSchemeId'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/notificationscheme-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'onlyDefault'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/notificationscheme/{notificationSchemeId}-DELETE': {
        'parameters': [
            {
                'name': 'notificationSchemeId'
            },
        ]
    },
    '/rest/api/3/notificationscheme/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/priority/move-PUT': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'after'
            },
            {
                'name': 'position'
            },
        ]
    },
    '/rest/api/3/priority-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'statusColor'
            },
            {
                'name': 'description'
            },
            {
                'name': 'iconUrl'
            },
        ]
    },
    '/rest/api/3/priority/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'replaceWith'
            },
        ]
    },
    '/rest/api/3/priority/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/priority-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/priority/search-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'priorityName'
            },
            {
                'name': 'onlyDefault'
            },
        ]
    },
    '/rest/api/3/priority/default-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/priority/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'iconUrl'
            },
            {
                'name': 'name'
            },
            {
                'name': 'statusColor'
            },
        ]
    },
    '/rest/api/3/issue/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'propertyKey'
            },
            {
                'name': 'currentValue'
            },
            {
                'name': 'entityIds'
            },
        ]
    },
    '/rest/api/3/issue/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'propertyKey'
            },
            {
                'name': 'expression'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/rest/api/3/issue/properties/multi-POST': {
        'parameters': [
            {
                'name': 'issues'
            },
        ]
    },
    '/rest/api/3/issue/properties-POST': {
        'parameters': [
            {
                'name': 'entitiesIds'
            },
            {
                'name': 'properties'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/properties-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/remotelink-POST': {
        'parameters': [
            {
                'name': 'object'
            },
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'application'
            },
            {
                'name': 'globalId'
            },
            {
                'name': 'relationship'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/remotelink-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'globalId'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'linkId'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/remotelink-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'globalId'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'linkId'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}-PUT': {
        'parameters': [
            {
                'name': 'object'
            },
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'linkId'
            },
            {
                'name': 'application'
            },
            {
                'name': 'globalId'
            },
            {
                'name': 'relationship'
            },
        ]
    },
    '/rest/api/3/resolution/move-PUT': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'after'
            },
            {
                'name': 'position'
            },
        ]
    },
    '/rest/api/3/resolution-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/resolution/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'replaceWith'
            },
        ]
    },
    '/rest/api/3/resolution/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/resolution-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/resolution/search-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'onlyDefault'
            },
        ]
    },
    '/rest/api/3/resolution/default-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/resolution/{id}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/jql/match-POST': {
        'parameters': [
            {
                'name': 'issueIds'
            },
            {
                'name': 'jqls'
            },
        ]
    },
    '/rest/api/3/search-GET': {
        'parameters': [
            {
                'name': 'jql'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'validateQuery'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'fieldsByKeys'
            },
        ]
    },
    '/rest/api/3/issue/picker-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'currentJQL'
            },
            {
                'name': 'currentIssueKey'
            },
            {
                'name': 'currentProjectId'
            },
            {
                'name': 'showSubTasks'
            },
            {
                'name': 'showSubTaskParent'
            },
        ]
    },
    '/rest/api/3/search/id-POST': {
        'parameters': [
            {
                'name': 'jql'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'nextPageToken'
            },
        ]
    },
    '/rest/api/3/search-POST': {
        'parameters': [
            {
                'name': 'expand'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'fieldsByKeys'
            },
            {
                'name': 'jql'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'validateQuery'
            },
        ]
    },
    '/rest/api/3/securitylevel/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members-GET': {
        'parameters': [
            {
                'name': 'issueSecuritySchemeId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'issueSecurityLevelId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member-PUT': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'levelId'
            },
            {
                'name': 'members'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/{schemeId}/level-PUT': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'levels'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/project-PUT': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'schemeId'
            },
            {
                'name': 'oldToNewSecurityLevelMappings'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'levels'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/{schemeId}-DELETE': {
        'parameters': [
            {
                'name': 'schemeId'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/level/member-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'schemeId'
            },
            {
                'name': 'levelId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/project-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'issueSecuritySchemeId'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/level-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'schemeId'
            },
            {
                'name': 'onlyDefault'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}-DELETE': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'levelId'
            },
            {
                'name': 'replaceWith'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}-DELETE': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'levelId'
            },
            {
                'name': 'memberId'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/search-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/level/default-PUT': {
        'parameters': [
            {
                'name': 'defaultValues'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}-PUT': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'levelId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/issuesecurityschemes/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'issueTypeId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}-GET': {
        'parameters': [
            {
                'name': 'issueTypeId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issuetype/{issueTypeId}/properties-GET': {
        'parameters': [
            {
                'name': 'issueTypeId'
            },
        ]
    },
    '/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'issueTypeId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype-PUT': {
        'parameters': [
            {
                'name': 'issueTypeIds'
            },
            {
                'name': 'issueTypeSchemeId'
            },
        ]
    },
    '/rest/api/3/issuetypescheme/project-PUT': {
        'parameters': [
            {
                'name': 'issueTypeSchemeId'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move-PUT': {
        'parameters': [
            {
                'name': 'issueTypeIds'
            },
            {
                'name': 'issueTypeSchemeId'
            },
            {
                'name': 'after'
            },
            {
                'name': 'position'
            },
        ]
    },
    '/rest/api/3/issuetypescheme-POST': {
        'parameters': [
            {
                'name': 'issueTypeIds'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'defaultIssueTypeId'
            },
        ]
    },
    '/rest/api/3/issuetypescheme/{issueTypeSchemeId}-DELETE': {
        'parameters': [
            {
                'name': 'issueTypeSchemeId'
            },
        ]
    },
    '/rest/api/3/issuetypescheme-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'queryString'
            },
        ]
    },
    '/rest/api/3/issuetypescheme/project-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/issuetypescheme/mapping-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'issueTypeSchemeId'
            },
        ]
    },
    '/rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}-DELETE': {
        'parameters': [
            {
                'name': 'issueTypeSchemeId'
            },
            {
                'name': 'issueTypeId'
            },
        ]
    },
    '/rest/api/3/issuetypescheme/{issueTypeSchemeId}-PUT': {
        'parameters': [
            {
                'name': 'issueTypeSchemeId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'defaultIssueTypeId'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping-PUT': {
        'parameters': [
            {
                'name': 'issueTypeMappings'
            },
            {
                'name': 'issueTypeScreenSchemeId'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/project-PUT': {
        'parameters': [
            {
                'name': 'issueTypeScreenSchemeId'
            },
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme-POST': {
        'parameters': [
            {
                'name': 'issueTypeMappings'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}-DELETE': {
        'parameters': [
            {
                'name': 'issueTypeScreenSchemeId'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project-GET': {
        'parameters': [
            {
                'name': 'issueTypeScreenSchemeId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'query'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/project-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/mapping-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'issueTypeScreenSchemeId'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'queryString'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove-POST': {
        'parameters': [
            {
                'name': 'issueTypeIds'
            },
            {
                'name': 'issueTypeScreenSchemeId'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default-PUT': {
        'parameters': [
            {
                'name': 'screenSchemeId'
            },
            {
                'name': 'issueTypeScreenSchemeId'
            },
        ]
    },
    '/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}-PUT': {
        'parameters': [
            {
                'name': 'issueTypeScreenSchemeId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/issuetype-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'hierarchyLevel'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/rest/api/3/issuetype/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'alternativeIssueTypeId'
            },
        ]
    },
    '/rest/api/3/issuetype-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/issuetype/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/issuetype/project-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'level'
            },
        ]
    },
    '/rest/api/3/issuetype/{id}/alternatives-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/issuetype/{id}/avatar2-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'size'
            },
            {
                'name': 'x'
            },
            {
                'name': 'y'
            },
        ]
    },
    '/rest/api/3/issuetype/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'avatarId'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/votes-POST': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/votes-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/votes-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/watchers-POST': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
        ]
    },
    '/rest/api/3/issue/watching-POST': {
        'parameters': [
            {
                'name': 'issueIds'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/watchers-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/watchers-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'username'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'worklogId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'worklogId'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'worklogId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'worklogId'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog-POST': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'author'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issueId'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'self'
            },
            {
                'name': 'started'
            },
            {
                'name': 'timeSpent'
            },
            {
                'name': 'timeSpentSeconds'
            },
            {
                'name': 'updateAuthor'
            },
            {
                'name': 'updated'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'notifyUsers'
            },
            {
                'name': 'adjustEstimate'
            },
            {
                'name': 'newEstimate'
            },
            {
                'name': 'reduceBy'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'overrideEditableFlag'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'notifyUsers'
            },
            {
                'name': 'adjustEstimate'
            },
            {
                'name': 'newEstimate'
            },
            {
                'name': 'increaseBy'
            },
            {
                'name': 'overrideEditableFlag'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'startedAfter'
            },
            {
                'name': 'startedBefore'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/worklog/updated-GET': {
        'parameters': [
            {
                'name': 'since'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/worklog/list-POST': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/worklog/deleted-GET': {
        'parameters': [
            {
                'name': 'since'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/worklog/{id}-PUT': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'author'
            },
            {
                'name': 'comment'
            },
            {
                'name': 'created'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issueId'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'self'
            },
            {
                'name': 'started'
            },
            {
                'name': 'timeSpent'
            },
            {
                'name': 'timeSpentSeconds'
            },
            {
                'name': 'updateAuthor'
            },
            {
                'name': 'updated'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'notifyUsers'
            },
            {
                'name': 'adjustEstimate'
            },
            {
                'name': 'newEstimate'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'overrideEditableFlag'
            },
        ]
    },
    '/rest/api/3/issue/archive-PUT': {
        'parameters': [
            {
                'name': 'issueIdsOrKeys'
            },
        ]
    },
    '/rest/api/3/issue/archive-POST': {
        'parameters': [
            {
                'name': 'jql'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/assignee-PUT': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'accountType'
            },
            {
                'name': 'active'
            },
            {
                'name': 'applicationRoles'
            },
            {
                'name': 'avatarUrls'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'emailAddress'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'groups'
            },
            {
                'name': 'key'
            },
            {
                'name': 'locale'
            },
            {
                'name': 'name'
            },
            {
                'name': 'self'
            },
            {
                'name': 'timeZone'
            },
        ]
    },
    '/rest/api/3/issue/bulk-POST': {
        'parameters': [
            {
                'name': 'issueUpdates'
            },
        ]
    },
    '/rest/api/3/issue-POST': {
        'parameters': [
            {
                'name': 'fields'
            },
            {
                'name': 'historyMetadata'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'transition'
            },
            {
                'name': 'update'
            },
            {
                'name': 'updateHistory'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}-DELETE': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'deleteSubtasks'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}-PUT': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'historyMetadata'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'transition'
            },
            {
                'name': 'update'
            },
            {
                'name': 'notifyUsers'
            },
            {
                'name': 'overrideScreenSecurity'
            },
            {
                'name': 'overrideEditableFlag'
            },
            {
                'name': 'returnIssue'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issues/archive/export-PUT': {
        'parameters': [
            {
                'name': 'archivedBy'
            },
            {
                'name': 'archivedDateRange'
            },
            {
                'name': 'issueTypes'
            },
            {
                'name': 'projects'
            },
            {
                'name': 'reporters'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/changelog-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/changelog/list-POST': {
        'parameters': [
            {
                'name': 'changelogIds'
            },
            {
                'name': 'issueIdOrKey'
            },
        ]
    },
    '/rest/api/3/issue/createmeta-GET': {
        'parameters': [
            {
                'name': 'projectIds'
            },
            {
                'name': 'projectKeys'
            },
            {
                'name': 'issuetypeIds'
            },
            {
                'name': 'issuetypeNames'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/editmeta-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'overrideScreenSecurity'
            },
            {
                'name': 'overrideEditableFlag'
            },
        ]
    },
    '/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'issueTypeId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'fieldsByKeys'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'updateHistory'
            },
        ]
    },
    '/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/transitions-GET': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'transitionId'
            },
            {
                'name': 'skipRemoteOnlyCondition'
            },
            {
                'name': 'includeUnavailableTransitions'
            },
            {
                'name': 'sortByOpsBarAndStatus'
            },
        ]
    },
    '/rest/api/3/events-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/notify-POST': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'htmlBody'
            },
            {
                'name': 'restrict'
            },
            {
                'name': 'subject'
            },
            {
                'name': 'textBody'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/rest/api/3/issue/{issueIdOrKey}/transitions-POST': {
        'parameters': [
            {
                'name': 'issueIdOrKey'
            },
            {
                'name': 'fields'
            },
            {
                'name': 'historyMetadata'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'transition'
            },
            {
                'name': 'update'
            },
        ]
    },
    '/rest/api/3/issue/unarchive-PUT': {
        'parameters': [
            {
                'name': 'issueIdsOrKeys'
            },
        ]
    },
    '/rest/api/3/jql/pdcleaner-POST': {
        'parameters': [
            {
                'name': 'queryStrings'
            },
        ]
    },
    '/rest/api/3/jql/autocompletedata/suggestions-GET': {
        'parameters': [
            {
                'name': 'fieldName'
            },
            {
                'name': 'fieldValue'
            },
            {
                'name': 'predicateName'
            },
            {
                'name': 'predicateValue'
            },
        ]
    },
    '/rest/api/3/jql/autocompletedata-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/jql/autocompletedata-POST': {
        'parameters': [
            {
                'name': 'includeCollapsedFields'
            },
            {
                'name': 'projectIds'
            },
        ]
    },
    '/rest/api/3/jql/parse-POST': {
        'parameters': [
            {
                'name': 'queries'
            },
            {
                'name': 'validation'
            },
        ]
    },
    '/rest/api/3/jql/sanitize-POST': {
        'parameters': [
            {
                'name': 'queries'
            },
        ]
    },
    '/rest/api/3/jql/function/computation-GET': {
        'parameters': [
            {
                'name': 'functionKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/rest/api/3/jql/function/computation-POST': {
        'parameters': [
            {
                'name': 'values'
            },
        ]
    },
    '/rest/api/3/expression/analyse-POST': {
        'parameters': [
            {
                'name': 'expressions'
            },
            {
                'name': 'contextVariables'
            },
            {
                'name': 'check'
            },
        ]
    },
    '/rest/api/3/expression/eval-POST': {
        'parameters': [
            {
                'name': 'expression'
            },
            {
                'name': 'context'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/application-properties/advanced-settings-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/application-properties-GET': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'permissionLevel'
            },
            {
                'name': 'keyFilter'
            },
        ]
    },
    '/rest/api/3/configuration-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/application-properties/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'id'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/rest/api/3/label-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/license/approximateLicenseCount/product/{applicationKey}-GET': {
        'parameters': [
            {
                'name': 'applicationKey'
            },
        ]
    },
    '/rest/api/3/license/approximateLicenseCount-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/instance/license-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/mypreferences/locale-DELETE': {
        'parameters': [
        ]
    },
    '/rest/api/3/mypreferences-DELETE': {
        'parameters': [
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/myself-GET': {
        'parameters': [
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/mypreferences-GET': {
        'parameters': [
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/mypreferences/locale-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/mypreferences/locale-PUT': {
        'parameters': [
            {
                'name': 'locale'
            },
        ]
    },
    '/rest/api/3/mypreferences-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/permissionscheme/{schemeId}/permission-POST': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'holder'
            },
            {
                'name': 'id'
            },
            {
                'name': 'permission'
            },
            {
                'name': 'self'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/permissionscheme-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'id'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'self'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}-DELETE': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'permissionId'
            },
        ]
    },
    '/rest/api/3/permissionscheme/{schemeId}-DELETE': {
        'parameters': [
            {
                'name': 'schemeId'
            },
        ]
    },
    '/rest/api/3/permissionscheme-GET': {
        'parameters': [
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/permissionscheme/{schemeId}/permission-GET': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}-GET': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'permissionId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/permissionscheme/{schemeId}-GET': {
        'parameters': [
            {
                'name': 'schemeId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/permissionscheme/{schemeId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'schemeId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'id'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'self'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/permissions-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/permissions/check-POST': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'globalPermissions'
            },
            {
                'name': 'projectPermissions'
            },
        ]
    },
    '/rest/api/3/permissions/project-POST': {
        'parameters': [
            {
                'name': 'permissions'
            },
        ]
    },
    '/rest/api/3/mypermissions-GET': {
        'parameters': [
            {
                'name': 'projectKey'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'issueKey'
            },
            {
                'name': 'issueId'
            },
            {
                'name': 'permissions'
            },
            {
                'name': 'projectUuid'
            },
            {
                'name': 'projectConfigurationUuid'
            },
            {
                'name': 'commentId'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/avatar/{id}-DELETE': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/avatars-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/avatar-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'fileName'
            },
            {
                'name': 'isDeletable'
            },
            {
                'name': 'isSelected'
            },
            {
                'name': 'isSystemAvatar'
            },
            {
                'name': 'owner'
            },
            {
                'name': 'urls'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/avatar2-POST': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'x'
            },
            {
                'name': 'y'
            },
            {
                'name': 'size'
            },
        ]
    },
    '/rest/api/3/projectCategory-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'self'
            },
        ]
    },
    '/rest/api/3/projectCategory/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/projectCategory-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/projectCategory/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/projectCategory/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'self'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/classification-level/default-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/classification-level/default-DELETE': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/classification-level/default-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/component-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'ari'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'assigneeType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'isAssigneeTypeValid'
            },
            {
                'name': 'lead'
            },
            {
                'name': 'leadAccountId'
            },
            {
                'name': 'leadUserName'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'name'
            },
            {
                'name': 'project'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'realAssignee'
            },
            {
                'name': 'realAssigneeType'
            },
            {
                'name': 'self'
            },
        ]
    },
    '/rest/api/3/component/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'moveIssuesTo'
            },
        ]
    },
    '/rest/api/3/component-GET': {
        'parameters': [
            {
                'name': 'projectIdsOrKeys'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'query'
            },
        ]
    },
    '/rest/api/3/component/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/component/{id}/relatedIssueCounts-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/components-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'componentSource'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/component-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'componentSource'
            },
            {
                'name': 'query'
            },
        ]
    },
    '/rest/api/3/component/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'ari'
            },
            {
                'name': 'assignee'
            },
            {
                'name': 'assigneeType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'isAssigneeTypeValid'
            },
            {
                'name': 'lead'
            },
            {
                'name': 'leadAccountId'
            },
            {
                'name': 'leadUserName'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'name'
            },
            {
                'name': 'project'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'realAssignee'
            },
            {
                'name': 'realAssigneeType'
            },
            {
                'name': 'self'
            },
        ]
    },
    '/rest/api/3/project/{projectId}/email-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/project/{projectId}/email-PUT': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'emailAddress'
            },
            {
                'name': 'emailAddressStatus'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/features-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/features/{featureKey}-PUT': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'featureKey'
            },
            {
                'name': 'state'
            },
        ]
    },
    '/rest/api/3/projectvalidate/validProjectKey-GET': {
        'parameters': [
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/projectvalidate/validProjectName-GET': {
        'parameters': [
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/projectvalidate/key-GET': {
        'parameters': [
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/project/{projectKeyOrId}/permissionscheme-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'projectKeyOrId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/project/{projectKeyOrId}/permissionscheme-GET': {
        'parameters': [
            {
                'name': 'projectKeyOrId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/project/{projectKeyOrId}/securitylevel-GET': {
        'parameters': [
            {
                'name': 'projectKeyOrId'
            },
        ]
    },
    '/rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme-GET': {
        'parameters': [
            {
                'name': 'projectKeyOrId'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/properties-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'propertyKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/role/{id}-POST': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'group'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/rest/api/3/role/{id}/actors-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'group'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/rest/api/3/role/{id}/actors-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/role/{id}-DELETE': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'user'
            },
            {
                'name': 'group'
            },
            {
                'name': 'groupId'
            },
        ]
    },
    '/rest/api/3/role/{id}/actors-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'user'
            },
            {
                'name': 'groupId'
            },
            {
                'name': 'group'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/role/{id}-PUT': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'categorisedActors'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/role-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/role/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'swap'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/role/{id}-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'id'
            },
            {
                'name': 'excludeInactiveUsers'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/role-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/role/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/roledetails-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'currentMember'
            },
            {
                'name': 'excludeConnectAddons'
            },
        ]
    },
    '/rest/api/3/role-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/role/{id}-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/role/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/project/type/{projectTypeKey}/accessible-GET': {
        'parameters': [
            {
                'name': 'projectTypeKey'
            },
        ]
    },
    '/rest/api/3/project/type-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/project/type/{projectTypeKey}-GET': {
        'parameters': [
            {
                'name': 'projectTypeKey'
            },
        ]
    },
    '/rest/api/3/project/type/accessible-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/version-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'approvers'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'driver'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issuesStatusForFixVersion'
            },
            {
                'name': 'moveUnfixedIssuesTo'
            },
            {
                'name': 'name'
            },
            {
                'name': 'operations'
            },
            {
                'name': 'overdue'
            },
            {
                'name': 'project'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'releaseDate'
            },
            {
                'name': 'released'
            },
            {
                'name': 'self'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'userReleaseDate'
            },
            {
                'name': 'userStartDate'
            },
        ]
    },
    '/rest/api/3/version/{id}/relatedwork-POST': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'issueId'
            },
            {
                'name': 'relatedWorkId'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/rest/api/3/version/{id}/removeAndSwap-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'customFieldReplacementList'
            },
            {
                'name': 'moveAffectedIssuesTo'
            },
            {
                'name': 'moveFixIssuesTo'
            },
        ]
    },
    '/rest/api/3/version/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'moveFixIssuesTo'
            },
            {
                'name': 'moveAffectedIssuesTo'
            },
        ]
    },
    '/rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}-DELETE': {
        'parameters': [
            {
                'name': 'versionId'
            },
            {
                'name': 'relatedWorkId'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/versions-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/version/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/version/{id}/relatedIssueCounts-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/version/{id}/relatedwork-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/version/{id}/unresolvedIssueCount-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/version-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'query'
            },
            {
                'name': 'status'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/version/{id}/mergeto/{moveIssuesTo}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'moveIssuesTo'
            },
        ]
    },
    '/rest/api/3/version/{id}/relatedwork-PUT': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'issueId'
            },
            {
                'name': 'relatedWorkId'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/rest/api/3/version/{id}/move-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'after'
            },
            {
                'name': 'position'
            },
        ]
    },
    '/rest/api/3/version/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'approvers'
            },
            {
                'name': 'archived'
            },
            {
                'name': 'driver'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issuesStatusForFixVersion'
            },
            {
                'name': 'moveUnfixedIssuesTo'
            },
            {
                'name': 'name'
            },
            {
                'name': 'operations'
            },
            {
                'name': 'overdue'
            },
            {
                'name': 'project'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'releaseDate'
            },
            {
                'name': 'released'
            },
            {
                'name': 'self'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'userReleaseDate'
            },
            {
                'name': 'userStartDate'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/archive-POST': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project-POST': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'assigneeType'
            },
            {
                'name': 'avatarId'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'fieldConfigurationScheme'
            },
            {
                'name': 'issueSecurityScheme'
            },
            {
                'name': 'issueTypeScheme'
            },
            {
                'name': 'issueTypeScreenScheme'
            },
            {
                'name': 'lead'
            },
            {
                'name': 'leadAccountId'
            },
            {
                'name': 'notificationScheme'
            },
            {
                'name': 'permissionScheme'
            },
            {
                'name': 'projectTemplateKey'
            },
            {
                'name': 'projectTypeKey'
            },
            {
                'name': 'url'
            },
            {
                'name': 'workflowScheme'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/delete-POST': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}-DELETE': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'enableUndo'
            },
        ]
    },
    '/rest/api/3/project-GET': {
        'parameters': [
            {
                'name': 'expand'
            },
            {
                'name': 'recent'
            },
            {
                'name': 'properties'
            },
        ]
    },
    '/rest/api/3/project/{projectId}/hierarchy-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/project/{projectKeyOrId}/notificationscheme-GET': {
        'parameters': [
            {
                'name': 'projectKeyOrId'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'properties'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/statuses-GET': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project/recent-GET': {
        'parameters': [
            {
                'name': 'expand'
            },
            {
                'name': 'properties'
            },
        ]
    },
    '/rest/api/3/project/search-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'id'
            },
            {
                'name': 'keys'
            },
            {
                'name': 'query'
            },
            {
                'name': 'typeKey'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'action'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'status'
            },
            {
                'name': 'properties'
            },
            {
                'name': 'propertyQuery'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}/restore-POST': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
        ]
    },
    '/rest/api/3/project/{projectIdOrKey}-PUT': {
        'parameters': [
            {
                'name': 'projectIdOrKey'
            },
            {
                'name': 'description'
            },
            {
                'name': 'assigneeType'
            },
            {
                'name': 'avatarId'
            },
            {
                'name': 'categoryId'
            },
            {
                'name': 'issueSecurityScheme'
            },
            {
                'name': 'key'
            },
            {
                'name': 'lead'
            },
            {
                'name': 'leadAccountId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'notificationScheme'
            },
            {
                'name': 'permissionScheme'
            },
            {
                'name': 'url'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/screenscheme-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'screens'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/screenscheme/{screenSchemeId}-DELETE': {
        'parameters': [
            {
                'name': 'screenSchemeId'
            },
        ]
    },
    '/rest/api/3/screenscheme-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'queryString'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/rest/api/3/screenscheme/{screenSchemeId}-PUT': {
        'parameters': [
            {
                'name': 'screenSchemeId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'screens'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields-POST': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'screenId'
            },
            {
                'name': 'tabId'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields-GET': {
        'parameters': [
            {
                'name': 'screenId'
            },
            {
                'name': 'tabId'
            },
            {
                'name': 'projectKey'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move-POST': {
        'parameters': [
            {
                'name': 'screenId'
            },
            {
                'name': 'tabId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'after'
            },
            {
                'name': 'position'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}-DELETE': {
        'parameters': [
            {
                'name': 'screenId'
            },
            {
                'name': 'tabId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'screenId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs/{tabId}-DELETE': {
        'parameters': [
            {
                'name': 'screenId'
            },
            {
                'name': 'tabId'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs-GET': {
        'parameters': [
            {
                'name': 'screenId'
            },
            {
                'name': 'projectKey'
            },
        ]
    },
    '/rest/api/3/screens/tabs-GET': {
        'parameters': [
            {
                'name': 'screenId'
            },
            {
                'name': 'tabId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResult'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}-POST': {
        'parameters': [
            {
                'name': 'screenId'
            },
            {
                'name': 'tabId'
            },
            {
                'name': 'pos'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/tabs/{tabId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'screenId'
            },
            {
                'name': 'tabId'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/screens/addToDefault/{fieldId}-POST': {
        'parameters': [
            {
                'name': 'fieldId'
            },
        ]
    },
    '/rest/api/3/screens-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}-DELETE': {
        'parameters': [
            {
                'name': 'screenId'
            },
        ]
    },
    '/rest/api/3/field/{fieldId}/screens-GET': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}/availableFields-GET': {
        'parameters': [
            {
                'name': 'screenId'
            },
        ]
    },
    '/rest/api/3/screens-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'id'
            },
            {
                'name': 'queryString'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'orderBy'
            },
        ]
    },
    '/rest/api/3/screens/{screenId}-PUT': {
        'parameters': [
            {
                'name': 'screenId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/serverInfo-GET': {
        'parameters': [
        ]
    },
    '/rest/atlassian-connect/1/service-registry-GET': {
        'parameters': [
            {
                'name': 'serviceIds'
            },
        ]
    },
    '/rest/api/3/statuses-POST': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'statuses'
            },
        ]
    },
    '/rest/api/3/statuses-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/statuses-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/statuses-PUT': {
        'parameters': [
            {
                'name': 'statuses'
            },
        ]
    },
    '/rest/api/3/statuses/search-GET': {
        'parameters': [
            {
                'name': 'expand'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'searchString'
            },
            {
                'name': 'statusCategory'
            },
        ]
    },
    '/rest/api/3/task/{taskId}/cancel-POST': {
        'parameters': [
            {
                'name': 'taskId'
            },
        ]
    },
    '/rest/api/3/task/{taskId}-GET': {
        'parameters': [
            {
                'name': 'taskId'
            },
        ]
    },
    '/rest/api/3/configuration/timetracking/list-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/configuration/timetracking/options-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/configuration/timetracking-PUT': {
        'parameters': [
            {
                'name': 'key'
            },
            {
                'name': 'name'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/rest/api/3/configuration/timetracking-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/configuration/timetracking/options-PUT': {
        'parameters': [
            {
                'name': 'defaultUnit'
            },
            {
                'name': 'timeFormat'
            },
            {
                'name': 'workingDaysPerWeek'
            },
            {
                'name': 'workingHoursPerDay'
            },
        ]
    },
    '/rest/api/3/uiModifications-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'contexts'
            },
            {
                'name': 'data'
            },
        ]
    },
    '/rest/api/3/uiModifications/{uiModificationId}-DELETE': {
        'parameters': [
            {
                'name': 'uiModificationId'
            },
        ]
    },
    '/rest/api/3/uiModifications-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/uiModifications/{uiModificationId}-PUT': {
        'parameters': [
            {
                'name': 'uiModificationId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'contexts'
            },
            {
                'name': 'data'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/rest/api/3/user/properties/{propertyKey}-DELETE': {
        'parameters': [
            {
                'name': 'propertyKey'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'userKey'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/rest/api/3/user/properties/{propertyKey}-GET': {
        'parameters': [
            {
                'name': 'propertyKey'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'userKey'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/rest/api/3/user/properties-GET': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'userKey'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/rest/api/3/user/properties/{propertyKey}-PUT': {
        'parameters': [
            {
                'name': 'propertyKey'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'userKey'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/rest/api/3/user/assignable/multiProjectSearch-GET': {
        'parameters': [
            {
                'name': 'projectKeys'
            },
            {
                'name': 'query'
            },
            {
                'name': 'username'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/user/assignable/search-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'sessionId'
            },
            {
                'name': 'username'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'project'
            },
            {
                'name': 'issueKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'actionDescriptorId'
            },
            {
                'name': 'recommend'
            },
        ]
    },
    '/rest/api/3/user/search-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'username'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'property'
            },
        ]
    },
    '/rest/api/3/user/search/query-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/user/search/query/key-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResult'
            },
        ]
    },
    '/rest/api/3/user/picker-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'showAvatar'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'excludeAccountIds'
            },
            {
                'name': 'avatarSize'
            },
            {
                'name': 'excludeConnectUsers'
            },
        ]
    },
    '/rest/api/3/user/viewissue/search-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'username'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'issueKey'
            },
            {
                'name': 'projectKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/user/permission/search-GET': {
        'parameters': [
            {
                'name': 'permissions'
            },
            {
                'name': 'query'
            },
            {
                'name': 'username'
            },
            {
                'name': 'accountId'
            },
            {
                'name': 'issueKey'
            },
            {
                'name': 'projectKey'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/user/bulk-GET': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'username'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/user-POST': {
        'parameters': [
            {
                'name': 'emailAddress'
            },
            {
                'name': 'applicationKeys'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'key'
            },
            {
                'name': 'name'
            },
            {
                'name': 'password'
            },
            {
                'name': 'products'
            },
            {
                'name': 'self'
            },
        ]
    },
    '/rest/api/3/user-DELETE': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'username'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/user/bulk/migration-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'username'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/user/columns-GET': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/rest/api/3/user-GET': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'username'
            },
            {
                'name': 'key'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/user/email-GET': {
        'parameters': [
            {
                'name': 'accountId'
            },
        ]
    },
    '/rest/api/3/user/email/bulk-GET': {
        'parameters': [
            {
                'name': 'accountId'
            },
        ]
    },
    '/rest/api/3/user/groups-GET': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'username'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/rest/api/3/users/search-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/users-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/user/columns-DELETE': {
        'parameters': [
            {
                'name': 'accountId'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/rest/api/3/user/columns-PUT': {
        'parameters': [
            {
                'name': 'columns'
            },
            {
                'name': 'accountId'
            },
        ]
    },
    '/rest/api/3/webhook-DELETE': {
        'parameters': [
            {
                'name': 'webhookIds'
            },
        ]
    },
    '/rest/api/3/webhook/refresh-PUT': {
        'parameters': [
            {
                'name': 'webhookIds'
            },
        ]
    },
    '/rest/api/3/webhook-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/webhook/failed-GET': {
        'parameters': [
            {
                'name': 'maxResults'
            },
            {
                'name': 'after'
            },
        ]
    },
    '/rest/api/3/webhook-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'webhooks'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/createdraft-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'issueType'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/workflow-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'workflowName'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/default-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/workflow-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'workflowName'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'issueType'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/publish-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'statusMappings'
            },
            {
                'name': 'validateOnly'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/default-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'issueType'
            },
            {
                'name': 'issueType'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
            {
                'name': 'workflow'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/workflow-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'defaultMapping'
            },
            {
                'name': 'issueTypes'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
            {
                'name': 'workflow'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft/default-PUT': {
        'parameters': [
            {
                'name': 'workflow'
            },
            {
                'name': 'id'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/draft-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'defaultWorkflow'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issueTypeMappings'
            },
            {
                'name': 'issueTypes'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'lastModifiedUser'
            },
            {
                'name': 'name'
            },
            {
                'name': 'originalDefaultWorkflow'
            },
            {
                'name': 'originalIssueTypeMappings'
            },
            {
                'name': 'self'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
        ]
    },
    '/rest/api/3/workflowscheme/project-PUT': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'workflowSchemeId'
            },
        ]
    },
    '/rest/api/3/workflowscheme/project-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
        ]
    },
    '/rest/api/3/workflowscheme/read-POST': {
        'parameters': [
            {
                'name': 'projectIds'
            },
            {
                'name': 'workflowSchemeIds'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/workflowscheme-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'defaultWorkflow'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issueTypeMappings'
            },
            {
                'name': 'issueTypes'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'lastModifiedUser'
            },
            {
                'name': 'name'
            },
            {
                'name': 'originalDefaultWorkflow'
            },
            {
                'name': 'originalIssueTypeMappings'
            },
            {
                'name': 'self'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'issueType'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/workflow-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/rest/api/3/workflowscheme-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/default-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'returnDraftIfExists'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'issueType'
            },
            {
                'name': 'returnDraftIfExists'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/workflow-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'returnDraftIfExists'
            },
        ]
    },
    '/rest/api/3/workflowscheme/update/mappings-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'workflowsForIssueTypes'
            },
            {
                'name': 'defaultWorkflowId'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'returnDraftIfExists'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/default-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/issuetype/{issueType}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'issueType'
            },
            {
                'name': 'issueType'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
            {
                'name': 'workflow'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/workflow-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'defaultMapping'
            },
            {
                'name': 'issueTypes'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
            {
                'name': 'workflow'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}/default-PUT': {
        'parameters': [
            {
                'name': 'workflow'
            },
            {
                'name': 'id'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
        ]
    },
    '/rest/api/3/workflowscheme/update-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'version'
            },
            {
                'name': 'id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'defaultWorkflowId'
            },
            {
                'name': 'statusMappingsByIssueTypeOverride'
            },
            {
                'name': 'statusMappingsByWorkflows'
            },
            {
                'name': 'workflowsForIssueTypes'
            },
        ]
    },
    '/rest/api/3/workflowscheme/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'defaultWorkflow'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'id'
            },
            {
                'name': 'issueTypeMappings'
            },
            {
                'name': 'issueTypes'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'lastModifiedUser'
            },
            {
                'name': 'name'
            },
            {
                'name': 'originalDefaultWorkflow'
            },
            {
                'name': 'originalIssueTypeMappings'
            },
            {
                'name': 'self'
            },
            {
                'name': 'updateDraftIfNeeded'
            },
        ]
    },
    '/rest/api/3/statuscategory-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/statuscategory/{idOrKey}-GET': {
        'parameters': [
            {
                'name': 'idOrKey'
            },
        ]
    },
    '/rest/api/3/status-GET': {
        'parameters': [
        ]
    },
    '/rest/api/3/status/{idOrName}-GET': {
        'parameters': [
            {
                'name': 'idOrName'
            },
        ]
    },
    '/rest/api/3/workflow/transitions/{transitionId}/properties-POST': {
        'parameters': [
            {
                'name': 'value'
            },
            {
                'name': 'transitionId'
            },
            {
                'name': 'key'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'key'
            },
            {
                'name': 'workflowMode'
            },
        ]
    },
    '/rest/api/3/workflow/transitions/{transitionId}/properties-DELETE': {
        'parameters': [
            {
                'name': 'transitionId'
            },
            {
                'name': 'key'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'workflowMode'
            },
        ]
    },
    '/rest/api/3/workflow/transitions/{transitionId}/properties-GET': {
        'parameters': [
            {
                'name': 'transitionId'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'includeReservedKeys'
            },
            {
                'name': 'key'
            },
            {
                'name': 'workflowMode'
            },
        ]
    },
    '/rest/api/3/workflow/transitions/{transitionId}/properties-PUT': {
        'parameters': [
            {
                'name': 'value'
            },
            {
                'name': 'transitionId'
            },
            {
                'name': 'key'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'id'
            },
            {
                'name': 'key'
            },
            {
                'name': 'workflowMode'
            },
        ]
    },
    '/rest/api/3/workflow/rule/config/delete-PUT': {
        'parameters': [
            {
                'name': 'workflows'
            },
        ]
    },
    '/rest/api/3/workflow/rule/config-GET': {
        'parameters': [
            {
                'name': 'types'
            },
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'keys'
            },
            {
                'name': 'workflowNames'
            },
            {
                'name': 'withTags'
            },
            {
                'name': 'draft'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/workflow/rule/config-PUT': {
        'parameters': [
            {
                'name': 'workflows'
            },
        ]
    },
    '/rest/api/3/workflows/create-POST': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'workflows'
            },
        ]
    },
    '/rest/api/3/workflows-POST': {
        'parameters': [
            {
                'name': 'projectAndIssueTypes'
            },
            {
                'name': 'workflowIds'
            },
            {
                'name': 'workflowNames'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/workflows/update-POST': {
        'parameters': [
            {
                'name': 'statuses'
            },
            {
                'name': 'workflows'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/rest/api/3/workflow-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'transitions'
            },
            {
                'name': 'description'
            },
        ]
    },
    '/rest/api/3/workflow/{entityId}-DELETE': {
        'parameters': [
            {
                'name': 'entityId'
            },
        ]
    },
    '/rest/api/3/workflow-GET': {
        'parameters': [
            {
                'name': 'workflowName'
            },
        ]
    },
    '/rest/api/3/workflow/search-GET': {
        'parameters': [
            {
                'name': 'startAt'
            },
            {
                'name': 'maxResults'
            },
            {
                'name': 'workflowName'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'queryString'
            },
            {
                'name': 'orderBy'
            },
            {
                'name': 'isActive'
            },
        ]
    },
    '/rest/api/3/workflows/capabilities-GET': {
        'parameters': [
            {
                'name': 'workflowId'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'issueTypeId'
            },
        ]
    },
    '/rest/api/3/workflows/create/validation-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
            {
                'name': 'validationOptions'
            },
        ]
    },
    '/rest/api/3/workflows/update/validation-POST': {
        'parameters': [
            {
                'name': 'payload'
            },
            {
                'name': 'validationOptions'
            },
        ]
    },
};