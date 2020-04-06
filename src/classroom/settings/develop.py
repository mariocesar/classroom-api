from .base import *

DEBUG = True

INSTALLED_APPS = [
    *INSTALLED_APPS,
    "debug_toolbar"
]

INTERNAL_IPS = ["127.0.0.1"]

AUTH_PASSWORD_VALIDATORS = []

MIDDLEWARE = [
    *MIDDLEWARE,
    "debug_toolbar.middleware.DebugToolbarMiddleware"
]
