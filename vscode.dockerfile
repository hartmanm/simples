
# Copyright (c) 2023 Michael Neill Hartman. All rights reserved.
# mnh_license@proton.me
# https://github.com/hartmanm

FROM ubuntu:jammy AS M
RUN cat <<EOF > /tmp/set_locale
#!/bin/bash
echo "en_US.UTF-8/" >> /etc/locale.gen
locale-gen
EOF
RUN chmod +x /tmp/set_locale
CMD ["./tmp/set_locale"]
RUN apt update -y 
RUN apt install -y wget
ARG CURRENT_RESOURCE=https://vscode.download.prss.microsoft.com/dbazure/download/stable/af28b32d7e553898b2a91af498b1fb666fdebe0c/code_1.85.0-1701895805_arm64.deb
RUN wget $CURRENT_RESOURCE
RUN apt install -y tilix
RUN apt install -y gpg
RUN apt install -y xdg-utils
RUN apt-get install -f -y ./code_1.85.0-1701895805_arm64.deb
# add user for code to use
RUN useradd -ms /bin/bash for_code
RUN echo 'for_code:is_the_code' | chpasswd
USER for_code
RUN mkdir /home/for_code/c
WORKDIR /home/for_code/c
# # context runner
# RUN cat <<EOF > /tmp/runner
# #!/bin/bash
# /usr/bin/./code
# EOF
# RUN chmod +x /tmp/runner

# open -a Docker\ Desktop.app; cd /Users/`whoami`/c; cp /Users/`whoami`/c/vscode.dockerfile /Users/`whoami`/c/Dockerfile; docker build . -t rcode:1; xhost + 127.0.0.1; (xterm -e "docker run -it -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix -v /Users/`whoami`/c:/home/for_code/c rcode:1 bash" &); while [[ "`docker ps | grep rcode:1`" == "" ]] ; do sleep 1 ;echo "waiting on code-container" ; done ; docker exec `docker ps | grep rcode:1  | awk '{print $1}'` code
