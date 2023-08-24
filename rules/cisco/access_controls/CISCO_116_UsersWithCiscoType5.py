class UsersWithCiscoType5:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        cisco_type5_usernames = []
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "username" in line.lower() and "secret" in line.lower():
                parts = line.split()
                if len(parts) >= 4 and parts[3].startswith("$5$"):  # Check if the secret uses Cisco Type 5
                    username = parts[1]
                    cisco_type5_usernames.append(f" {username} on line {line_number}")

        if cisco_type5_usernames:
            comment = ", ".join(cisco_type5_usernames)
            return {"value": "FAIL", "comment": comment}
        else:
            return {"value": "PASS", "comment": ""}
