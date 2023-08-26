class DeepAppInspectionDisabled:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        lines = self.configuration.splitlines()

        for index, line in enumerate(lines):
            if "set deep-app-inspection disable" in line:
                return {
                    "value": "FAIL",
                    "comment": f"Line {index + 1}"
                    # "comment": f"Line {index + 1}: {line.strip()}"

                }
        
        return {"value": "PASS", "comment": ""}
