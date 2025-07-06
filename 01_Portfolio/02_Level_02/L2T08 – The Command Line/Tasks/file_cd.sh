#!/bin/bash

# The Command Line Task Point 1

clear
mkdir dir_one
mkdir dir_two
mkdir dir_three
cd dir_one
mkdir sub_dir_one
mkdir sub_dir_two
mkdir sub_dir_three
rmdir sub_dir_two
rmdir sub_dir_three

# I added another version in case you needed me to remove two of the initial 
# directories. the tasks notes are ambiguous and don't specify which folders 
# they would like us to remove.

# clear
# mkdir dir_one
# mkdir dir_two
# mkdir dir_three
# cd dir_one
# mkdir sub_dir_one
# mkdir sub_dir_two
# mkdir sub_dir_three
# cd ..
# rmdir dir_two
# rmdir dir_three
# ls