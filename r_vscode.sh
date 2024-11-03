#!/bin/bash

# Copyright (c) 2023 Michael Neill Hartman. All rights reserved.
# mnh_license@proton.me
# https://github.com/hartmanm

# r_vscode
# requires docker and brew->xquartz
# hardcodes
GET_PASSWORD=0
(open -a xquartz &)         # prestart xquartz
(open -a Docker\ Desktop &) # start docker desktop
# stop old code-servers
while [[ "`docker ps | grep codercom/code-server`" != "" ]]
do
sleep 1
echo "stopping old code-server"
docker kill `docker ps | grep codercom/code-server | awk '{print $1}'`
done
# ensure Docker Desktop is running
while [[ "`ps -ef | grep "Docker Desktop"`" == "" ]]
do
sleep 1
echo "starting Docker Desktop"
(open -a Docker\ Desktop &) # start docker desktop
done
# generate code-server spawnfiles
docker pull codercom/code-server
OPWD=`pwd`
cat > /tmp/code_server <<EOF
#!/bin/bash
docker run -it -p 127.0.0.1:8080:8080 -v "$OPWD:/home/coder" codercom/code-server
EOF
cat > /tmp/run_code_server <<EOF
#!/bin/bash
bash /tmp/code_server
EOF
(xterm -e bash /tmp/run_code_server &)
# wait for server to be serving
while [[ "`docker ps | grep codercom/code-server`" == "" ]]
do
sleep 1
echo "waiting on code-server"
done
sleep 1
# launch browser
open -a Safari http://127.0.0.1:8080
[[ $GET_PASSWORD -eq 1 ]] && {
# get password from container when ready
docker exec `docker ps | grep codercom/code-server | awk '{print $1}'` cat /home/coder/.config/code-server/config.yaml | grep "password:" | awk '{print $2}' | tr -d '/n' 1>/tmp/watch_error
echo "" > /tmp/watch_error
while [[ "`awk '{print $1}' /tmp/watch_error | wc -c | grep 25`" == "" ]]
do
sleep 1
echo "waiting on code-server"
docker exec `docker ps | grep codercom/code-server | awk '{print $1}'` cat /home/coder/.config/code-server/config.yaml | grep "password:" | awk '{print $2}' | tr -d '/n' 1>/tmp/watch_error
done
cat /tmp/watch_error
}
