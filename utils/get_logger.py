import logging


def get_logger(namespace: str) -> logging.Logger:
    """Generic utility function to get logger object with fixed configurations"""
    logger = logging.getLogger(namespace)
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)
    logging.addLevelName(logging.ERROR, "error")
    logging.addLevelName(logging.WARNING, "warning")
    logging.addLevelName(logging.INFO, "info")
    logging.addLevelName(logging.DEBUG, "debug")
    logger.addHandler(logging.NullHandler())
    return logger
