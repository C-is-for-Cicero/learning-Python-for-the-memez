def function(*args):
    result = [str.upper(strings) for strings in args]
    result=sorted(result)

    return result
