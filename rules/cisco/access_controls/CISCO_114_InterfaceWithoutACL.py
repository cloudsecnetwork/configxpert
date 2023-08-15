class InterfaceWithoutACL:
    def __init__(self, configuration):
        self.configuration = configuration
        self.interfaces_with_acl = self.extract_interfaces_with_acl()

    def extract_interfaces_with_acl(self):
        interfaces_with_acl = set()
        for line in self.configuration.splitlines():
            if line.startswith("access-list"):
                interface_name = line.split()[-1]
                interfaces_with_acl.add(interface_name)
        return interfaces_with_acl

    def detect_interfaces_without_acl(self):
        all_interfaces = set()
        for line in self.configuration.splitlines():
            if line.startswith("interface"):
                interface_name = line.split()[1]
                all_interfaces.add(interface_name)

        interfaces_without_acl = all_interfaces - self.interfaces_with_acl
        return interfaces_without_acl

    def check(self):
        interfaces_without_acl = self.detect_interfaces_without_acl()

        if interfaces_without_acl:
            comment = ", ".join(interfaces_without_acl)
            return {"value": "FAIL", "comment": f"Interfaces without ACLs: {comment}"}
        else:
            return {"value": "PASS", "comment": ""}

