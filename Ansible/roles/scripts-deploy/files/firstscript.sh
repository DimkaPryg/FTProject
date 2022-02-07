#!/bin/bash

# change work directory
cd files 
file_name=""

# if file exist return file_name_i (e.g. file_name_1, file_name_2)
function setName() {
  local is_exist=true
  local i=1
  if [ ! -f "$1$2" ]; then
     file_name=$1
     return 1
  fi
  while [ "$is_exist" = true ]
    do
      i=$((i+1))
      if [ ! -f "$1_$i$2" ]; then
         is_exist=false
         file_name="$1_$i"
         return 1
      fi
    done
}

# create data file
setName "data_$(date +"%Y-%m-%d")" ""
curl http://localhost/articles/ > "$file_name"

# create dump arhive
if [ $(ls | wc -l) -eq 4 ]; then
   cd /local/backups/
   setName "dump_$(date +"%Y-%m-%d")" ".tar"
   tar zcf "$file_name.tar" /local/files/
   rm -R /local/files/*
fi