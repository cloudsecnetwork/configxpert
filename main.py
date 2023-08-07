from config_parser import read_configuration_from_file
from config_analyzer import analyze_configuration
from config_reporter import generate_security_report

def main():
    config_filename = "data/device_config.txt"

    configuration = read_configuration_from_file(config_filename)
    if not configuration:
        return

    analyzed_results = analyze_configuration(configuration)
    security_report = generate_security_report(analyzed_results)

    print(security_report)

if __name__ == "__main__":
    main()
