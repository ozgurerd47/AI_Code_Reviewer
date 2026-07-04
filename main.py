from github_connector import connect_github
from pr_reader import fetch_pr
from ai_reviewer import analyze_code
import os

def ai_comment(repo_name, pr_number, comment_body):

    gh = connect_github()
    repo = gh.get_repo(repo_name)
    pr = repo.get_pull(pr_number)

    formatted_comment = f"### AI Review Comment:\n\n{comment_body}"

    pr.create_issue_comment(formatted_comment)

if __name__ == "__main__":
    TARGET_REPO = os.getenv("TARGET_REPO")
    PR_ID = int(os.getenv("PR_ID"))

    diff_text = fetch_pr(TARGET_REPO, PR_ID)
    if not diff_text.strip():
        print("No changes detected in the PR.")
    else:
        ai_review_comment = analyze_code(diff_text)
        review = analyze_code(diff_text)

        ai_comment(TARGET_REPO, PR_ID, review)

