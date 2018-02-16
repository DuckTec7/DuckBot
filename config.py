import os

class Config(object):
    SECRET_KEY = 'my_secret_token'
    PAGE_ACCESS_TOKEN = 'EAAZAzuQsZCExUBAA7cZCzjpLj489WrosYygFZC91Gcibkbm36qaoWXlnVBa52bKRW5lGl4ZB95InazzIxAMk4i8jznsH59EQmRqvS6OOotkSjr2LxuwHwTRhtHodPrLCGsSbrTm11BZCvCSmlsYTfGe47U2KdZAZARW62aZCXFlGlJgZDZD'

class DevelopmentConfig(Config):
    DEBUG = True
