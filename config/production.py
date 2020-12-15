from .common import Config
import logging


class ProductionConfig(Config):
    LOG_LEVEL = logging.INFO
