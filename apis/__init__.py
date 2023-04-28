from .dummy_api import DummyApis
from .header_bar_api import HeaderBarApi


def AppAPIs(server):

    DummyApis(server)
    HeaderBarApi(server)