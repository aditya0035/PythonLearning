"""
Logging Module is used to print things out
they can print things on console window or in a file
used by developer for logs purpose on production environment
there are various level of logger
logging comes with python installation but not a global module we need to import that before using that
import logging
for a module the logging configuration are defined once that is once we get the logger instance then it will work
on that configuration although we can give any name to logger every time we called it
there is one logger instance throughout a directory
if no additional configuration are specified it will run with default configuration
"""
#import logging

#logger=logging.getLogger("Logger Name")
"""
Here in logger Name we can give any name but its a good practice to use __name__ so that easy to track for error
also if we give name like database.Query the it will create a logger instance which will inherit configuration 
from parent logger which is database
by default the logger Name is inherit from root logger
There are various level of logging in python
1.Debug
2.Info
3.Warning 
4.Error 
5.Critical
Default level is set to Warning level
Once a config is set and instance is created we can't change the configuration after that if we try to change it it will
not reflected
To set configuration we need to call logging.basiccnfig()
in basic config we can set the logging level
File if need to save to the file
The message format how to save the file search for descriptive message format for logging

"""

import  logging

#logging.basicConfig(level=logging.DEBUG,filename="xyz.txt",format="%(asctime)s %(levelname)s: %(message)s")
#here s for string and d for digit
#logger=logging.getLogger(__name__)
#logging.debug("Hello Logging")

"""
Maximum Readability Configurations
%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s
"""
maximum_readbility_format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.DEBUG,filename="xyz.txt",format=maximum_readbility_format)
logger=logging.getLogger(__name__)
logging.debug("Hello Logging")

"""
Each time we run a module it does not create a new file it append the content to that file
also we can put handler for logging 
apart from that there is dateformat paramter to define date format for message logging
"""