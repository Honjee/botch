from api_calls.base import baseURL
from api_calls.base import buildQueryParams
from api_calls.credentials import client_id
from api_calls.credentials import client_secret

def oauth(req):
    resp = buildQueryParams(req)
    resp.client_id = client_id
    resp.client_secret = client_secret
    print("ouaht fuucnt")
    return resp
