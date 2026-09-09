from models.user import User

class UserRepository:

    def __init__(self, db):
        self.__db = db

    def add(self, user: User):
        self.__db.add(user)
        self.__db.flush()
        return user
    