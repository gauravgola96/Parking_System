import logging, os, sys
from config import config

#Loading class config according to ENV var
config_name = os.environ.get('PARKING_SYSTEM_ENV', 'development')
current_config = config[config_name]

#Logger Settings
package_name = '.'.join(__name__.split('.')[:-1])
root_logger = logging.getLogger(package_name)
console_handler = logging.StreamHandler(sys.stdout)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)
root_logger.setLevel(current_config.LOG_LEVEL)
