#!/usr/bin/env python
#dummy comment
from app import app
SECRET_KEY = 'SuperSecretString'
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
