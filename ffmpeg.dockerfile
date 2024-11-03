
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
RUN apt install -y ffmpeg
# add user
RUN useradd -ms /bin/bash for_ops
RUN echo 'for_ops:is_the_code' | chpasswd
USER for_ops
RUN mkdir /home/for_ops/working
WORKDIR /home/for_ops/working

# open -a Docker\ Desktop.app; cd /Users/`whoami`/working; cp /Users/`whoami`/working/ffmpeg.dockerfile /Users/`whoami`/working/Dockerfile; docker build . -t ffmpeg:1; xhost + 127.0.0.1; (xterm -e "docker run -it -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix -v /Users/`whoami`/working:/home/for_ops/working ffmpeg:1 bash" &)

# ffmpeg -i 'New Recording 11.m4a' -t 600 -c copy 'New Recording 11_part1.m4a' -ss 600 -c copy 'New Recording 11_part2.m4a'
