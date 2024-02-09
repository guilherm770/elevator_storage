from fastapi.testclient import TestClient
from fastapi.middleware.cors import CORSMiddleware
from src.factory import create_app
from src.routers import demand_router, elevator_router, floor_router
import logging


def test_create_app():
    app = create_app(debug=True)  # Set debug to True for testing purposes

    # Test app configurations
    assert app.debug is True

    # Test logging configurations
    logger = logging.getLogger()
    
    # Remove additional handlers added by FastAPI during testing
    for handler in logger.handlers.copy():
        logger.removeHandler(handler)
        
    # Test logging configurations
    logger = logging.getLogger()
    assert len(logger.handlers) == 1  # Only one handler added
    assert logger.handlers[0].level == logging.DEBUG  # DEBUG level

    # Test CORS middleware
    middleware = next(
        middleware
        for middleware in app.middleware
        if middleware.cls == CORSMiddleware
    )
    assert middleware.origins == ["*"]
    assert middleware.credentials is True
    assert middleware.methods == ["*"]
    assert middleware.headers == ["*"]

    # Test included routers
    assert any(
        router.path == "/demand" and router.route_class == demand_router.router
        for router in app.routes
    )
    assert any(
        router.path == "/elevator" and router.route_class == elevator_router.router
        for router in app.routes
    )
    assert any(
        router.path == "/floor" and router.route_class == floor_router.router
        for router in app.routes
    )