class WeakIPSecEncryption:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        lines = self.configuration.splitlines()
        weak_lines = []

        for index, line in enumerate(lines):
            if "set proposal aes256-sha1" in line:
                weak_lines.append(f"Line {index + 1}: {line.lstrip()}")
        
        if weak_lines:
            return {
                "value": "FAIL",
                "comment": ", ".join(weak_lines)
            }
        else:
            return {"value": "PASS", "comment": ""}
