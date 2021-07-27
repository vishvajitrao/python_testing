# Logging is the process of tracking the event when software runs.Logging is one of the most important concept for software develop, debugging and running.
# Levels of the message

# 1. Debug:- This is the used to get details information.
# 2 warning:-This is used to indicate something unexpected happen in the application.
# 3 info:- This is used when something work properly
# 4 error:- This is used when error occur in the software
# 5 critical:- This tells serious errors.

# All the level has corresponding numeric value

# notset-0
# debug-10
# info-20
# warning-30
# error-40
# critical-50

import logging


# create logger

# log = logging.Logger("my-logger")
# logger = logging.getLogger(log.name)
#
# # set log level
# logger.setLevel(logging.INFO)
#
# # Define file handler and set formatter
# handler = logging.FileHandler("logging.log", mode="w")
#
# formatter = logging.Formatter(fmt='%(asctime)s - %(message)s - %(name)s')
# handler.setFormatter(fmt=formatter)
#
# # add file handler to the logger
# logger.addHandler(handler)
#
# logger.debug('A debug message')
# logger.info('An info message')
# logger.warning('Something is not right.')
# logger.error('A Major error has happened.')
# logger.critical('Fatal error. Cannot continue')

# set up logging using basicConfig()
# We can also setup logging using basicConfig() method.info(), debug(), error(), critical() and warning() automatically call the basicConfig() function if the handler not defined


logging.basicConfig(filename="logging1.log", filemode="w",
                    format='%(asctime)s - %(message)s - %(name)s - Level no :- %(levelno)s',level=logging.DEBUG)


# logging.debug('A debug message')
# logging.info('An info message')
# logging.warning('Something is not right.')
# logging.error('A Major error has happened.')
# logging.critical('Fatal error. Cannot continue')


# print message on console

logs = logging.Logger("Vishvajit")
log = logging.getLogger(logs.name)
log.debug('A debug message')
log.info('An info message')
log.warning('Something is not right.')
log.error('A Major error has happened.')
log.critical('Fatal error. Cannot continue')
