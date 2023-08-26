# ConfigXpert Net

## Overview
ConfigXpert Net is a Python script that analyzes network device configurations to identify potential security vulnerabilities. It performs security checks on the provided configuration file and generates a detailed security report. This tool is intended to help network administrators and security professionals enhance the security posture of their network devices.

## Prerequisites
- Python 3.x installed on your system.
- An SSH-enabled network device configuration file (e.g., `device_config.txt`).

## Getting Started

1. Clone the repository to your local machine:

2. Navigate to the project directory:

3. Install the required dependencies from the `requirements.txt` file:

4. Place your network device configuration file (`device_config.txt`) in the `data/` directory.

### Docker Build

1. Clone this repository to your local machine:
```
git clone https://github.com/configxpert/configxpert-net.git
```

2. Navigate to the project directory:
```
cd configxpert-net
```

3. Build the Docker image using the following command:
```
docker build -t configxpert .
```

### Running the Docker Container

After building the Docker image, you can run the ConfigXpert tool using the following command:
```
docker run -it --rm configxpert
```

## Running the Python Script 

To analyze the network device configuration and generate the security report, follow these steps:

1. Open a terminal or command prompt.
```
git clone https://github.com/configxpert/configxpert-net.git
```

2. Execute the main script (`main.py`) using Python:
```
cd configxpert-net
```

3. The script will read the configuration from the `device_config.txt` file, analyze it for security checks, and generate a security report.
```
pip install -r requirements.txt
```

4. The generated security report will be displayed on the console. You can also reference the location for you own config files instea.
```
 python main.py --help
 python main.py -d "cisco" -f "data/device_config.txt"
 python main.py -d "fortinet" -f "data/firewall.conf"
```

## Customizing Security Checks

You can customize the security checks performed by the Config Review Tool by modifying the `config_analyzer/config_analyzer.py` file. In this file, you can implement additional checks or adjust the existing logic to match your specific security requirements.

## Running Unit Tests

To run unit tests for the individual modules, you can execute the following commands:
```
python -m unittest discover -s tests
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contribution

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests.
