import traceback

try:
    VERSION = __import__("pkg_resources").get_distribution("app").version
except Exception:
    VERSION = "unknown"

__version__ = VERSION
__build__ = "0.0.1"


# try:
#     from app.scans.models import Scan
#
# except Exception:
#     traceback.print_exc()
