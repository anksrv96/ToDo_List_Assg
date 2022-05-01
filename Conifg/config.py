class TestData:
    USERNAME = "A"
    EMAIL = "a@b.com"
    PASSWORD = "12345678"
    AGE = 25
    BEARER_TOKEN = None

    def set_bearer_token(self, token):
        self.BEARER_TOKEN = token
