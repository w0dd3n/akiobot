#!/usr/bin/python3
#coding: utf-8

###
### @DESCRIPTION
### BotWebManagementService provide service level daemon to handle
### web interface service for local management purpose only
### Service is to be started and stopped from Service Engine
###
### @LICENCE= CC BY NC 2021
###

from http.server import BaseHTTPRequestHandler, HTTPServer

from botLogger import CBotAppLogger, CBotEventLogger

### Constants
SERVER_HOSTNAME     = "localhost"
SERVER_PORT         = 8080
SERVER_VERSION      = "Akiobot Manager"
SYS_VERSION         = "Python 3.x"


class CBotWebManService:

    def __init__(self) -> None:
        self.__serverHandler = None

    def startService(self):
        CBotAppLogger().info("Starting web management service")
        
        if self.__serverHandler != None:
            self.__serverHandler.server_close()
        
        self.__serverHandler = HTTPServer((SERVER_HOSTNAME, SERVER_PORT), CBotHTTPHandler)
        self.__serverHandler.serve_forever()

        CBotAppLogger().info("Web Management Service is RUNNING")

    def stopService(self):
        CBotAppLogger().info("Stopping Web Management Service")

        if self.__serverHandler != None:
            self.__serverHandler.server_close()
        else:
            CBotAppLogger.error("Web Management Service already stopped")

        CBotAppLogger().info("Web Management Service is STOPPPED")

class CBotHTTPHandler(BaseHTTPRequestHandler):

    ### TODO - Define & Implement PATH Handlers
    ### TODO - Implement Jinja2 HTML Templates
    def do_GET(self):

        CBotEventLogger().info("HOST - " + str(self.client_address) + " - " + self.requestline)

        self.server_version = SERVER_HOSTNAME
        self.sys_version = SYS_VERSION

        self.send_response_only(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Akiobot Web Werver</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>UNDER CONSTRUCTION</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

### TODO - CBotWeblogicConfig - To be implemented
class CBotWeblogicConfig:
    """
    Implement business logic for configuration management
    such as Wi-Fi, etc.
    """

    def __init__(self) -> None:
        pass

### TODO - CBotWeblogicDirectory - To be implemented
class CBotWeblogicDirectory:
    """
    Implement business logic for user data configuration
    such as contacts, reminders, etc.
    """

    def __init__(self) -> None:
        pass