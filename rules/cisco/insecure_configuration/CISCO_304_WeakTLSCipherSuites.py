class WeakTLSCipherSuites:
    def __init__(self, configuration):
        self.configuration = configuration

    def check(self):
        weak_cipher_suites = []
        for line_number, line in enumerate(self.configuration.splitlines(), start=1):
            if "ssl cipher" in line.lower() or "tls cipher" in line.lower():
                parts = line.split()
                cipher_suite = " ".join(parts[2:])
                if self.is_weak_cipher_suite(cipher_suite):
                    weak_cipher_suites.append(f"Weak cipher suite '{cipher_suite}' detected on line {line_number}")

        if weak_cipher_suites:
            comment = "\n".join(weak_cipher_suites)
            return {"value": "FAIL", "comment": comment}
        else:
            return {"value": "PASS", "comment": ""}

    def is_weak_cipher_suite(self, cipher_suite):
        weak_ciphers = ["rc4", "des", "3des", "md5"]
        for weak_cipher in weak_ciphers:
            if weak_cipher in cipher_suite.lower():
                return True
        return False