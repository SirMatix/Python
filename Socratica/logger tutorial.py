import logging

#create and configure logger
LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = 'Logons.log',
                    level = logging.DEBUG,
                    #format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()
# root logger is basic logger without a name

#test the logger

logger.info('second message.')
print(logger.level)

