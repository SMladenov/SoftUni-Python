def concatenate(*args, **kwargs):
    concatenatedString = ''.join(args)
    
    for key, value in kwargs.items():
        concatenatedString = concatenatedString.replace(key, value)

    return concatenatedString