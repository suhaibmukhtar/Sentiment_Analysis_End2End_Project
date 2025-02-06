import sys
from logger import logging
import os

import sys
import logging

#this is called when exception occurs in our code and to handle that this function is used
#error_detail: Accepts the sys module to use its exc_info() function, which is required to get 
# detailed exception information.
def error_message_details(error_message, error_detail:sys):
    #returns three Exception type, exception message, traceback object where error occured in code
    exc_type,exc_value,exc_tb=error_detail.exc_info()
    exception_type=exc_type
    exception_msg=exc_value
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    function_name=exc_tb.tb_frame.f_code.co_name
    error_message=f"Excetion Type is: {exception_type},\nException message is: {exception_msg}. \nException has occured in File: {file_name}, \nLine no: {line_number},\nName of function: {function_name}"
    logging.info(error_message)
    return error_message

class CustomException(Exception): #receives custom exception as input
    def __init__(self, error_message, error_details:sys): #error details is sys library
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_details)
    
    def __str__(self):
        return self.error_message #when exception obj called returns the error message detailed


if __name__=="__main__":
    logging.info("Started the Project pipeline")
    try:
        a=1/0
        logging.info("Division By Zero error")
    except Exception as e:
        raise CustomException(e,sys)