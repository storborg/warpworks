from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


settings = {
    'sqlalchemy.url': 'sqlite:///',

    'elastic.index': 'warpworks-tests',

    'debug': 'true',

    'pyramid_frontend.compiled_asset_dir': '/tmp/warpworks/compiled',
    'pyramid_frontend.theme': 'light',

    'gimlet.secret': 's3krit',
}
