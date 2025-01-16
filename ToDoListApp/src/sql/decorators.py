# Decorators
from functools import wraps
import traceback


@staticmethod
def db_ops(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        # class_name = self.__class__.__name__
        try:
            result = func(self, *args, **kwargs)
            # getattr(self, f"_{class_name}__commit")()
            self._commit()
            return result
        except Exception as e:
            print(f"Unexpected error: {e}")
            # getattr(self, f"_{class_name}__rollback")()
            self._rollback()
            traceback.print_exc()

    return wrapper
