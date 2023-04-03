#!/bin/bash
# Gets byte size of an http request
curl -s "$1" | wc -c
