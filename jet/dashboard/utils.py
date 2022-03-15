from importlib import import_module
from jet.dashboard import settings


def get_current_dashboard(location):
    if location == 'index':
        path = settings.JET_INDEX_DASHBOARD
    elif location == 'app_index':
        path = settings.JET_APP_INDEX_DASHBOARD
    else:
        raise ValueError(f'Unknown dashboard location: {location}')

    module, cls = path.rsplit('.', 1)

    try:
        module = import_module(module)
        return getattr(module, cls)
    except ImportError:
        return None
