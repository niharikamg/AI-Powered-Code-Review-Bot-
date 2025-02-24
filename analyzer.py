import ast
import pylint.lint

def analyze_code(code):
    try:
        ast.parse(code)  # Ensure the code is syntactically correct
        pylint_output = pylint.lint.Run(["--disable=all", "--enable=E,F,W,C,R"], do_exit=False)
        return str(pylint_output)
    except Exception as e:
        return f"Error analyzing code: {str(e)}"
