def read_configuration_from_file(filename):
    try:
        with open(filename, "r") as file:
            configuration = file.read()
        return configuration
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
    return None
