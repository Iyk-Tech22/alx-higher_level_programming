#!/urs/bin/env bash
# It sends a json post request to a given url with a given json file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
