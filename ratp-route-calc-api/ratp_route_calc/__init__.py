"""A client library for accessing Calculateur Vianavigo - Accès générique (Navitia)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
