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
    __name          = "__logger_event__"
    __level         = logging.DEBUG
    __filepath      = "./logs/app.log"
    __format        = "[%(levelname)8s] <%(asctime)s> %(filename)s:%(lineno)d - %(message)s"
    __logHandler    = None
    __logFormater   = None
    __logger        = None

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
    __name      = "__logger_event__"
    __level     = logging.DEBUG
    __filepath  = "./logs/events.log"
    __format    = "[%(levelname)8s] <%(asctime)s> - %(message)s"

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

    CBotAppLogger().info("Test EVENT log")
    CBotAppLogger().debug("Test EVENT log")
    CBotAppLogger().warning("Test EVENT log")
    CBotAppLogger().error("Test EVENT log")
    CBotAppLogger().critical("Test EVENT log")


### EOF ###