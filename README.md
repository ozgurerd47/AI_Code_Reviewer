# 🤖 AI-Powered GitHub Code Reviewer Bot

An automated, serverless MLOps pipeline that acts as a **Senior AI Code Reviewer**. The bot automatically retrieves Pull Request (PR) diffs, analyzes the changes using a large language model through the Hugging Face Inference API, and posts actionable review comments directly to GitHub.

---

## 🌟 Features

* **Automated PR Diff Extraction** – Retrieves only the modified lines from a Pull Request using `PyGithub` to reduce token usage and improve inference speed.
* **LLM-Powered Code Review** – Uses **Qwen-2.5-Coder-32B-Instruct** via the Hugging Face Serverless Inference API.
* **Senior Engineer Review Style** – Identifies potential bugs, security vulnerabilities, performance issues, and clean code violations while suggesting improvements.
* **Automated Feedback** – Publishes structured Markdown review comments directly on the GitHub Pull Request.
* **Secure Configuration** – Keeps GitHub and Hugging Face credentials safely managed with environment variables.

---

## 🛠️ Tech Stack

| Category               | Technology                      |
| ---------------------- | ------------------------------- |
| **Language**           | Python 3.10+                    |
| **GitHub Integration** | PyGithub                        |
| **LLM API**            | Hugging Face Inference API      |
| **Model**              | Qwen/Qwen2.5-Coder-32B-Instruct |
| **Configuration**      | python-dotenv                   |

---

## 🏗️ Architecture

```text
Developer Opens/Updates PR
           │
           ▼
    pr_reader.py
   (Fetch PR Diff)
           │
           ▼
   ai_reviewer.py
 (LLM Code Analysis)
           │
           ▼
       main.py
(Post Review Comment)
           │
           ▼
      GitHub Pull Request
```

---

## ⚙️ Workflow

1. A developer opens or updates a Pull Request.
2. `pr_reader.py` retrieves the changed code from GitHub.
3. `ai_reviewer.py` sends the diff to the LLM for analysis.
4. The model reviews the code for:

   * Bugs
   * Security vulnerabilities
   * Performance issues
   * Clean code violations
   * Best-practice improvements
5. `main.py` posts the generated review back to the Pull Request.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate

# Windows
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create your environment file:

```bash
cp .env.example .env
```

Update the `.env` file with your credentials:

```env
GITHUB_TOKEN=ghp_your_github_token
HF_TOKEN=hf_your_huggingface_token
TARGET_REPO=username/repository-name
TARGET_PR_ID=1
```

---

## ▶️ Run

Execute the pipeline:

```bash
python main.py
```

---

## 📂 Project Structure

```text
.
├── ai_reviewer.py      # Sends the PR diff to the LLM
├── pr_reader.py        # Fetches Pull Request diffs
├── main.py             # Pipeline entry point
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📌 Example Pipeline

```text
Pull Request
      │
      ▼
 GitHub API
      │
      ▼
 PR Diff Extraction
      │
      ▼
 Hugging Face API
      │
      ▼
Qwen-2.5-Coder-32B-Instruct
      │
      ▼
 Generated Review
      │
      ▼
GitHub PR Comment
```
