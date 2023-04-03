#!/urs/bin/env bash
# It display all http methods a server allows.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
