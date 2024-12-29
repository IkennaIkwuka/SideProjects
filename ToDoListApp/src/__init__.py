from .main import App
from .utilities import Utility

utility = Utility()


app = App(10, "cmd/docs/Tasks.txt")

__all__ = ["App","utility"]
