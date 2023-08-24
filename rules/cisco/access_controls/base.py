from .CISCO_100_NoPassword import NoPassword
from .CISCO_101_DefaultPassword import DefaultPassword
from .CISCO_102_WeakPassword import WeakPassword
from .CISCO_112_LongHTTPSessionTimeout import LongHTTPSessionTimeout
from .CISCO_113_NoAdminLineACL import NoAdminLineACL
from .CISCO_114_InterfaceWithoutACL import InterfaceWithoutACL
from .CISCO_115_UsersWithCiscoType7 import UsersWithCiscoType7

# Import other rule classes here if you have more rules

__all__ = [
    "NoPassword",
    "DefaultPassword",
    "WeakPassword",
    "LongHTTPSessionTimeout",
    "NoAdminLineACL",
    "InterfaceWithoutACL",
    "UsersWithCiscoType7",
    # Add other rule class names here
]