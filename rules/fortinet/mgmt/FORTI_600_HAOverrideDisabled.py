class HAOverrideDisabled:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "set override disable" in line.lower():
                return {"value": "FAIL", "comment": f"Line {line_number}"}

        return {"value": "PASS", "comment": ""}
