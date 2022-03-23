import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(filename)s.%(funcName)s: %(message)s'
        },
        'json': {
            'format': '%(asctime)s %(name)s %(levelname)s %(filename)s %(funcName)s %(message)s',
            'class': 'pythonjsonlogger.jsonlogger.JsonFormatter'
        },
    },
    'handlers': {
        'console': {
            'formatter': 'standard',
            'class': 'logging.StreamHandler'
        },
        'json': {
            'formatter': 'json',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'json': {
            'handlers': ['json'],
            'level': 'INFO',
            'propagate': False
        },
        '': {  # root logger
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False
        },
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

def main():
    logger = logging.getLogger("json")

    logger.info("Info message")

    try:
        raise Exception
    except Exception:
        logger.exception("Error message")


if __name__ == '__main__':
    main()
