from flask_jwt_extended import JWTManager

JWT = JWTManager()
BLACKLIST = set()


@JWT.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in BLACKLIST
