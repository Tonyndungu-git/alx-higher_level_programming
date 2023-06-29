#!/bin/bash
#sends a GET request to the URL with a custom header, and displays the body
header="X-School-User-Id: 98"; curl -s -H "$header" "$1"
