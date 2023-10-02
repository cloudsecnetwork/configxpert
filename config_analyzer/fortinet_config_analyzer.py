from rules.fortinet.interface.base import *
from rules.fortinet.filtering.base import *
from rules.fortinet.mgmt.base  import *
from rules.fortinet.system1.base import *
# Import other rule classes from base.py if you have more rules

def analyze_fortinet_configuration(configuration):
    # Perform security checks
    security_checks_results = {}

    # security_checks_results["Telnet is enabled"] = TelnetEnabled(configuration).check()

    # security_checks_results["System interface with HTTP access"] = InterfaceWithHTTP(configuration).check()
    # security_checks_results["Weak encryption on IPSec interface"] = WeakIPSecEncryption(configuration).check()
    # security_checks_results["Disabled Perfect Forward Secrecy on IPSec interface"] = NoPFSOnIPSec(configuration).check()
    # security_checks_results["Disabled replay protection on IPSec interface"] = NoReplayOnIPSec(configuration).check()

    # security_checks_results["Filtering rule not configured properly"] = ImproperFiltering(configuration).check()
    # security_checks_results["Deep application inspection is disabled"] = DeepAppInspectionDisabled(configuration).check()
    # security_checks_results["Intrusion Prevention System config not present"] = NoIPSConfig(configuration).check()

    # security_checks_results["Override setting is disabled for HA"] = HAOverrideDisabled(configuration).check()
    # security_checks_results["Overly permissive wildcard domains set"] = WildcardFQDN(configuration).check()
    # security_checks_results["Central management access control is disabled"] = NoCentralMgmtAccessControl(configuration).check()
    # security_checks_results["Central management log is disabled"] = NoCentralMgmtLog(configuration).check()

    # print(security_checks_results) -- 

    return security_checks_results
