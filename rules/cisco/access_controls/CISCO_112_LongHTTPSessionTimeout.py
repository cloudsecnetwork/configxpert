class LongHTTPSessionTimeout:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        timeout_limit = 1200  # 20 minutes in seconds

        for index, line in enumerate(self.configuration.splitlines(), start=1):
            if "ip http timeout-policy" in line.lower() and "idle" in line.lower():
                parts = line.split()
                if len(parts) >= 7:
                    timeout = int(parts[6])
                    print("timeout", timeout)
                    if timeout > timeout_limit:
                        return {
                            "value": "FAIL",
                            "comment": f"found on line {index}: '{line.strip()}'"
                        }
        return {"value": "PASS", "comment": ""}