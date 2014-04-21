def to_function(callable):
    def f(*args, **kwargs):
        return callable(*args, **kwargs)
    f.__name__ = callable.__name__
    f.__doc__ = callable.__doc__
    return f
