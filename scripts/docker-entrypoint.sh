#!/bin/sh

_wait_connections() {
    cnt=5 # max retry times
    for i in $@; do
        host_port=${i//:/ }
        until echo $host_port | xargs nc -z -w 5
        do
            cnt=$(($cnt-1))
            (($cnt == 0)) && { echo "Connect to $host_port timeout, exit!!!" ; exit 1; }
            echo "Waiting delay for $i connection..."
            sleep 5
        done
        echo "Connection to $i is available"
    done
}

# ensure access to host by docker.host.internal
_check_host() {
    grep "docker.host.internal" /etc/hosts \
    || printf "`/sbin/ip route|awk '/default/ { print $3 }'`\tdocker.host.internal"  >> /etc/hosts
}

# start supervisord with nodaemon mode
_start_up() {
    supervisord -nc supervisord.conf
}

# normal startup the container
if [ "${1}" = '--wait' ]; then
    _check_host

    # delete first param --XXX
    conns=${@/$1}
    _wait_connections $conns

    # migrate database schema
    cd .. && python manage.py migrate && cd config

    _start_up
fi

# use to migrate
if [ "${1}" = '--migrate' ]; then
    _check_host
    # delete first param --XXX
    conns=${@/$1}
    # wait for the connection
    _wait_connections $conns

    cd .. && python manage.py migrate && cd config
fi

# execute user command
if [ "${1}" = '--exec' ]; then
    commad=${@/$1}
    sh -c "$commad"
fi

# default is doing nothing
if [ -z "$1" ]; then
    echo "doing nothing"
    exit 0
fi
