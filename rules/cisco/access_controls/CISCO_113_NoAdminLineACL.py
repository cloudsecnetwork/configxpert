class NoAdminLineACL:
    def __init__(self, configuration):
        self.configuration = configuration
        self.lines_with_vty = self.extract_lines_with_vty()

    def extract_lines_with_vty(self):
        lines_with_vty = []
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "line vty" in line.lower():
                lines_with_vty.append((line_number, line))
        return lines_with_vty

    def check(self):
        if self.lines_with_vty:
            comment = "found on "
            for line_number, line in self.lines_with_vty:
                comment += f"Line {line_number}: {line}, "
            return {"value": "FAIL", "comment": comment}
        else:
            return {"value": "PASS", "comment": ""}
