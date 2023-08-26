import argparse
import colorama
from config_parser.config_parser import read_configuration_from_file
from config_analyzer.cisco_config_analyzer import analyze_cisco_configuration
from config_analyzer.fortinet_config_analyzer import analyze_fortinet_configuration
from config_reporter.config_reporter import generate_security_report

def main():
    colorama.init(autoreset=True, convert=True)  # Initialize colorama with convert=True

    # Create an argument parser
    parser = argparse.ArgumentParser(description="Process configuration file for security analysis")
    
    # Add an argument for the file path
    parser.add_argument("-f", type=str, required=True, help="Path to the configuration file")
    
    # Add an argument for the device type
    parser.add_argument("-d", type=str, choices=["fortinet", "cisco"], required=True, help="Specify a type of networking device")

    # Parse the command line arguments
    args = parser.parse_args()
    config_filename = args.f
    device_type = args.d

    # Read the configuration from the specified file
    configuration = read_configuration_from_file(config_filename)
    if not configuration:
        return

    # Analyze the configuration for security checks based on the device type
    if device_type.lower() == "fortinet":
        analyzed_results = analyze_fortinet_configuration(configuration)
    elif device_type.lower() == "cisco":
        analyzed_results = analyze_cisco_configuration(configuration)
    else:
        # print("Unsupported device type. Please provide 'fortinet' or 'cisco' as the device type.")
        return

    # Generate the security report with colored output
    security_report = generate_security_report(analyzed_results)

    # Display the security report
    print(security_report)

    colorama.deinit()  # Deinitialize colorama

if __name__ == "__main__":
    main()
