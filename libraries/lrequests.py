import requests
from lispy.error import lispy_function

@lispy_function("lrequests:get", ["str"])
def lrequests_get(args):
    return requests.get(args[0])

@lispy_function("lrequests:get:headers", ["str", "dict"])
def lrequests_get_headers(args):
    return requests.get(args[0], headers=args[1])

@lispy_function("lrequests:post", ["str", "dict"])
def lrequests_post(args):
    return requests.post(args[0], payload=args[1])

@lispy_function("lrequests:statuscode", ["Response"])
def lrequests_statuscode(args):
    return args[0].status_code

@lispy_function("lrequests:headers", ["Response"])
def lrequests_headers(args):
    return args[0].headers

@lispy_function("lrequests:encoding", ["Response"])
def lrequests_encoding(args):
    return args[0].encoding

@lispy_function("lrequests:text", ["Response"])
def lrequests_text(args):
    return args[0].text

@lispy_function("lrequests:json", ["Response"])
def lrequests_json(args):
    return args[0].json()


module = {
    "lrequests:get": lrequests_get, "lrequests:get:headers": lrequests_get_headers, "lrequests:post": lrequests_post, "lrequests:statuscode": lrequests_statuscode, 
    "lrequests:headers": lrequests_headers, "lrequests:encoding": lrequests_encoding, "lrequests:text": lrequests_text, "lrequests:json": lrequests_json
}