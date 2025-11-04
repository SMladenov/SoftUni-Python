from functools import wraps


def uppercase (function):
    @wraps(function) #For Documentation
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result
    
    return wrapper

@uppercase
def get_letters():
    """Documentation"""
    return "please print upper"

# print (get_letters())
# print (get_letters.__doc__)

#*args

###Classes as Decorators###

#__call__ method allows class instances to be called as functions

class func_logger:

    _logfile = 'out.log'

    def __init__ (self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        log_string = self.func.__name__ + " was called"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args)


    
