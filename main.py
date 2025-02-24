import sys
from code_analysis.analyzer import analyze_code
from models.gpt_suggestions import suggest_improvements

def main(file_path):
    with open(file_path, "r") as f:
        code = f.read()

    analysis = analyze_code(code)
    suggestions = suggest_improvements(code)

    print("Analysis Report:")
    print(analysis)
    print("\nAI Suggestions:")
    print(suggestions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <file.py>")
    else:
        main(sys.argv[1])