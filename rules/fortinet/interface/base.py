from .FORTI_100_InterfaceWithHTTP import InterfaceWithHTTP
from .FORTI_101_WeakIPSecEncryption import WeakIPSecEncryption
from .FORTI_102_NoPFSOnIPSec import NoPFSOnIPSec
from .FORTI_103_NoReplayOnIPSec import NoReplayOnIPSec
# Import other rule classes here if you have more rules

__all__ = [
    "InterfaceWithHTTP",
    "WeakIPSecEncryption",
    "NoPFSOnIPSec",
    "NoReplayOnIPSec"
    # Add other rule class names here
]