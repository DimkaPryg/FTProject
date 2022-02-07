#!/bin/bash

# .pid file
pid_file="/var/run/secondscript.pid"

if [ -f $pid_file ]; then
  # Pid file exist. 
  exit
else
  # Create pid file 
  echo $$ > $pid_file
fi

check_dir="/local/backups/"
check_size=$(du -sb $check_dir | cut -f1)
check_number=$(ls $check_dir | wc -l)


if [ $check_size -gt $folder_size ]; then
  echo "Folder size is more than $folder_size ($check_size)"
fi

if [ $check_number -gt $files_count ]; then
  echo "Number of files in the folder is more than $files_count ($check_number)"
fi

# Clean up pid file
rm $pid_file