from github_connector import connect_github

def fetch_pr(repo_name, pr_number):

    gh = connect_github()

    repo = gh.get_repo(repo_name)
    pr = repo.get_pull(pr_number)

    diff_content = ""

    for file in pr.get_files():

        if file.patch:
            diff_content += f"\n---File: {file.filename}---\n"
            diff_content += file.patch + "\n"

    return diff_content