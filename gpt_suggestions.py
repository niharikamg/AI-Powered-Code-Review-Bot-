import openai

def suggest_improvements(code):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Python code reviewer."},
            {"role": "user", "content": f"Review the following Python code and suggest improvements:\n{code}"}
        ]
    )
    return response["choices"][0]["message"]["content"]
