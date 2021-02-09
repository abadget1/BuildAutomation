#!/bin/bash
function jumpstart() {
    cd ~/Desktop
    python3 jumpstart.py $1
    # mkdir ~/Desktop/Web/BuildAutomation/$1
    # cd ~/Desktop/Web/BuildAutomation/$1
    # git init
    # git remote add origin https://github.com/$GIT_USERNAME/$1.git
    # git add .
    # touch READ.md
    # git commit -m "first commit"
    # git push -u origin main
    # code .
}