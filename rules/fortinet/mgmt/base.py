from .FORTI_600_HAOverrideDisabled import HAOverrideDisabled
from .FORTI_601_WildcardFQDN import WildcardFQDN
from .FORTI_602_NoCentralMgmtAccessControl import NoCentralMgmtAccessControl
from .FORTI_603_NoCentralMgmtLog import NoCentralMgmtLog
# Import other rule classes here if you have more rules

__all__ = [
    "HAOverrideDisabled",
    "WildcardFQDN",
    "NoCentralMgmtAccessControl",
    "NoCentralMgmtLog"
    # Add other rule class names here
]