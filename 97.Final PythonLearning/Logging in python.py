'''logging module is used for loggin purprose'''
import  logging
'''and it will give same object'''
'''if we need to set some configuraton that need to done before getting the logger
There various level of logging
1.Debug
2.Info
3.Warning Default
4.Error
5.Critical
Also we can create logger by any name buts its a good practice if we can create logger using 
module name __name__
also if we use logger name like database.query then here it will create a sub logger which inherit from 
database so it will use the configuration define in database until it is override
there are handler for logger which we can use
let see in example
'''
'''logging.basicConfig(
    level=logging.DEBUG
)'''
'''We can format the message as'''
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s:%(message)s" 
    '''for maximum readbility the format is
    %(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s
    ''',
    filename="logger.txt"
)

logger=logging.getLogger('test_logger') # we can give any name we want here we can access it across differnt file
'''Here the test logger will be inherit from root logger'''
logger.info("Please see the info message")
logger.warning("Please see warning message")
logger.debug("Please see the debug message")
logger.error("Please see the error message")
logger.critical("Please see the critical mesaage")
'''you can write the logging message to file instead of console by specifying file name'''
logger.info("This is the formatted Message")

'''Always specify config before getting the logger otherwise chages will not work'''

'''There are handle for logger which we can use if needed'''