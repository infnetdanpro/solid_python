
db_session = ...


# The Single-responsibility principle: "There should never be more than one reason for a class to change."
# In other words, every class should have only one responsibility.
# Here class has mixed logic with database, this is bad :)
class User:
    def __init__(self, name: str, surname: str):
        self.db_conn = db_session()
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def save_in_db(self):
        pass


# Good
# Split logic to basic class and class for work with user in DB
class BaseUser:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name


class UserModelDB:
    def get_username_from_db(self, user_id: int):
        pass

    def save_in_db(self, user: dict):
        pass


class User(BaseUser, UserModelDB):
    ...
