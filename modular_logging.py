import logging.config



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(pathname)s:%(lineno)d %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'rror.log',
            'backupCount': 2,
            'formatter': 'default',
        },
        'information': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'information.log',
            'backupCount': 2,
            'formatter': 'default',
        },
    },
    'loggers': {
        'logger1': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'logger2': {
            'handlers': ['information'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

logging.config.dictConfig(LOGGING)