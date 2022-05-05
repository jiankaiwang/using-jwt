# -*- coding: utf-8 -*-

import logging
import jwt
import datetime
import base64
import hmac
import hashlib
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(levelname)s: %(message)s')

# In[]

if __name__ == '__main__':

  priKey = """-----BEGIN PRIVATE KEY----------END PRIVATE KEY-----"""
  JWToken = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJpc3MiOiAiamlhbmthaXdhbmciLCAic3ViIjogInVwZGF0aW5nLWRiIiwgImV4cCI6IDE2NTE3NjI0NjksICJ0aW1lc3RhbXAiOiAxNjUxNzYxODY5fQ.idNJ1tF6JzPtZMsC5dMlRK0HO-dI3sTBRvl9JbJrpxY"

  if len(JWToken) < 1:
    currentTime = int(datetime.datetime.now().strftime("%s"))

    headers = {"alg": "HS256", "typ": "JWT"}
    payload = {"iss": "jiankaiwang",
              "sub": "updating-db",
              "exp": currentTime + 60*10,
              "timestamp": currentTime}  

    JWToken = jwt.encode(payload=payload, key=priKey, algorithm="SH256", headers=headers)
  else:
    print("* You can generate JWT from requests.py. *")
  
  print("JWT:")
  print(JWToken)

  try:
    info = jwt.decode(jwt=JWToken, key=priKey, verify=False, algorithms="HS256")
    print("Info:")
    print(info)
  except Exception as err:
    print("Error:")
    print(err)
