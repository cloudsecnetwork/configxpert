class WeakPassword:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        # Check for the presence of both "username" and "password" in the configuration
        for index, line in enumerate(self.configuration.splitlines(), start=1):
            if "username" in line.lower() and "password" in line.lower():
                return {
                    "value": "FAIL",
                    "comment": f"found on line {index}: '{line.strip()}'"
                }
        return {"value": "PASS", "comment": ""}