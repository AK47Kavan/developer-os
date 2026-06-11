#!/bin/bash

mkdir -p data


cat > data/system.json <<EOF
{
 "os": "$(sw_vers -productVersions)",
 "kernel": "$(uname -r)",
 "uptime": "$(uptime)",
 "brew_packages": "$(brew list | wc -l | td -d ' ')"
}
EOF
