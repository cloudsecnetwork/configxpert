class UsersWithCiscoType7:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        cisco_type7_usernames = []
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "username" in line.lower() and "secret" in line.lower():
                parts = line.split()
                if len(parts) >= 4 and parts[3].startswith("7"):  # Check if the secret is using Cisco Type 7
                    username = parts[1]
                    cisco_type7_usernames.append(f"{username} on line {line_number}")

        if cisco_type7_usernames:
            comment = ", ".join(cisco_type7_usernames)
            return {"value": "FAIL", "comment": comment}
        else:
            return {"value": "PASS", "comment": ""}