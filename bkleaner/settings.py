"""Global settings."""

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
            '%(asctime)s - %(levelname)s - '
            '%(module)s.%(funcName)s:%(lineno)d - %(message)s'
        },
        'system': {
            'format':
            '%(name)s %(module)s: %(message)s'
        },
        'simple': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'formatter': 'system'
        }
    },
    'loggers': {
        'bkleaner': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}
