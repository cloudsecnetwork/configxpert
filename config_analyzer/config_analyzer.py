from rules.cisco.access_controls.base import *
from rules.cisco.snmp.base import *
from rules.cisco.insecure_configuration.base import *
# Import other rule classes from base.py if you have more rules

def analyze_configuration(configuration):
    # Perform security checks
    security_checks_results = {}

    security_checks_results["No Password Configured"] = NoPassword(configuration).check()
    security_checks_results["Default Password in use"] = DefaultPassword(configuration).check()
    security_checks_results["Weak Password in use"] = WeakPassword(configuration).check()
    security_checks_results["Long HTTP Session Timeout"] = LongHTTPSessionTimeout(configuration).check()
    security_checks_results["Admin Line without an ACL"] = NoAdminLineACL(configuration).check()
    security_checks_results["Interface without ACL"] = InterfaceWithoutACL(configuration).check()
    security_checks_results["Users Configured With Cisco Type 7 Password Hashing Algorithm"] = UsersWithCiscoType7(configuration).check()
    security_checks_results["Users Configured With Cisco Type 5 Password Hashing Algorithm"] = UsersWithCiscoType5(configuration).check()

    security_checks_results["Default SNMP String"] = DefaultSNMPString(configuration).check()
    security_checks_results["SNMP Write Access Enabled"] = SNMPWriteAccess(configuration).check()
    security_checks_results["Clear Text SNMP"] = ClearTextSNMP(configuration).check()

    security_checks_results["No Inbound TCP Keep Alives"] = NoInboundTCPKeepAlives(configuration).check()
    security_checks_results["Clear Text HTTP Service"] = ClearTextHTTPService(configuration).check()
    security_checks_results["Usernames With Admin"] = UsernamesWithAdmin(configuration).check()

    # print(security_checks_results)

    return security_checks_results
