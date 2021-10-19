#!/usr/bin/python3
#coding: utf-8

###
### @DESCRIPTION
### BotServiceEngine handles the overall lifecycle of the bot services
### Implementing Singleton Design Pattern
###
### TODO - Describe services implemented
###
### @LICENCE= CC BY NC 2021
###

import time

from botLogger import CBotAppLogger
from botWebManagementService import CBotWebManService


class CBotServiceEngine:

    def __init__(self) -> None:
        self.__webfrontServiceHandler = CBotWebManService()
        self.__speechServiceHandler = None
        self.__messagingServiceHandler = None

    def startEngine(self):
        CBotAppLogger().info("Starting Bot Service Engine")

        self.__webfrontServiceHandler.startService()
        
        ### TODO - Start messagging service
        ### TODO - Start speeching service

        CBotAppLogger().info("Bot Service Engine is up and running")



    def stopEngine(self):
        CBotAppLogger().info("Stopping Bot Service Engine")

        self.__webfrontServiceHandler.stopService()

        ### TODO - Stop speeching service
        ### TODO - Stop web management interface

        CBotAppLogger().info("Stopping Bot Service Engine")


# sample use case
if __name__ == "__main__":
    botServiceEngine = CBotServiceEngine()
    botServiceEngine.startEngine()
    time.sleep(60)
    botServiceEngine.stopEngine()
    del botServiceEngine


### EOF ###