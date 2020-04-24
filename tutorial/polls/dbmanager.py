import mysql.connector


class DbManager:
    __instance = None
    __dbconnection = None
    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
            cls.__dbconnection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd='Cakeman345',  # "mypassword",
                auth_plugin='mysql_native_password',
                database="university",
            )
        return cls.__instance

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    def getConnection(self):
        if self.__instance is None:
            self.instance()
        return self.__dbconnection

    def __del__(self):
        self.__dbconnection.close()