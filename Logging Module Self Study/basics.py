import logging 
logging.basicConfig(filename="Logs.txt",format="%(asctime)s %(levelname)s %(message)s")
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("This is a Debug Message")