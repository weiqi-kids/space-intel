"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .ast_spacemobile import AstSpacemobileFetcher
from .boeing import BoeingFetcher
from .globalstar import GlobalstarFetcher
from .intuitive import IntuitiveFetcher
from .iridium import IridiumFetcher
from .l3harris import L3harrisFetcher
from .lockheed import LockheedFetcher
from .northrop import NorthropFetcher
from .planet import PlanetFetcher
from .redwire import RedwireFetcher
from .rocket_lab import RocketLabFetcher
from .ses import SesFetcher
from .spire import SpireFetcher
from .viasat import ViasatFetcher

FETCHERS = {
    "ast_spacemobile": AstSpacemobileFetcher,
    "boeing": BoeingFetcher,
    "globalstar": GlobalstarFetcher,
    "intuitive": IntuitiveFetcher,
    "iridium": IridiumFetcher,
    "l3harris": L3harrisFetcher,
    "lockheed": LockheedFetcher,
    "northrop": NorthropFetcher,
    "planet": PlanetFetcher,
    "redwire": RedwireFetcher,
    "rocket_lab": RocketLabFetcher,
    "ses": SesFetcher,
    "spire": SpireFetcher,
    "viasat": ViasatFetcher,
}
