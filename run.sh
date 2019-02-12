#!/bin/bash

APP_PATH=`dirname $0`
cd ${APP_PATH}

option=$1
[ -z "$option" ] && option=start


start(){
    nohup ~/.local/bin/uwsgi --ini ${APP_PATH}/uwsgi.ini > ${APP_PATH}/geoip_uwsgi.log 2>&1 &
}

stop(){
    ~/.local/bin/uwsgi --stop /tmp/uwsgi50020.pid
    pkill -f uwsgi -9
}

case ${option} in
    start)
    echo "[*] Starting  Now......"
    start
    echo "[*] Starting  Finished"
    ;;
    stop)
    echo "[-] Stopping  Now......"
    stop
    echo "[-] Stopping  Finished"
    ;;
    restart)
    echo "[+] Restart  Now......"
    stop
    start
    echo "[+] Restart  Finished"
    ;;
    *)
esac
