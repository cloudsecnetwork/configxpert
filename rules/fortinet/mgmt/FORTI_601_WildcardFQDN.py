class WildcardFQDN:
    def __init__(self, configuration):
        self.configuration = configuration
        self.issue_lines = []

    def check(self):
        lines = self.configuration.splitlines()
        for line_number, line in enumerate(lines, start=1):
            if "set wildcard-fqdn" in line.lower()and "*." in line:
                self.issue_lines.append((line_number, line))

        if self.issue_lines:
            comment = "\n".join([f"Line {line_number}: {line.lstrip()}" for line_number, line in self.issue_lines])
            return {"value": "FAIL", "comment": f"Wildcard FQDN issues found:\n{comment}"}
        else:
            return {"value": "PASS", "comment": ""}
