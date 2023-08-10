import argparse
import colorama
from config_parser.config_parser import read_configuration_from_file
from config_analyzer.config_analyzer import analyze_configuration
from config_reporter.config_reporter import generate_security_report

def main():
    colorama.init(autoreset=True, convert=True)  # Initialize colorama with convert=True

    # Create an argument parser
    parser = argparse.ArgumentParser(description="Process configuration file for security analysis")
    
    # Add an argument for the file path
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to the configuration file")

    # Parse the command line arguments
    args = parser.parse_args()
    config_filename = args.file

    # Read the configuration from the specified file
    configuration = read_configuration_from_file(config_filename)
    if not configuration:
        return

    # Analyze the configuration for security checks
    analyzed_results = analyze_configuration(configuration)

    # Generate the security report with colored output
    security_report = generate_security_report(analyzed_results)

    # Display the security report
    print(security_report)

    colorama.deinit()  # Deinitialize colorama

if __name__ == "__main__":
    main()
