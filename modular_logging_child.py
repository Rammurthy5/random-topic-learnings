from modular_logging import logging

logging.getLogger('logger1').info("hey there!")
logging.getLogger('logger1').debug("hey debug!")
logging.getLogger('logger1').error("hey error!")
logging.getLogger('logger1').warning("hey warn!")
logging.getLogger('logger2').error("hey logger2")