#!/usr/bin/python3
#coding: utf-8

###
### @DESCRIPTION
### Logger module defines loggers, handlers and formatters of app
### appLogger provides logs for development purpose
### eventLogger provides logs for user activities
###
### To use 'from botLogger import CBotAppLogger or CBotEventLogger'
###
### @LICENCE= CC BY NC 2021 
###
### @DOCS - https://docs.python.org/3/howto/logging.html
### @DOCS - https://docs.python.org/3.8/howto/logging-cookbook.html#logging-cookbook

### TODO - Add file rotation feature

### Import Standard Modules
import logging

### Define constants for configuration purpose
LOG_NAME_EVENT      = "__logger_event__"
LOG_NAME_APP        = "__logger_app__"
LOG_LEVEL_EVENT     = logging.DEBUG
LOG_LEVEL_APP       = logging.DEBUG
LOG_FILE_EVENT      = "../logs/events.log"
LOG_FILE_APP        = "../logs/app.log"
LOG_FORMAT_EVENT    = "[%(levelname)8s] <%(asctime)s> - %(message)s"
LOG_FORMAT_APP      = "[%(levelname)8s] <%(asctime)s> - %(message)s"


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


### Application Logger for analysis purpose
### Keep track of any useful data for devops team
###
class CBotAppLogger(metaclass=SingletonType):
    __instance      = None
    __name          = LOG_NAME_APP
    __level         = LOG_LEVEL_APP
    __filepath      = LOG_FILE_APP
    __format        = LOG_FORMAT_APP

    def __init__(self) -> None:
        if CBotAppLogger.__instance != None:
            raise("INTERNAL ERROR")
        else:
            CBotAppLogger.__instance = self
            self.__builder()
    
    def __builder(self):
        # define a Handler which writes INFO messages or higher to the sys.stderr
        # define Handlers which write INFO messages or higher to appropriate LOG_FILE_...
        self.__logHandler = logging.FileHandler(self.__filepath, mode='a', encoding='utf-8')

        # define default logging level to be used
        self.__logHandler.setLevel(self.__level)

        # set a format for the handler
        self.__logFormater = logging.Formatter(self.__format)
        self.__logHandler.setFormatter(self.__logFormater)

        # add handlers to the root logger
        logging.getLogger(self.__name).addHandler(self.__logHandler)

        # Now, define a couple of other loggers 
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)

    def debug(self, message):
        self.__logger.debug(message)

    def info(self, message):
        self.__logger.info(message)
    
    def warning(self, message):
        self.__logger.warning(message)

    def error(self, message):
        self.__logger.error(message)    

    def critical(self, message):
        self.__logger.critical(message)   
        

class CBotEventLogger(metaclass=SingletonType):
    __instance  = None
    __name      = LOG_NAME_EVENT
    __level     = LOG_LEVEL_EVENT
    __filepath  = LOG_FILE_EVENT
    __format    = LOG_FORMAT_EVENT

    def __init__(self) -> None:
        if CBotEventLogger.__instance != None:
            raise("INTERNAL ERROR")
        else:
            CBotEventLogger.__instance = self
            self.__builder()
    
    def __builder(self):
        # define a Handler which writes INFO messages or higher to the sys.stderr
        # define Handlers which write INFO messages or higher to appropriate LOG_FILE_...
        self.__logHandler = logging.FileHandler(self.__filepath, mode='a', encoding='utf-8')

        # define default logging level to be used
        self.__logHandler.setLevel(self.__level)

        # set a format for the handler
        self.__logFormater = logging.Formatter(self.__format)
        self.__logHandler.setFormatter(self.__logFormater)

        # add handlers to the root logger
        logging.getLogger(self.__name).addHandler(self.__logHandler)

        # Now, define a couple of other loggers 
        self.__logger = logging.getLogger(self.__name)
        self.__logger.setLevel(self.__level)

    def debug(self, message):
        self.__logger.debug(message)

    def info(self, message):
        self.__logger.info(message)
    
    def warning(self, message):
        self.__logger.warning(message)

    def error(self, message):
        self.__logger.error(message)    

    def critical(self, message):
        self.__logger.critical(message)

# sample use case
if __name__ == "__main__":
    CBotEventLogger().info("Test EVENT log")
    CBotEventLogger().debug("Test EVENT log")
    CBotEventLogger().warning("Test EVENT log")
    CBotEventLogger().error("Test EVENT log")
    CBotEventLogger().critical("Test EVENT log")

    CBotAppLogger().info("Test APP log")
    CBotAppLogger().debug("Test APP log")
    CBotAppLogger().warning("Test APP log")
    CBotAppLogger().error("Test APP log")
    CBotAppLogger().critical("Test APP log")


### EOF ###