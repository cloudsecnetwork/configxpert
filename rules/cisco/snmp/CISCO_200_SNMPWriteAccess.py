class SNMPWriteAccess:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        snmp_write_lines = []
        for index, line in enumerate(self.configuration.splitlines(), start=1):
            if "snmp-server community" in line.lower() and "rw" in line.lower():
                snmp_write_lines.append({
                    "index": index,
                    "line": line.strip()
                })

        if snmp_write_lines:
            return {
                "value": "FAIL",
                "comment": ", ".join([f"Line {entry['index']}: '{entry['line']}'" for entry in snmp_write_lines])
            }
        else:
            return {"value": "PASS", "comment": ""}
