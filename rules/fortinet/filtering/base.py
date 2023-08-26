from .FORTI_300_ImproperFiltering import ImproperFiltering
from .FORTI_302_DeepAppInspectionDisabled import DeepAppInspectionDisabled
from .FORTI_301_NoIPSConfig import NoIPSConfig
# Import other rule classes here if you have more rules

__all__ = [
    "ImproperFiltering",
    "DeepAppInspectionDisabled",
    "NoIPSConfig"
    # Add other rule class names here
]
