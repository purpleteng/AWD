#!/bin/bash
time=`date "+%F%T"`
bak_file="/"$time".tar.gz"
web_dir="/var/www/html/"
tar -zcvf $bak_file $web_dir >/dev/null 2>&1 &

# crontab 
# */5 * * * * /bin/sh /bak.sh