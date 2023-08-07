import colorama

# Function to apply colors based on the pass/fail status
def get_colored_status(status):
    if status == "Pass":
        return colorama.Fore.GREEN + status + colorama.Style.RESET_ALL
    elif status == "Fail":
        return colorama.Fore.RED + status + colorama.Style.RESET_ALL
    else:
        return status

# Function to generate the security report with colored output
def generate_security_report(analyzed_results):
    # Create an empty report string to hold the report contents
    report = "Security Check Results:\n"

    # Loop through each security check result and format the report
    for check_name, result in analyzed_results.items():
        colored_status = get_colored_status(result)
        report += f"{check_name}: {colored_status}\n"

    return report
