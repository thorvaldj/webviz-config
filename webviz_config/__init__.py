from pkg_resources import get_distribution, DistributionNotFound

from ._localhost_token import LocalhostToken
from ._localhost_open_browser import LocalhostOpenBrowser
from ._is_reload_process import is_reload_process

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass