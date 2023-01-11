import os
import sys
import argparse
import git
from datetime import datetime

def create_commit(repo_path, message, timestamp):
    try:
        repo = git.Repo(repo_path)
        # Stage all changes
        repo.git.add(A=True)
        # Create a commit with the specified timestamp
        repo.git.commit(m=message, date=timestamp)
        print(f"Commit created with message '{message}' at {timestamp}")
    except Exception as e:
        print(f"Error creating commit: {e}")

def push_commits(repo_path, branch='main'):
    try:
        repo = git.Repo(repo_path)
        origin = repo.remote(name='origin')
        origin.push(branch)
        print(f"Commits pushed to {branch} branch on GitHub")
    except Exception as e:
        print(f"Error pushing commits: {e}")

def main():
    parser = argparse.ArgumentParser(description="Time-travel command-line tool for creating commits with specific timestamps and pushing them to GitHub")
    
    subparsers = parser.add_subparsers(dest='command')
    
    # Create commits
    create_commit_parser = subparsers.add_parser('create-commit', help='Create a commit with a specific timestamp')
    create_commit_parser.add_argument('repo_path', type=str, help='Path to the git repository')
    create_commit_parser.add_argument('message', type=str, help='Commit message')
    create_commit_parser.add_argument('timestamp', type=str, help='Timestamp for the commit (format: YYYY-MM-DDTHH:MM:SS)')
    
    # Push commits
    push_parser = subparsers.add_parser('push', help='Push commits to GitHub')
    push_parser.add_argument('repo_path', type=str, help='Path to the git repository')
    push_parser.add_argument('branch', type=str, nargs='?', default='main', help='Branch to push to (default: main)')
    
    args = parser.parse_args()
    
    if args.command == 'create-commit':
        create_commit(args.repo_path, args.message, args.timestamp)
    elif args.command == 'push':
        push_commits(args.repo_path, args.branch)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
