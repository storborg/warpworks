from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from pyramid_frontend.theme import Theme
from pyramid_frontend.assets.less import LessAsset
from pyramid_frontend.assets.requirejs import RequireJSAsset


class LightTheme(Theme):
    key = 'light'

    assets = {
        'main-less': LessAsset(
            '/_light/css/main.less',
            less_path='/_light/js/vendor/less.js',
            lessc_path='/var/sw/less-1.7.0/node_modules/less/bin/lessc',
        ),
        'main-js': RequireJSAsset(
            '/_light/js/main.js',
            require_config_path='/_light/js/require_config.js',
            require_base_url='/_light/js/vendor/',
        ),
    }

    image_filters = [
    ]
