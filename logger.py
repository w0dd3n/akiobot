#!/usr/bin/python3
#coding: utf-8

###
### @DESCRIPTION
### Logger module defines loggers, handlers and formatters of app
### appLogger provides logs for development purpose
### eventLogger provides logs for user activities
###
### To use 'from logger import appLogger/eventLogger'
###
### @LICENCE= CC BY NC 2021
###
### @DOCS - https://docs.python.org/3/howto/logging.html
### @DOCS - https://docs.python.org/3.8/howto/logging-cookbook.html#logging-cookbook

### TODO - Add file rotation feature

### Import Standard Modules
import logging

### MODULE CONSTANTS
###
LOG_NAME_EVENT      = "__logger_event__"
LOG_LEVEL_EVENT     = logging.DEBUG
LOG_FILE_EVENT      = "./logs/events.log"
LOG_FORMAT_EVENT    = "[%(levelname)8s] <%(asctime)s> - %(message)s"

LOG_NAME_APP        = "__logger_app,__"
LOG_LEVEL_APP       = logging.DEBUG
LOG_FILE_APP        = "./logs/app.log"
LOG_FORMAT_APP      = "[%(levelname)8s] <%(asctime)s> %(filename)s:%(lineno)d - %(message)s"

LOG_DATE_FMT        = "%d/%m/%Y %H:%M:%S"


# define a Handler which writes INFO messages or higher to the sys.stderr
# define Handlers which write INFO messages or higher to appropriate LOG_FILE_...
eventLogHandler = logging.FileHandler(LOG_FILE_EVENT, mode='a', encoding='utf-8')
appLogHandler = logging.FileHandler(LOG_FILE_APP, mode='a', encoding='utf-8')

# define default logging level to be used
eventLogHandler.setLevel(LOG_LEVEL_EVENT)
appLogHandler.setLevel(LOG_LEVEL_APP)

# set a format for each handler
eventFormatter = logging.Formatter(LOG_FORMAT_EVENT)
eventLogHandler.setFormatter(eventFormatter)
appFormatter = logging.Formatter(LOG_FORMAT_APP)
appLogHandler.setFormatter(appFormatter)

# add handlers to the root logger
logging.getLogger(LOG_NAME_EVENT).addHandler(eventLogHandler)
logging.getLogger(LOG_NAME_APP).addHandler(appLogHandler)

# Now, define a couple of other loggers 
appLogger = logging.getLogger(LOG_NAME_APP)
appLogger.setLevel(LOG_LEVEL_APP)
eventLogger = logging.getLogger(LOG_NAME_EVENT)
eventLogger.setLevel(LOG_LEVEL_EVENT)

