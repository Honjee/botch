from flask import make_response

baseURL = 'https://discordapp.com/api'

def buildQueryParams(req):
    resp = make_response()
    resp.set_cookie('username', 'the username')
    return resp
