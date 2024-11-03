#!/bin/bash

# Copyright (c) Michael Neill Hartman. All rights reserved.
# mnh_license@proton.me
# https://github.com/hartmanm

HOST_DIRECTORY_TO_MOUNT=`pwd`

cat <<EOF > das_b
export DOCKER_BUILDKIT=1
cp das.dockerfile Dockerfile
docker build -t das_di:latest .
docker run                          \
-it                                 \
-p 3000:3000                        \
-v ${HOST_DIRECTORY_TO_MOUNT}:/da   \
das_di:latest
EOF

cat <<EOF > dav_b
export DOCKER_BUILDKIT=1
cp dav.dockerfile Dockerfile
docker build -t dav_di:latest .
docker run                          \
-it                                 \
-p 8080:8080                        \
-v ${HOST_DIRECTORY_TO_MOUNT}:/da   \
dav_di:latest
EOF

(bash das_b &)
#docker wait `docker ps -q`
(bash dav_b &)

#[[ -e Dockerfile ]] && rm Dockerfile
#[[ -d generated ]]  && rm -rf generated
