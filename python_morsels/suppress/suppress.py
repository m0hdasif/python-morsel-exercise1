import contextlib

class Suppressor(contextlib.suppress, contextlib.ContextDecorator):
    """
    Context manager for suppressing exceptions while getting
    the exception and traceback for non-suppressed exceptions.
    Can be used as a decorator.
    """
    def __init__(self, *args):
        super().__init__(*args)
        self.exception = None
        self.traceback = None

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.exception = value
        self.traceback = traceback
        return super().__exit__(type, value, traceback)

def suppress(*args):
    return Suppressor(*args)
