import os


def _default_sqlite_path() -> str:
    # Resolve path relative to this file: backend/instance/app.db
    here = os.path.dirname(__file__)
    backend_dir = os.path.abspath(os.path.join(here, '..'))
    instance_dir = os.path.join(backend_dir, 'instance')
    os.makedirs(instance_dir, exist_ok=True)
    return os.path.join(instance_dir, 'app.db')


def get_database_uri() -> str:
    # Default to SQLite in backend/instance; override with DATABASE_URL
    default_path = _default_sqlite_path()
    return os.getenv('DATABASE_URL', f'sqlite:///{default_path}')
