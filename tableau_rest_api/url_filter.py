from ..tableau_exceptions import *


class UrlFilter:
    def __init__(self, field, operator, values):
        self.field = field
        self.operator = operator
        self.values = values

    def get_filter_string(self):
        """
        :rtype: unicode
        """
        if len(self.values) == 0:
            raise InvalidOptionException('Must pass in at least one value for the filter')
        elif len(self.values) == 1:
            value_string = self.values[0]
        else:
            value_string = ",".join(self.values)
            value_string = "[{}]".format(value_string)
        url = "{}:{}:{}".format(self.field, self.operator, value_string)
        return url

    # Users, Datasources, Views, Workbooks
    @staticmethod
    def create_name_filter(name):
        """
        :type name: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('name', 'eq', [name, ])

    # Users
    @staticmethod
    def create_last_login_filter(operator, last_login_time):
        """
        :param operator: Should be one of 'eq', 'gt', 'gte', 'lt', 'lte'
        :type operator: unicode
        :param last_login_time: ISO 8601 representation of time like 2016-01-01T00:00:00:00Z
        :type last_login_time: unicode
        :rtype: UrlFilter
        """
        comparison_operators = ['eq', 'gt', 'gte', 'lt', 'lte']
        if operator not in comparison_operators:
            raise InvalidOptionException("operator must be one of 'eq', 'gt', 'gte', 'lt', 'lte' ")
        # Convert to the correct time format

        return UrlFilter('lastLogin', operator, [last_login_time, ])

    # Users
    @staticmethod
    def create_site_role_filter(site_role):
        """
        :type site_role: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('siteRole', 'eq', [site_role, ])

    # Workbooks
    @staticmethod
    def create_owner_name_filter(owner_name):
        """
        :type owner_name: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('ownerName', 'eq', [owner_name, ])

    # Workbooks, Datasources, Views, Jobs
    @staticmethod
    def create_created_at_filter(operator, created_at_time):
        """
        :param operator: Should be one of 'eq', 'gt', 'gte', 'lt', 'lte'
        :type operator: unicode
        :param created_at_time: ISO 8601 representation of time like 2016-01-01T00:00:00:00Z
        :type created_at_time: unicode
        :rtype: UrlFilter
        """
        comparison_operators = ['eq', 'gt', 'gte', 'lt', 'lte']
        if operator not in comparison_operators:
            raise InvalidOptionException("operator must be one of 'eq', 'gt', 'gte', 'lt', 'lte' ")
        # Convert to the correct time format

        return UrlFilter('createdAt', operator, [created_at_time, ])

    # Workbooks, Datasources, Views
    @staticmethod
    def create_updated_at_filter(operator, updated_at_time):
        """
        :param operator: Should be one of 'eq', 'gt', 'gte', 'lt', 'lte'
        :type operator: unicode
        :param updated_at_time: ISO 8601 representation of time like 2016-01-01T00:00:00:00Z
        :type updated_at_time: unicode
        :rtype: UrlFilter
        """
        comparison_operators = ['eq', 'gt', 'gte', 'lt', 'lte']
        if operator not in comparison_operators:
            raise InvalidOptionException("operator must be one of 'eq', 'gt', 'gte', 'lt', 'lte' ")
        # Convert to the correct time format

        return UrlFilter('updatedAt', operator, [updated_at_time, ])

    # Workbooks, Datasources, Views
    @staticmethod
    def create_tags_filter(tags):
        """
        :type tags: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('tags', 'in', tags)

    # Workbooks, Datasources, Views
    @staticmethod
    def create_tag_filter(tag):
        """
        :type tag: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('tags', 'eq', [tag, ])

    # Datasources
    @staticmethod
    def create_datasource_type_filter(ds_type):
        """
        :type ds_type: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('type', 'eq', [ds_type, ])

