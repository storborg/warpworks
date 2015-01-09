from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


def includeme(config):
    config.include('.error')

    config.add_route('index', '/')
    config.add_route('about', '/about')
    config.add_route('gallery', '/gallery')

    # User scaffolding routes
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('forgot-password', '/forgot-password')
    config.add_route('forgot-reset', '/forgot-reset')
    config.add_route('account', '/account')
    config.add_route('settings', '/account/settings')

    config.scan('.')
