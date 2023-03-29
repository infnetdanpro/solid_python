# The Dependency inversion principle: "Depend upon abstractions, [not] concretions."

class Connector:
    conn = None

    def connect(self):
        return self.conn


# bad
class AuthForUser:
    def __init__(self, connector: Connector):
        self.connection = connector.connect()

    def authenticate(self, credential):
        pass

    def is_authenticate(self):
        pass

    def last_login(self):
        pass


class AnonymousAuth(AuthForUser):
    pass


class GitHubAuth(AuthForUser):
    def last_login(self):
        # do request
        pass


class FacebookAuth(AuthForUser):
    pass


class Permission:
    def __init__(self, auth: AuthForUser):
        self.auth = auth

    def has_permission(self):
        pass


class IsLoggedInPermission(Permission):
    def last_login(self):
        return self.auth.last_login()
