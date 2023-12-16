from flask import session, redirect
from functools import wraps


def authenticate(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #CHECK IF USER IS LOGGED IN
        if not session.get("LOGGED_USER"):
            return redirect("/auth")
        
        return fn (*args, **kwargs)
    return wrapper

def guest(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #CHECK IF USER IS LOGGED IN
        if session.get("LOGGED_USER"):
            return redirect("/auth")
        
        return fn (*args, **kwargs)
    return wrapper
