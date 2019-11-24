import datetime
import time
import tempfile
import os


"""Declaring global variables for logger"""
TEMPDIR = tempfile.gettempdir()
TEMP_LOG_FOLDER = os.path.join(TEMPDIR, "DUKE")
DEBUG = True  # If True log will get printed on the shell.
WRITE_LOG = True  # If True log will get written in TEMP_LOG_FOLDER.


def log(typ="INFO", msg="No Msg"):
    """This function prints provided msg with date stamp.
    Args:
        typ (str): type of the message.
        msg (str): Text to print as message.

    Returns:
        (str): Returns date stamp formatted text in string.
    """
    temp_log_file = os.path.join(TEMP_LOG_FOLDER, "{}.log".format(
        datetime.datetime.now().date()))
    now = time.time()
    timestamp = datetime.datetime.fromtimestamp(now).strftime(
        '%Y-%m-%d %I:%M %p')
    string_ = "{} : {} : {}".format(typ, timestamp, msg)
    if DEBUG:
        print(string_)
    if WRITE_LOG:
        try:  # using "try" to avoid permission errors on end user machines!
            if not os.path.exists(os.path.join(TEMP_LOG_FOLDER)):
                os.makedirs(os.path.join(TEMP_LOG_FOLDER))
            with open(temp_log_file, "a") as rp:
                rp.write("{}\n".format(string_))
        except Exception as err:
            print("ERROR : While writing a log to path {}".format(temp_log_file))
            print("ERROR : msg : {}".format(err))
    return string_
