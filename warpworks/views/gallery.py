from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from pyramid.view import view_config

from .. import model


@view_config(route_name='gallery', renderer='gallery.html')
def gallery_view(request):
    q = model.Session.query(model.DraftMeta)
    return dict(drafts=q.all())
