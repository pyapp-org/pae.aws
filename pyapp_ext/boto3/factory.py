from boto3 import Session

from pyapp.conf.helpers import ThreadLocalNamedSingletonFactory

__all__ = ("Session", "get_session", "session_factory", "client", "resource")


class SessionFactory(ThreadLocalNamedSingletonFactory[boto3.Session]):
    """
    Factory for creating AWS sessions.
    """

    defaults = {
        "region_name": None,
        "aws_access_key_id": None,
        "aws_secret_access_key": None,
        "aws_session_token": None,
        "profile_name": None,
    }

    def create(self, name: str = None) -> Session:
        config = self.get(name)
        return Session(**config)


session_factory = SessionFactory("AWS")
get_session = session_factory.create()


def client(service_name: str, config_name: str = None):
    """
    Factory for creating AWS clients.
    """
    return get_session(config_name).client(service_name)


def resource(service_name: str, config_name: str = None):
    """
    Factory for creating AWS resources
    """
    return get_session(config_name).resource(service_name)