class DefaultPassword:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        # Check for the presence of common default passwords
        default_passwords = ["cisco", "admin", "12345", "password"]
        
        for index, line in enumerate(self.configuration.splitlines(), start=1):
            for default in default_passwords:
                if default in line.lower():
                    return {
                        "value": "FAIL",
                        "comment": f"found on Line {index}: '{line.strip()}'"
                    }
        return {"value": "PASS", "comment": ""}