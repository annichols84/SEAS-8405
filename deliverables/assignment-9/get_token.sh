#!/bin/bash

curl -X POST "http://localhost:8080/realms/IAM-Project/protocol/openid-connect/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "client_id=flask-app" \
     -d "username=test-user" \
     -d "password=test" \
     -d "grant_type=password"
