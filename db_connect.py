import oracledb


class DbConnect:
    """Class for connecting to database"""

    def __init__(self) -> None:
        pass

    def getConnection(user, user_pwd, dns):
        """Return connection to databse"""

        connection = oracledb.connect(
            user=user, password=user_pwd, dsn=dns)

        return connection
