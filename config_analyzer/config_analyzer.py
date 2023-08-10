from rules.cisco.access_controls.base import *
# Import other rule classes from base.py if you have more rules

def analyze_configuration(configuration):
    # Perform security checks
    security_checks_results = {}

    security_checks_results["No Password Configured"] = NoPassword(configuration).check()
    security_checks_results["Default Password in use"] = DefaultPassword(configuration).check()
    security_checks_results["Weak Password in use"] = WeakPassword(configuration).check()

    print(security_checks_results)

    return security_checks_results
