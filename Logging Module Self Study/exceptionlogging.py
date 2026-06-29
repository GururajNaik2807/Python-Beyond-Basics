import  logging 
logging.basicConfig(filename="trail.txt",format="%(asctime)s %(levelname)s %(message)s")
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
def checkval(val):
    if val<0:
        raise ValueError(f"Tried to check {val} ,But Number Cannot be Smaller than Zero")
    else:
        logger.info(f"This Value can be proceed further {val} ")
try:
    checkval(-1)
except ValueError as ve:
    logger.error("A error has occured %s",ve)

