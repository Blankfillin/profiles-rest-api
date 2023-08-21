# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-a4x%g3e71y$-djx=%2)k10w!&ge4bit^cg)e7qhohc9hs2g&dl"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

LOGGING["formatters"]["colored"] = {  # type: ignore
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["cooking_core"]["level"] = "DEBUG"  # type: ignore
LOGGING["handlers"]["console"]["level"] = "DEBUG"  # type: ignore
LOGGING["handlers"]["console"]["formatter"] = "colored"  # type: ignore
