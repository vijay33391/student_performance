import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Extract error details like file name and line number where the exception occurred.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the custom exception with detailed error information.
        """
        super().__init__(error_message)
        # Correctly pass the error instead of error_message to get proper details
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

# Main block should be outside the class
'''if __name__ == "__main__":
    try:
        a = 1 / 0  # Simulate a division by zero error
    except Exception as e:
        logging.info("Division by zero occurred")
        raise CustomException(e, sys)'''
