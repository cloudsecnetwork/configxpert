class NoCentralMgmtAccessControl:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        access_control_enabled = False
        lines = self.configuration.splitlines()
        central_mgmt_line = None

        for index, line in enumerate(lines):
            if "config system central-management" in line:
                central_mgmt_line = index + 1  # Add 1 to convert to line number
                index += 1
                while index < len(lines) and not lines[index].strip().startswith("end"):
                    if "set access-control enable" in lines[index]:
                        access_control_enabled = True
                    index += 1
            else:
                index += 1
        
        if central_mgmt_line is not None:
            if access_control_enabled:
                return {
                    "value": "PASS",
                    "comment": f"Line {central_mgmt_line}"
                }
            else:
                return {
                    "value": "FAIL",
                    "comment": f"Line {central_mgmt_line}"
                }
        else:
            return {
                "value": "NA",
                "comment": ""
            }