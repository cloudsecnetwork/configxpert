import colorama

# Function to apply colors based on the pass/fail status
def get_colored_status(status):
    if status == "PASS":
        return colorama.Fore.GREEN + status + colorama.Style.RESET_ALL
    elif status == "FAIL":
        return colorama.Fore.RED + status + colorama.Style.RESET_ALL
    else:
        return status
    
def get_comment(comment):
    if comment == "":
        return ""
    return f"- {comment}"
    # return colorama.Fore.YELLOW + comment + colorama.Style.RESET_ALL

# Function to generate the security report with colored output
def generate_security_report(analyzed_results):
    # Create an empty report string to hold the report contents
    report = "Security Check Results:\n\n"

    # Loop through each security check result and format the report
    for check_name, result in analyzed_results.items():
        status = get_colored_status(result["value"])
        comment = get_comment(result["comment"])
        report += f"{status}: {check_name} {comment}\n"

    return report