class UrlFilter27(UrlFilter):
    def __init__(self, field, operator, values):
        UrlFilter.__init__(self, field, operator, values)
    # Some of the previous methods add in methods

    # Users, Datasources, Views, Workbooks
    @staticmethod
    def create_names_filter(names):
        """
        :type names: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('name', 'in', names)

    # Users
    @staticmethod
    def create_site_roles_filter(site_roles):
        """
        :type site_roles: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('siteRole', 'in', site_roles)

    # Workbooks, Projects
    @staticmethod
    def create_owner_names_filter(owner_names):
        """
        :type owner_names: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('ownerName', 'in', owner_names)

    # Workbooks. Datasources, Views
    # create_owner_name_filter (singular) allowed for all of them

    # Groups
    @staticmethod
    def create_domain_names_filter(domain_names):
        """
        :type domain_names: list[unicode]
        :rtype: UrlFilter
        """

        return UrlFilter('domainName', 'in', domain_names)

    # Groups
    @staticmethod
    def create_domain_nicknames_filter(domain_nicknames):
        """
        :type domain_nicknames: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('domainNickname', 'in', domain_nicknames)

    # Groups
    @staticmethod
    def create_domain_name_filter(domain_name):
        """
        :type domain_name: unicode
        :rtype: UrlFilter
        """

        return UrlFilter('domainName', 'eq', [domain_name, ])

    # Groups
    @staticmethod
    def create_domain_nickname_filter(domain_nickname):
        """
        :type domain_nickname: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('domainNickname', 'eq', [domain_nickname, ])

    # Groups
    @staticmethod
    def create_minimum_site_roles_filter(minimum_site_roles):
        """
        :type minimum_site_roles: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('minimumSiteRole', 'in', minimum_site_roles)

    # Groups
    @staticmethod
    def create_minimum_site_role_filter(minimum_site_role):
        """
        :type minimum_site_role: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('minimumSiteRole', 'eq', [minimum_site_role, ])

    # Groups
    @staticmethod
    def create_is_local_filter(is_local):
        """
        :type is_local:
        :return: bool
        """
        if is_local not in [True, False]:
            raise InvalidOptionException('is_local must be True or False')
        return UrlFilter('isLocal', 'eq', str(is_local).lower())

    # Groups
    @staticmethod
    def create_user_count_filter(operator, user_count):
        """
        :param operator: Should be one of 'eq', 'gt', 'gte', 'lt', 'lte'
        :type operator: unicode
        :type user_count: int
        :rtype: UrlFilter
        """
        comparison_operators = ['eq', 'gt', 'gte', 'lt', 'lte']
        if operator not in comparison_operators:
            raise InvalidOptionException("operator must be one of 'eq', 'gt', 'gte', 'lt', 'lte' ")
        # Convert to the correct time format

        return UrlFilter('userCount', operator, [user_count, ])

    # Projects
    @staticmethod
    def create_owner_domains_filter(owner_domains):
        """
        :param owner_domains: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('ownerDomain', 'in', owner_domains)

    # Projects
    @staticmethod
    def create_owner_domain_filter(owner_domain):
        """
        :param owner_domain: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('ownerDomain', 'in', [owner_domain, ])

    # Projects
    @staticmethod
    def create_owner_emails_filter(owner_emails):
        """
        :param owner_emails: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('ownerEmail', 'in', owner_emails)

    # Projects
    @staticmethod
    def create_owner_email_filter(owner_email):
        """
        :param owner_email: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('ownerEmail', 'in', [owner_email, ])

    # Views
    @staticmethod
    def create_hits_total_filter(operator, hits_total):
        """
        :param operator: Should be one of 'eq', 'gt', 'gte', 'lt', 'lte'
        :type operator: unicode
        :type hits_total: int
        :rtype: UrlFilter
        """
        comparison_operators = ['eq', 'gt', 'gte', 'lt', 'lte']
        if operator not in comparison_operators:
            raise InvalidOptionException("operator must be one of 'eq', 'gt', 'gte', 'lt', 'lte' ")
        # Convert to the correct time format

        return UrlFilter('hitsTotal', operator, [hits_total, ])


class UrlFilter28(UrlFilter27):
    def __init__(self, field, operator, values):
        UrlFilter27.__init__(self, field, operator, values)
    # No changes in 2.8


class UrlFilter30(UrlFilter28):
    def __init__(self, field, operator, values):
        UrlFilter28.__init__(self, field, operator, values)
    # No changes in 3.0


class UrlFilter31(UrlFilter30):
    def __init__(self, field, operator, values):
        UrlFilter30.__init__(self, field, operator, values)

    # Jobs
    @staticmethod
    def create_started_at_filter(operator, started_at_time) -> UrlFilter:
        """
        :param operator: Should be one of 'eq', 'gt', 'gte', 'lt', 'lte'
        :type operator: unicode
        :param started_at_time: ISO 8601 representation of time like 2016-01-01T00:00:00:00Z
        :type started_at_time: unicode
        :rtype: UrlFilter
        """
        comparison_operators = ['eq', 'gt', 'gte', 'lt', 'lte']
        if operator not in comparison_operators:
            raise InvalidOptionException("operator must be one of 'eq', 'gt', 'gte', 'lt', 'lte' ")
        # Convert to the correct time format

        return UrlFilter('createdAt', operator, [started_at_time, ])

    # Jobs
    @staticmethod
    def create_ended_at_filter(operator, ended_at_time) -> UrlFilter:
        """
        :param operator: Should be one of 'eq', 'gt', 'gte', 'lt', 'lte'
        :type operator: unicode
        :param ended_at_time: ISO 8601 representation of time like 2016-01-01T00:00:00:00Z
        :type ended_at_time: unicode
        :rtype: UrlFilter
        """
        comparison_operators = ['eq', 'gt', 'gte', 'lt', 'lte']
        if operator not in comparison_operators:
            raise InvalidOptionException("operator must be one of 'eq', 'gt', 'gte', 'lt', 'lte' ")
        # Convert to the correct time format

        return UrlFilter('createdAt', operator, [ended_at_time, ])

    # Jobs
    @staticmethod
    def create_job_types_filter(job_types) -> UrlFilter:
        """
        :type job_types: list[unicode]
        :rtype: UrlFilter
        """
        return UrlFilter('jobType', 'in', job_types)

    # Jobs
    @staticmethod
    def create_job_type_filter(job_type) -> UrlFilter:
        """
        :type job_type: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('tags', 'eq', [job_type, ])

    # Jobs
    @staticmethod
    def create_notes_filter(notes) -> UrlFilter:
        """
        :type notes: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('notes', 'has', [notes, ])

    @staticmethod
    def create_title_equals_filter(title) -> UrlFilter:
        """
        :type title: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('title', 'eq', [title, ])

    @staticmethod
    def create_title_has_filter(title) -> UrlFilter:
        """
        :type title: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('title', 'has', [title, ])

    @staticmethod
    def create_subtitle_equals_filter(subtitle) -> UrlFilter:
        """
        :type subtitle: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('subtitle', 'eq', [subtitle, ])

    @staticmethod
    def create_subtitle_has_filter(subtitle) -> UrlFilter:
        """
        :type subtitle: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('subtitle', 'has', [subtitle, ])

class UrlFilter33(UrlFilter31):
    def __init__(self, field, operator, values):
        UrlFilter31.__init__(self, field, operator, values)

    @staticmethod
    def create_project_name_equals_filter(project_name) -> UrlFilter:
        """
        :type subtitle: unicode
        :rtype: UrlFilter
        """
        return UrlFilter('projectName', 'eq', [project_name, ])
