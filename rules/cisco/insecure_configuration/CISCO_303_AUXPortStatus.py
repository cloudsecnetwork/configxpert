class AUXPortStatus:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        aux_port_enabled = False
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "line aux" in line.lower():
                aux_port_enabled = True
                break

        if aux_port_enabled:
            return {"value": "FAIL", "comment": "AUX Port is Not Disabled"}
        else:
            return {"value": "PASS", "comment": ""}