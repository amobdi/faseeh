import logging
import time
import fasseh
import os

# create logger
logger = logging.getLogger('fasseh')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
logDir = 'logs'
if not os.path.exists(logDir):
    os.makedirs(logDir)
fh = logging.FileHandler(logDir + '/' + time.strftime("%Y%m%d-%H%M%S"))
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'
                              '(line %(lineno)s in %(name)s)')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
