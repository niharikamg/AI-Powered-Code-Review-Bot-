import unittest
from code_analysis.security_checks import check_security

class TestSecurityChecks(unittest.TestCase):
    def test_hardcoded_password(self):
        code = "password = '12345'"
        result = check_security(code)
        self.assertIn("Hardcoded password found", result)  # Adjust based on actual output

if __name__ == "__main__":
    unittest.main()
