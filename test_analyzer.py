import unittest
from code_analysis.analyzer import analyze_code

class TestAnalyzer(unittest.TestCase):
    def test_valid_code(self):
        code = "print('Hello, World!')"
        result = analyze_code(code)
        self.assertIn("Your code looks fine", result)  # Adjust based on actual output

if __name__ == "__main__":
    unittest.main()
