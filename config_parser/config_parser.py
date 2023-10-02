import re
import json


def read_cisco_file(filename):
    try:
        with open(filename, "r") as file:
            configuration = file.read()
        return configuration
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(
            f"Error: An unexpected error occurred while reading the file: {str(e)}")
    return None


def fortinet_config_to_json(config):
    result = {}
    current_section = None
    current_subsection = None

    try:
        lines_iterator = iter(config.splitlines())

        for line in lines_iterator:
            line = line.lstrip()

            if line.startswith("config"):
                current_section = line.replace("config ", "").strip()
                result[current_section] = {}
                current_subsection = None
                # next_line = next(lines_iterator, '')

            elif line.startswith("edit"):
                match = re.match(r'edit\s+["\']?(.*?)["\']?$', line.lstrip())
                current_subsection = match.group(1)
                result[current_section][current_subsection] = {}

            elif current_subsection is not None and line.startswith("set "):
                key, value = re.match(r"set (\S+) (.+)", line).groups()
                value = value.strip('"')
                result[current_section][current_subsection][key] = value

            elif current_subsection is None and line.startswith("set "):
                key, value = re.match(r"set (\S+) (.+)", line).groups()
                value = value.strip('"')
                result[current_section][key] = value

        return json.dumps(result, indent=2)

    except Exception as e:
        print(
            f"Error: An unexpected error occurred while processing the configuration: {str(e)}")
        return None


def read_fortinet_file(filename):
    try:
        with open(filename, "r") as file:
            raw_config = file.read()
            configuration = fortinet_config_to_json(raw_config)
            print(configuration)
            print()
        return configuration
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(
            f"Error: An unexpected error occurred while reading the file: {str(e)}")
    return None
