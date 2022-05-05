# JSON Web Tokens (JWT)

In the repository, I demo the core idea of how JWT works. In the regular procedure of requests, clients connect to the server, the session is established on the server and its content is also saved by the session ID. On the other hand, the client side may have cookie. However such mechanism is expensive and less efficient especially on many requests. 

JWT is one of solutions of the above. In addition, it also keeps the real stateless, like how the Restful API works. The general idea is like the below flow. The first step is the same to the regular. The client login a authentication server with the username and the password. The server would check the user information. If it is validated, the server would send back a JWT back to the client (`authenticate and generate signature`). After that, every operation the client sends to the server must carry the JSON Web Tokens instead of the regular mechanism of sessions and cookies.

![](doc/jwt.png)
Refer to the [link](https://medium.com/mr-efacani-teatime/%E6%B7%BA%E8%AB%87jwt%E7%9A%84%E5%AE%89%E5%85%A8%E6%80%A7%E8%88%87%E9%81%A9%E7%94%A8%E6%83%85%E5%A2%83-301b5491b60e) (2022).

Next, let's have a look at the components of JWT.

- `Header` defines the kind of algorithms generating the signature and token types.
- `Payload` defines the necessary information of the request, like the user name, operation, tmiestamp, etc.
- `Signature` the information of both `Header` and `Payload` to the hash code by using the private key. The format is like `base64(Header) + base64(Payload) + base64(Signature)`.

In the following, I demo how to generate the JSON Web Token on Python.

```py
priKey = """-----BEGIN PRIVATE KEY----------END PRIVATE KEY-----"""

currentTime = int(datetime.datetime.now().strftime("%s"))

headers = json.dumps({"alg": "HS256", "typ": "JWT"})
payload = json.dumps({"iss": "jiankaiwang",
                      "sub": "updating-db",
                      "aud": "db-server",
                      "exp": currentTime + 60*10,
                      "timestamp": currentTime})

unsignedToken = EncodeBase64(ToBytes(headers)) \
                + ToBytes('.') \
                + EncodeBase64(ToBytes(payload))
signature = CreateSHA256Sign(priKey, unsignedToken)

JWTTOKEN = unsignedToken.decode("utf-8") \
           + '.' \
           + signature.decode("utf-8")
```

In the Payload, there are several standard fields you have to fill.

- `iss`: issuer, the JWT publisher
- `sub`: subject of JWT
- `aud`: audience of JWT, the JWT receiver
- `exp`: expiration time
- `nbf`: not before time
- `iat`: issued at time
- `jti`: JWT ID

## How to start

```sh
python3 -m virtualenv -p python3 env
source ./env/bin/activate
pip3 install --no-cache-dir ./environ/requirements.txt
python3 requests.py
```

The result is like:
```text
Headers:
{"alg": "HS256", "typ": "JWT"}

Payload:
{"iss": "jiankaiwang", "sub": "updating-db", "aud": "db-server", "exp": 1651760527, "timestamp": 1651759927}

JWT:
eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJpc3MiOiAiamlhbmthaXdhbmciLCAic3ViIjogInVwZGF0aW5nLWRiIiwgImF1ZCI6ICJkYi1zZXJ2ZXIiLCAiZXhwIjogMTY1MTc2MDUyNywgInRpbWVzdGFtcCI6IDE2NTE3NTk5Mjd9.aMXv8unaaUfL2NMxQduVYJ-nsHlLpLX4GsK0f6gE_5M
```

Next you can verify the JWT token by `JWT.io`.

![](./doc/jwt.io.png)
