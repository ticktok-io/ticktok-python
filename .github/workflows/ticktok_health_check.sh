#!/usr/bin/env bash

set -e

check_health() {
    echo checking health...
    until [[ $(curl --silent  --fail $1/mgmt/health/ 2>&1 | grep '"UP"') != "" ]]; do
        sleep 1
    done
    echo $1 is healthy!
}

timeout 10 check_health http://localhost:9643