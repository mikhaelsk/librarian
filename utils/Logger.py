import logging

class Logger():
    def __init__(self):
        logging.basicConfig( level = logging.DEBUG, filename='test.log', filemode = 'w', format = '%(levelname)-10s [%(asctime)s] %(message)s')
    
    def WriteToLog(self, lineTxt):
        logging.debug(lineTxt)
    
    
