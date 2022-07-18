import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration/config.ini")  # giving path to the configuration file


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def getUserPassword():
        password = config.get("common info", "password")
        return password
