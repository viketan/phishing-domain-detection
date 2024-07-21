from src.logger import logging
from src.exception import CustomException
import os,sys

def main():
    try:
        logging.info("Iniated main function excution")
    except Exception as e:
        logging.error(f"Error occured in main :{e}")
        raise CustomException(e,sys)

if __name__=="__main__":
    main()