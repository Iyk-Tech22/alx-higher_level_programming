#!/bin/bash
# It takes in a url as an argument and makes a get request to the url and display the body of the response
curl -sX GET $1 -H "X-School-User-Id: 98" -L
