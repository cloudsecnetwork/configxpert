class defaultPassword:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        # Check for the presence of common default passwords
        default_passwords = ["cisco", "admin", "12345", "password"]
        
        for line in self.configuration.splitlines():
            for default in default_passwords:
                if default in line.lower():
                    # default password exists in config
                    return "Fail"
        return "True"