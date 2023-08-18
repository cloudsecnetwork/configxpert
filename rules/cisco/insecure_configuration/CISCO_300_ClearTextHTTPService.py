class ClearTextHTTPService:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        http_enabled_lines = []
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "ip http server" in line.lower():
                http_enabled_lines.append(line_number)

        if http_enabled_lines:
            comment = ", ".join([f"Line {line_number}" for line_number in http_enabled_lines])
            return {"value": "FAIL", "comment": f"Clear Text HTTP Service Enabled on: {comment}"}
        else:
            return {"value": "PASS", "comment": ""}