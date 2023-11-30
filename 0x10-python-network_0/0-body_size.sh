#!/bin/bash
# send a request to an URL with curl, and show body size of the response
curl -s "$1" | wc -c
