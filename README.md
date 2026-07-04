# 🤖 AI-Powered GitHub Code Reviewer Bot

An automated, serverless MLOps pipeline that acts as a **Senior AI Code Reviewer**. It automatically fetches Pull Request (PR) diffs, analyzes the changes using large language models via Hugging Face Inference API, and posts constructive code reviews directly to GitHub PRs.

---

## 🌟 Key Features

- **Automated Diff Extraction:** Fetches only the changed lines (`git diff`) of a Pull Request using `PyGithub` to optimize context length and speed.
- **Advanced LLM Code Analysis:** Powered by **Qwen-2.5-Coder-32B-Instruct** via Hugging Face Serverless Inference API.
- **Senior Engineer Persona:** Detects security vulnerabilities (e.g., SQL injections, hardcoded credentials), performance bottlenecks, and clean code violations.
- **Automated Feedback Loop:** Directly posts formatted Markdown reviews as GitHub PR comments.
- **Secure & Configurable:** Environment variables managed securely via `.env` without exposing sensitive PATs or API keys.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **APIs & SDKs:** `PyGithub`, `huggingface_hub`
- **AI / NLP Model:** Qwen/Qwen2.5-Coder-32B-Instruct
- **Security & Config:** `python-dotenv`

---

## 🚀 Architecture Workflow

1. **Trigger:** A developer opens or updates a Pull Request.
2. **Fetch:** `pr_reader.py` connects to GitHub and extracts the raw patch/diff.
3. **Analyze:** `ai_reviewer.py` prompts the LLM to review the code for bugs, security issues, and bad practices.
4. **Comment:** `main.py` posts the structured review back to the GitHub Pull Request automatically.

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
