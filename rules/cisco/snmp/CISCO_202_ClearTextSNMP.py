class ClearTextSNMP:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        clear_text_lines = []
        for index, line in enumerate(self.configuration.splitlines(), start=1):
            if "snmp-server community" in line.lower():
                clear_text_lines.append({
                    "index": index,
                    "line": line.strip()
                })

        if clear_text_lines:
            return {
                "value": "FAIL",
                "comment": ", ".join([f"Line {entry['index']}: '{entry['line']}'" for entry in clear_text_lines])
            }
        else:
            return {"value": "PASS", "comment": ""}


