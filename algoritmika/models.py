

class User:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password
        self.access_token = None
        self.refresh_token = None


user = User(name='Alex', login='login', password='password')

