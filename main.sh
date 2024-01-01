#!/bin/bash

# Function to generate random commit messages
generate_commit_message() {
    messages=("Update README" "Fix bug" "Add feature" "Improve docs" "Refactor code" "Update dependencies" "Fix typo" "Add tests" "Optimize performance" "Update configurations")
    echo ${messages[$RANDOM % ${#messages[@]}]}
}

# Start and end dates for commits
start_date="2024-01-03"
end_date="2024-01-04"

# Loop through each day in the date range
current_date=$start_date
while [[ "$current_date" < "$end_date" ]]; do
    # Generate a random number of commits for each day (between 1 and 3)
    num_commits=$((1 + RANDOM % 3))
    
    for ((i = 0; i < num_commits; i++)); do
        # Make a change to the repository
        echo "$current_date - $(generate_commit_message)" >> commit_log.txt

        # Stage and commit the change with a backdated timestamp
        GIT_AUTHOR_DATE="$current_date 12:00:00" GIT_COMMITTER_DATE="$current_date 12:00:00" git add commit_log.txt
        GIT_AUTHOR_DATE="$current_date 12:00:00" GIT_COMMITTER_DATE="$current_date 12:00:00" git commit -m "$(generate_commit_message)"
    done
    
    # Move to the next day
    current_date=$(date -j -v+1d -f "%Y-%m-%d" "$current_date" +"%Y-%m-%d")
done

# Push the commits to GitHub
git push origin master
