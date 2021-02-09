#!/bin/bash
function jumpstart() {
    cd ~
    python3 /Users/Aaron/Desktop/Web/BuildAutomation/$1
    mkdir ~/Desktop/$1
    cd ~/Desktop/$1
    git init
    git remote add $1 https://github.com/abadget1/$1.git
    git add .
    touch READ.md
    git commit -m "first commit"
    git push -u $1 master
    code .
}
