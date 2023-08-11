class WeakPassword:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        for index, line in enumerate(self.configuration.splitlines(), start=1):
            if "username" in line.lower() and "password" in line.lower():
                parts = line.lower().split()
                password_index = parts.index("password")
                if password_index + 1 < len(parts) and len(parts[password_index + 1]) <= 8:
                    return {
                        "value": "FAIL",
                        "comment": f"found on Line {index}: '{line.strip()}'"
                    }
        return {"value": "PASS", "comment": ""}