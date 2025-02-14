import requests

EXIT_FLAG = False
while EXIT_FLAG is False:
    username = input("github-activity: ")
    response = requests.get(f"https://api.github.com/users/{username}/events")
    if response.status_code == 200:
        items = response.json()
        print("found")
        for item in items:
            if item['type'] == 'CreateEvent':
                if item['payload']['ref_type'] == "branch":
                    print(f"user: {item['actor']['login']} has made a branch called {item['payload']['ref']} from branch {item['payload']['master_branch']} on repo {item['repo']['name']}")
                elif item['payload']['ref_type'] == "tag":
                    print(f"user: {item['actor']['login']} has made a tag called {item['payload']['ref']} from branch {item['payload']['master_branch']} on repo {item['repo']['name']}")
                elif item['payload']['ref_type'] == "repository":
                    print(f"user: {item['actor']['login']} has made a repository called {item['repo']['name']} with master branch {item['payload']['master_branch']}")

            elif item['type'] == 'ForkEvent':
                print(f"user: {item['actor']['display_login']} has forked {item['forkee']['full_name']}")

            elif item['type'] == 'IssueCommentEvent':
                print(f"user: {item['actor']['login']} has commented on {item['repo']['name']}")

            elif item['type'] == 'PullRequestReviewEvent':
                print(f"user: {item['actor']['login']} has reviewd the pull request of user {item['payload']['pull_request']['user']['login']} for repo {item['repo']['name']}")

            elif item['type'] == 'PushEvent':
                commits_counts = len(item["payload"]["commits"])
                print(f"user: {item['actor']['display_login']} pushed {commits_counts} commits to {item['repo']['name']}")

            elif item['type'] == 'WatchEvent':
                print(f"user: {item['actor']['login']} starred {item['repo']['name']}")
    ask = input("do you want to exit? (y/n): ").strip().lower()
    if ask == 'y':
        EXIT_FLAG = True
