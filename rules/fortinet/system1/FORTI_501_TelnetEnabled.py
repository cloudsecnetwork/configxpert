class TelnetEnabled:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        start_marker = "config system accprofile"
        end_marker = "end"
        started = False
        config = []

        for line in enumerate(self.configuration.splitlines(), start=1):
            if line.strip() == start_marker:
                started = True
                continue
            elif line.strip() == end_marker and started:
                started = False
                break

            if started:
                config.append(line)

        if started:
            return {"value": "FAIL", "comment": "End marker not found"}
        elif config:
            return {"value": "PASS", "comment": "\n".join(config)}
        else:
            return {"value": "FAIL", "comment": "Start marker not found"}
