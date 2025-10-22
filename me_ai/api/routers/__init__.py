from .chat import chat_router
from .health import health_router

routers = [health_router, chat_router]
