class ImproperFiltering:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        lines = self.configuration.splitlines()
        config_list = False
        issues = []

        for index, line in enumerate(lines):
            if "config entries" in line:
                config_list = True
            elif config_list and "edit" in line:
                entry_line_number = index + 1
                while index < len(lines) and not lines[index].strip().startswith("next"):
                    if "set action pass" in lines[index]:
                        issues.append({
                            "line_number": entry_line_number + 1,
                            "line_content": lines[entry_line_number]
                        })
                    index += 1
            elif config_list and "next" in line:
                config_list = False
        
        if issues:
            formatted_issues = "".join([f"Line {issue['line_number']}; " for issue in issues])
            return {
                "value": "FAIL",
                "comment": "issues found on: " + formatted_issues
            }
        else:
            return {
                "value": "PASS",
                "comment": "No issues found with improper filtering."
            }
