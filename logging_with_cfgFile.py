from logging.config import fileConfig
import logging

fileConfig('log.cfg', defaults={'logfilename': '/var/log/mylog.log'})
logger = logging.getLogger('sLogger')

logger.debug("hey")
logger.critical("crashed")
logger.info("information")
