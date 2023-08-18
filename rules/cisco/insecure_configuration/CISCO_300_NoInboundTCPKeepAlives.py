class NoInboundTCPKeepAlives:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        no_keepalive_lines = []
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "no ip tcp keepalive" in line.lower():
                no_keepalive_lines.append(line_number)

        if no_keepalive_lines:
            comment = ", ".join([f"Line {line_number}" for line_number in no_keepalive_lines])
            return {"value": "FAIL", "comment": f"No Inbound TCP KeepAlives found on: {comment}"}
        else:
            return {"value": "PASS", "comment": ""}

