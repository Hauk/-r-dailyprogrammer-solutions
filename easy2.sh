#!/bin/bash

#Untested but I'm sure it's fine!

# CD to the Oracle trace directory - Change to actual directory location.
cd opt/app/oracle/oradata/orcl/trace/

#Remove all trc files in the directory older than 10 days.
find . -name "*.trc" -mtime +35 -exec rm -rf  {} \;

echo "Removed all .trc files older than 10 days..."

#Remove all trm files in the directory older than 10 days.
find . -name "*.trm" -mtime +35 -exec rm -rf  {} \;

echo "Removed all .trm files older than 10 days..."

#Done
echo "Done."

