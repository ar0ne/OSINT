try:
    VERSION = __import__("pkg_resources").get_distribution("osint").version
except Exception:
    VERSION = "unknown"

__version__ = VERSION
__build__ = "0.1.0"
