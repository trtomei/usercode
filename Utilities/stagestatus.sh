#!/bin/bash

# Boilerplate
# Check for arguments
if [ $# -ne 4 ]; then
    echo Usage:$0 DIRECTORY EXPRESSION MINSIZE OUTFILENAME
    exit 127
fi

# First, let's get how many files are actually good (non-zero size).
# $1 is the directory to be listed, $2 is the argument to grep 
# (the files to be searched), $3 is the minimum file size.
# We dump the file list to raw.list
AWKARG="\$5 > $3 {print \$9}"
rfdir $1 | grep $2 | awk "$AWKARG" > raw.list
GOODFILES=`cat raw.list | wc -l`
echo $GOODFILES "good files found in" $1

# Let's check the status of all those files, and dump to tmp
python checkmyfiles.py $1 > tmp

# Let's check how many of those are STAGED, and put the result
# in the file indicated by $4
cat tmp | grep STAGED | awk '{print $1}' | sed 's!/castor!'\''rfio:/castor!g' | sed 's/root/root'\'',/g' | sed '$s/,$//' > $4

# For the number of staged files 
STAGEDFILES=`cat $4 | wc -l`
echo $STAGEDFILES "staged files. The list is in" $4

# Clean up tmp
rm tmp

exit 0
