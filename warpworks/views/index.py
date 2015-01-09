from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from pyramid.view import view_config
from pyweaving.generators.twill import twill


@view_config(route_name='index', renderer='index.html')
def index_view(request):
    draft = twill(2, warp_color=(200, 0, 0), weft_color=(90, 90, 90))
    return dict(draft_json=draft.to_json())
