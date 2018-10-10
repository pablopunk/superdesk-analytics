# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2018 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license

import superdesk
from .content_publishing_report import ContentPublishingReportResource, \
    ContentPublishingReportService


def init_app(app):
    endpoint_name = 'content_publishing_report'
    service = ContentPublishingReportService(endpoint_name, backend=superdesk.get_backend())
    ContentPublishingReportResource(endpoint_name, app=app, service=service)

    superdesk.privilege(
        name='content_publishing_report',
        label='Content Publishing Reports',
        description='User can view Content Publishing Reports'
    )
