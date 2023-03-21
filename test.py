import os
import logging
import logging.config

wd = os.path.dirname(__file__)
conf_path = os.path.join(wd, 'logging.conf')

# seting everything by read config file
logging.config.fileConfig(conf_path)

app_logger_name = 'applog'

# get root logger
root_logger = logging.getLogger()
# get self-defined app logger
app_logger = logging.getLogger(app_logger_name)


# logging: root logger
root_logger.debug(" [root logger] This is debug log")
root_logger.info(" [root logger] This is info log")
root_logger.warning(" [root logger] This is warning log")
root_logger.error(" [root logger] This is error log")
root_logger.critical(" [root logger] This is critical log")

# logging: app logger
app_logger.debug(" [app logger] This is debug log")
app_logger.info(" [app logger] This is info log")
app_logger.warning(" [app logger] This is warning log")
app_logger.error(" [app logger] This is error log")
app_logger.critical(" [app logger] This is critical log")

# export all python system error info
a = 'abc'
try:
    int(a)
except Exception as e:
    # app_logger.error(e)
    app_logger.exception(e)
    
    
app_logger.info(" [app logger] Program Finished!")

# logging.basicConfig(format="%(asctime)s | %(levelname)-8s | %(filename)s : %(lineno)s | %(message)s",
#                     datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
# # logging.basicConfig(format="%(asctime)s | %(levelname)s | %(filename)s : %(lineno)s | %(message)s",
# #                     level=logging.DEBUG)

# name = "ZhangSan"
# age = 18

# logging.debug("Name: %s, Age: %d", name, age)
# logging.warning("Name: %s, Age: %d", name, age)


# import logging

# logging.basicConfig(level=logging.DEBUG)

# name = "ZhangSan"
# age = 18

# logging.debug("Name: %s, Age: %d", name, age)
# logging.debug("Name: %s, Age: %d" % (name, age))
# logging.debug("Name: {}, Age: {}".format(name, age))
# logging.debug(f"Name: {name}, Age: {age}")


# print("this is print log")

# logging.basicConfig(level=logging.DEBUG)
# # logging.basicConfig(filename='demo.log', leve1=logging.DEBUG)
# # logging.basicConfig(filename='demo.log', filemode='w',leve1=logging.DEBUG)

# logging.debug("This is debug log")
# logging.info("This is info log")
# logging.warning("This is warning log")
# logging.error("This is error log")
# logging.critical("This is critical log")


# logging.basicConfig(leve1=logging.DEBUG)

# name = "3&3"

# age = 18

# logging.debug("i'$f§ 96$, Ei-fi—t» Pad", name, age)
# logging.debug("i}$:§3 Pas, E523 96d" 95 (name, age))
# logging.debug("f‘&~'§ {}, EEi—Ii {}".format(name, age))
# logging.debug(f"35££% {name}, 325% {age}")
