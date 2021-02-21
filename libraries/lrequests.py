import requests
from lispy.error import lispy_function

@lispy_function("lrequests:get", ["str"], "Making a request to url")
def lrequests_get(args):
    return requests.get(args[0])

@lispy_function("lrequests:get:headers", ["str", "dict"], "Making a request to url with headers")
def lrequests_get_headers(args):
    return requests.get(args[0], headers=args[1])

@lispy_function("lrequests:post", ["str", "dict"], "Making a request to url with post values")
def lrequests_post(args):
    return requests.post(args[0], payload=args[1])

@lispy_function("lrequests:statuscode", ["Response"], "Getting status code of response")
def lrequests_statuscode(args):
    return args[0].status_code

@lispy_function("lrequests:headers", ["Response"], "Getting header of response")
def lrequests_headers(args):
    return args[0].headers

@lispy_function("lrequests:encoding", ["Response"], "Getting encoding of response")
def lrequests_encoding(args):
    return args[0].encoding

@lispy_function("lrequests:text", ["Response"], "Getting text of response")
def lrequests_text(args):
    return args[0].text

@lispy_function("lrequests:json", ["Response"], "Getting json of response")
def lrequests_json(args):
    return args[0].json()


module = {
    "lrequests:get": lrequests_get, "lrequests:get:headers": lrequests_get_headers, "lrequests:post": lrequests_post, "lrequests:statuscode": lrequests_statuscode, 
    "lrequests:headers": lrequests_headers, "lrequests:encoding": lrequests_encoding, "lrequests:text": lrequests_text, "lrequests:json": lrequests_json
}