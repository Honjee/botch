from api_calls.base import baseURL
from api_calls.base import buildQueryParams

def oauth(req):
    resp = buildQueryParams(req)
    print(resp)
