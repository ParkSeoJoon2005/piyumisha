class Config(object):
    LOGGER = True
    API_ID = int("api_id")
    API_HASH = "api_hash"
    TOKEN = "token"

class Development(Config):
    TEST_DEVELOP = True
    LOGGER = True
