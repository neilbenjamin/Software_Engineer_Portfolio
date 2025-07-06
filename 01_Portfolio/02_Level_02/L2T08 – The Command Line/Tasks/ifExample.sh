#!/bin/bash

# Solution courtesy of stack-overflow
# The command line  - Point 2 & 2.1

clear
if [ -d "new_folder" ]; 
then mkdir "if_folder"
    if [ -d "if_folder" ];
    then mkdir "hyperionDev"
    fi
else mkdir "new-projects"
fi