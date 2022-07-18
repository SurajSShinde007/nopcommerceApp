import logging

class LogGen:
    @staticmethod
    def logegn():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%m(asctime)s: %(levelname)s: %(messege)s',datefmt='%m/%d/%Y %I:%M:%S %P')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

# to get log use logger as a object and write in the test case where it is required
