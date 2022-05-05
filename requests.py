# -*- coding: utf-8 -*-

import logging
import datetime
import base64
import hmac
import hashlib
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s-%(levelname)s: %(message)s')

# In[]

def ToBytes(string):
  return bytes(string, 'utf-8')

def EncodeBase64(message):
  return base64.urlsafe_b64encode(message).replace(b'=', b'')

def CreateSHA256Sign(key, unsignedMessage):
  signaturedMessage = hmac.new(\
    ToBytes(key), unsignedMessage, digestmod=hashlib.sha256).digest()
  return EncodeBase64(signaturedMessage)

# In[]

if __name__ == '__main__':

  priKey = """-----BEGIN PRIVATE KEY----------END PRIVATE KEY-----"""

  currentTime = int(datetime.datetime.now().strftime("%s"))

  headers = json.dumps({"alg": "HS256", "typ": "JWT"})
  payload = json.dumps({"iss": "jiankaiwang",
                        "sub": "updating-db",
                        # "aud": "db-server",
                        "exp": currentTime + 60*10,
                        "timestamp": currentTime})

  unsignedToken = EncodeBase64(ToBytes(headers)) + ToBytes('.') + EncodeBase64(ToBytes(payload))
  signature = CreateSHA256Sign(priKey, unsignedToken)

  JWTTOKEN = unsignedToken.decode("utf-8") + '.' + signature.decode("utf-8")

  print("Secret:")
  print(priKey)

  print("\nHeaders:")
  print(headers)

  print("\nPayload:")
  print(payload)

  print("\nJWT:")
  print(JWTTOKEN)
