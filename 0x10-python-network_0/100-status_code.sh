#!/use/bin/env bash
# It sends a get request to a given url and display the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
