# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import projeto.estoque.routing
from channels.sessions import SessionMiddlewareStack


application = ProtocolTypeRouter({ 
    'websocket': AuthMiddlewareStack(
        URLRouter(
            projeto.estoque.routing.websocket_urlpatterns
        )
    )
})