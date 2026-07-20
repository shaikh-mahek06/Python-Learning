import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug Message")
logging.info("Program Started")
logging.warning("Low Disk Space")
logging.error("File Not Found")
logging.critical("System Crash")

# Question 2: Save Logs to a File
print(" Question 2: Save Logs to a File")
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program Started")
logging.warning("Warning Message")
logging.error("Something went wrong")

# 3.Handle division by zero and log the error.
print("3.Handle division by zero and log the error.")
logging.basicConfig(level=logging.ERROR)
try:
    a=7
    b=0
    print(a/b)
except ZeroDivisionError:
    logging.error("can not possible")

# 4.Log the actual exception message.
print(" 4.Log the actual exception message.")
import logging
logging.basicConfig(level=logging.INFO)
try:
    a=70
    b=0
    print(a/b)
except Exception as e:
    logging.error(e)

# 5.Log the complete traceback.

logging.basicConfig(level=logging.ERROR)

try:
    print(10 / 0)

except Exception:
    logging.exception("An Exception Occurred")
    