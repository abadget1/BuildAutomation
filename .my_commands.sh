#!/bin/bash
function jumpstart() {
    cd ~
    python3 $PATH/jumpstart.py $1
    mkdir ~/Desktop/$1
    cd ~/Desktop/$1
    git init
    git remote add $1 https://github.com/$GIT_USERNAME/$1.git
    git add .
    touch READ.md
    git commit -m "first commit"
    git push -u $1 master
    code .
}
