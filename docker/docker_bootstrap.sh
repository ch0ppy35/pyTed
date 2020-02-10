#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

runuser -l postgres -c '/usr/lib/postgresql/9.6/bin/postgres -D /var/lib/postgresql/9.6/main -c config_file=/etc/postgresql/9.6/main/postgresql.conf' &
sleep 4
python3.6 -m flask run