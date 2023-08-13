class DefaultSNMPString:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        for index, line in enumerate(self.configuration.splitlines(), start=1):
            if "snmp-server community" in line.lower():
                if any(snmp_string in line.lower() for snmp_string in ["public", "private"]):
                    return {
                        "value": "FAIL",
                        "comment": f"Line {index}: '{line.strip()}'"
                    }
        return {"value": "PASS", "comment": ""}