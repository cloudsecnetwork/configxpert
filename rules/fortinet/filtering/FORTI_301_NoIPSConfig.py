class NoIPSConfig:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        lines = self.configuration.splitlines()
        ips_start_line = None
        ips_end_line = None

        for index, line in enumerate(lines):
            if "config ips global" in line:
                ips_start_line = index + 1  # Add 1 to convert to line number
            elif ips_start_line is not None and line.strip() == "end":
                ips_end_line = index + 1  # Add 1 to convert to line number
                break

        if ips_start_line is not None and ips_end_line is not None:
            lines_between = ips_end_line - ips_start_line - 1
            if lines_between == 0:
                return {
                    "value": "FAIL",
                    "comment": f"Line {ips_start_line}"
                }
            else:
                return {
                    "value": "PASS",
                    "comment": ""
                    # "comment": f"{lines_between} lines between lines {ips_start_line} and {ips_end_line}"
                }
        else:
            return {
                "value": "NA",
                "comment": ""
            }
