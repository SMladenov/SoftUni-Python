#Function Executor

def func_executor(*args):
    result = []
    for item in args:
        funcName = item[0].__name__
        funcArgs = item[1]
        funcResult = item[0](*funcArgs)
        result.append(f"{funcName} - {funcResult}")
        
    return '\n'.join(result)