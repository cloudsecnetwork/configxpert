def analyze_configuration(configuration):
    # Split the configuration into lines
    config_lines = configuration.splitlines()

    # Security checks results (dictionary to hold check names and their results)
    security_checks_results = {}

    # Check 1: Check if "enable secret" is configured
    if "enable secret" in configuration:
        security_checks_results["Enable Secret Configured"] = "Pass"
    else:
        security_checks_results["Enable Secret Configured"] = "Fail"

    # Check 2: Check if SSH is enabled for remote access
    if "transport input ssh" in configuration:
        security_checks_results["SSH Enabled"] = "Pass"
    else:
        security_checks_results["SSH Enabled"] = "Fail"

    # Check 3: Check if there are any empty access lists (ACLs)
    acl_lines = [line for line in config_lines if line.strip().startswith("access-list")]
    empty_acls = [acl for acl in acl_lines if "permit" not in acl and "deny" not in acl]
    if empty_acls:
        security_checks_results["Empty ACLs"] = "Fail"
    else:
        security_checks_results["Empty ACLs"] = "Pass"

    # Check 4: Check if IP Source Routing is disabled
    if "no ip source-route" in configuration:
        security_checks_results["IP Source Routing Disabled"] = "Pass"
    else:
        security_checks_results["IP Source Routing Disabled"] = "Fail"

    # Check 5: Check if CDP (Cisco Discovery Protocol) is disabled on external interfaces
    interfaces = [line for line in config_lines if line.strip().startswith("interface")]
    cdp_disabled_on_external = False
    for interface in interfaces:
        if "no cdp enable" not in interface:
            cdp_disabled_on_external = True
            break
    if cdp_disabled_on_external:
        security_checks_results["CDP Disabled on External Interfaces"] = "Pass"
    else:
        security_checks_results["CDP Disabled on External Interfaces"] = "Fail"

    # Check 6: Check if unused interfaces are shut down
    unused_interfaces = ["GigabitEthernet0/3", "GigabitEthernet0/4"]  # List of unused interfaces
    for interface in unused_interfaces:
        if interface in configuration and "no shutdown" not in configuration:
            security_checks_results["Unused Interface: " + interface] = "Fail"
        else:
            security_checks_results["Unused Interface: " + interface] = "Pass"

    # Add more checks as needed based on your security requirements

    return security_checks_results
