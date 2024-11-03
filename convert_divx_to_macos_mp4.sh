#/bin/bash

# Copyright (c) 2022 Michael Neill Hartman. All rights reserved.
# mnh_license@proton.me
# https://github.com/hartmanm

# convert_divx_to_macos_mp4

# for ubuntu / else install ffmpeg before running this script

INPUT_VIDEO_DIRECTORY_FULLPATH=/home/test/home_movies
OUTPUT_VIDEO_DIRECTORY_FULLPATH=/home/test/ffmpeg

LOG_FILE=${OUTPUT_VIDEO_DIRECTORY_FULLPATH}/run_log_`date | tr ': ' '_'`
START_TIME=`date`
echo "START_TIME : ${START_TIME}" 
echo "START_TIME : ${START_TIME}" > ${LOG_FILE}
[[ `which ffmpeg` == "" ]] && sudo apt install -y ffmpeg
[[ ! -d ${OUTPUT_VIDEO_DIRECTORY_FULLPATH} ]] && mkdir -p ${OUTPUT_VIDEO_DIRECTORY_FULLPATH}
for VIDEO in `ls $INPUT_VIDEO_DIRECTORY_FULLPATH`
do
VIDEO_WITH_NEW_EXTENSION="`echo ${VIDEO} | tr '.' ' ' | awk '{print $1}'`.mp4"
[[ ! -e ${OUTPUT_VIDEO_DIRECTORY_FULLPATH}/${VIDEO_WITH_NEW_EXTENSION} ]] && {
echo "
starting at `date`
time ffmpeg -i ${INPUT_VIDEO_DIRECTORY_FULLPATH}/${VIDEO} -c:v libx265 -tag:v hvc1 -f mp4 $OUTPUT_VIDEO_DIRECTORY_FULLPATH/${VIDEO_WITH_NEW_EXTENSION}
"
echo "
starting at `date`
time ffmpeg -i ${INPUT_VIDEO_DIRECTORY_FULLPATH}/${VIDEO} -c:v libx265 -tag:v hvc1 -f mp4 $OUTPUT_VIDEO_DIRECTORY_FULLPATH/${VIDEO_WITH_NEW_EXTENSION}
" >> ${LOG_FILE}
time ffmpeg -i ${INPUT_VIDEO_DIRECTORY_FULLPATH}/${VIDEO} -c:v libx265 -tag:v hvc1 -f mp4 $OUTPUT_VIDEO_DIRECTORY_FULLPATH/${VIDEO_WITH_NEW_EXTENSION}
echo "
completed at `date`
time ffmpeg -i ${INPUT_VIDEO_DIRECTORY_FULLPATH}/${VIDEO} -c:v libx265 -tag:v hvc1 -f mp4 $OUTPUT_VIDEO_DIRECTORY_FULLPATH/${VIDEO_WITH_NEW_EXTENSION}
"
echo "
completed at `date`
time ffmpeg -i ${INPUT_VIDEO_DIRECTORY_FULLPATH}/${VIDEO} -c:v libx265 -tag:v hvc1 -f mp4 $OUTPUT_VIDEO_DIRECTORY_FULLPATH/${VIDEO_WITH_NEW_EXTENSION}
" >> ${LOG_FILE}
sleep 1
}
done
END_TIME=`date`
echo "END_TIME : ${END_TIME}" 
echo "END_TIME : ${END_TIME}" >> ${LOG_FILE}
