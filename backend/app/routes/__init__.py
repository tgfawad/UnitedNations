from flask import Blueprint

api_bp = Blueprint('api', __name__)

# Import submodules to register routes on the blueprint
from . import menu, rules  # noqa: E402,F401

__all__ = ["api_bp"]
