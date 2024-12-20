# gunicorn

# APP_MODE="local"
# APP_MODE="production"

import os

from dotenv import load_dotenv

load_dotenv(".env")

def app(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain; charset=utf-8")
    ]
    app_mode=os.environ.get("APP_MODE")
    print(app_mode)
    secret=os.environ.get("SECRET")
    print(secret)
    start_response(status, headers)
    return [b"Hello, WSGI World"]