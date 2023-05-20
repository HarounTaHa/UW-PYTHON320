# simple.py
# def my_fun(n):
#     for i in range(0, n):
#         print(i)  # <-- Add this line
#         100 / (50 - i)
#
#
# if __name__ == "__main__":
#     my_fun(100)
#
# ---------------------------------------------
# import logging
#
# logging.basicConfig(level=logging.WARNING)
#
#
# def my_fun(n):
#     for i in range(0, n):
#         logging.debug(i)
#         if i == 50:
#             logging.warning("The value of i is 50.")
#         try:
#             100 / (50 - i)
#         except ZeroDivisionError:
#             logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))
#
#
# if __name__ == "__main__":
#     my_fun(100)

# import logging
#
# log_format = "%(asctime)s %(filename)s:%(lineno)-4d %(levelname)s %(message)s"  # Add/modify these
# logging.basicConfig(level=logging.WARNING, format=log_format, filename='mylog.log')
#
# def my_fun(n):
#     for i in range(0, n):
#         logging.debug(i)
#         if i == 50:
#             logging.warning("The value of i is 50.")
#         try:
#             100 / (50 - i)
#         except ZeroDivisionError:
#             logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))
#
# if __name__ == "__main__":
#     my_fun(100)

# import logging
#
# log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
#
# # BEGIN NEW STUFF
# # Create a "formatter" using our format string
# formatter = logging.Formatter(log_format)
# # Create a log message handler that sends output to the file 'mylog.log'
# file_handler = logging.FileHandler('mylog.log')
# # Set the formatter for this log message handler to the formatter we created above.
# file_handler.setFormatter(formatter)
# # Get the "root" logger. More on that below.
# logger = logging.getLogger()
# # Add our file_handler to the "root" logger's handlers.
# logger.addHandler(file_handler)
#
#
# # END NEW STUFF
#
# def my_fun(n):
#     for i in range(0, n):
#         logging.debug(i)
#         if i == 50:
#             logging.warning("The value of i is 50.")
#         try:
#             i / (50 - i)
#         except ZeroDivisionError:
#             logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))
#
#
# if __name__ == "__main__":
#     my_fun(100)
#
# import logging
#
# log_format = "%(asctime)s %(filename)s:%(lineno)-3d %(levelname)s %(message)s"
#
# formatter = logging.Formatter(log_format)
#
# file_handler = logging.FileHandler('mylog.log')
# file_handler.setLevel(logging.WARNING)  # Add this line
# file_handler.setFormatter(formatter)
#
# console_handler = logging.StreamHandler()  # Add this line
# console_handler.setLevel(logging.DEBUG)  # Add this line
# console_handler.setFormatter(formatter)  # Add this line
#
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)  # Add this line
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)  # Add this line
#
#
# def my_fun(n):
#     for i in range(0, n):
#         logging.debug(i)
#         if i == 50:
#             logging.warning("The value of i is 50.")
#         try:
#             i / (50 - i)
#         except ZeroDivisionError:
#             logging.error("Tried to divide by zero. Var i was {}. Recovered gracefully.".format(i))
#
#
# if __name__ == "__main__":
#     my_fun(100)


# =============================================Debugging =============================================

def my_fun():
    for i in range(1, 500):
        print(i)
        123 / (50 - i)


if __name__ == '__main__':
    my_fun()
