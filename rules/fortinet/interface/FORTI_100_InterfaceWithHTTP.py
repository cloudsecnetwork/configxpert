class InterfaceWithHTTP:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        http_interfaces = []
        
        lines = self.configuration.splitlines()
        index = 0
        while index < len(lines):
            line = lines[index]
            if "edit" in line and index + 1 < len(lines):
                index += 1
                while index < len(lines) and not lines[index].strip().startswith("next"):
                    if "set allowaccess" in lines[index] and "http " in lines[index]:
                        http_interfaces.append({
                            "interface_line": lines[index].strip(),
                            "interface_index": index + 1
                        })
                    index += 1
            else:
                index += 1
        
        if http_interfaces:
            return {
                "value": "FAIL",
                "comment": "issues found: \n" + "\n".join([f"Line {entry['interface_index']}: '{entry['interface_line']}'" for entry in http_interfaces])
            }
        else:
            return {"value": "PASS", "comment": ""}
