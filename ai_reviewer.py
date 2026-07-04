import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

def analyze_code(diff_text):

    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        raise ValueError("HF_TOKEN is not set in the environment variables.")
    
    client = InferenceClient(
        model = "Qwen/Qwen2.5-Coder-32B-Instruct",
        token=hf_token
    )

    prompt = """
    Please follow those instructions:
    1. Detect security vulnerabilities, performance issues and bad code practices, if exists.
    2. Provide a short, clear and concise summary of the changes in the PR.
    3. If code is perfect, then just say "The code is perfect, no issues found."
    4. Give your answer in markdown format. 
    """

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"Analyze these code changes: \n\n{diff_text}"}
    ]

    try: 
        response = client.chat_completion(
            messages = messages,
            max_tokens = 500,
            temperature = 0.3
        )

        review_comment = response.choices[0].message.content
        return review_comment

    except Exception as e:
        print(f"Error during code analysis: {e}")

