from .dev import DevelopmentConfig
from .production import ProductionConfig
from .pre_production import PreProductionConfig


config = {
    'development': DevelopmentConfig,
    'pre-production': PreProductionConfig,
    'production': ProductionConfig
}