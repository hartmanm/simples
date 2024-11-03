#!/bin/bash

# Copyright (c) 2022 Michael Neill Hartman. All rights reserved.
# mnh_license@proton.me
# https://github.com/hartmanm

# generate_sim_results_csv.sh

# use DecodeKeys_Animal.txt and log_*_READABLE.txt to generate a csv per animal
# for "timestamp,temperature,distance,location_x,location_y,bpm" 
# denomalize 1 csv per animal using timestamp as primary key for index

# choose TARGET_ANIMAL as
# Zebra
# Lion
# Elephant

TOP_LEVEL=`pwd`
WHOAMI=`whoami`
TARGET_LEY_FILE=${TOP_LEVEL}/SimResults/DecodeKeys_Animal.txt
ZEBRAS=`grep Zebra ${TARGET_LEY_FILE} | tr -d '":' | awk '{print $1}'`
LIONS=`grep Lion ${TARGET_LEY_FILE} | tr -d '":' | awk '{print $1}'`
ELEPHANTS=`grep Elephant ${TARGET_LEY_FILE} | tr -d '":' | awk '{print $1}'`

TARGET_FILE=${TOP_LEVEL}/SimResults/log_*_READABLE.txt

# Zebra
# Lion
# Elephant
TARGET_ANIMAL=Elephant

TARGET_LIST=
[[ ${TARGET_ANIMAL} == 'Zebra' ]] && TARGET_LIST=${ZEBRAS}
[[ ${TARGET_ANIMAL} == 'Lion' ]] && TARGET_LIST=${LIONS}
[[ ${TARGET_ANIMAL} == 'Elephant' ]] && TARGET_LIST=${ELEPHANTS}
mkdir -p ${TOP_LEVEL}/generated_${TARGET_ANIMAL}
for ANIMAL in `echo $TARGET_LIST`
do
echo "processing $ANIMAL from `echo $TARGET_LIST`"
echo "timestamp,temperature,distance,location_x,location_y,bpm" > ${TOP_LEVEL}/generated_${TARGET_ANIMAL}/animal_${ANIMAL}
TIMESTAMP=
TEMPATURE=
DISTANCE=
LOCATION_X=
LOCATION_Y=
BPM=
TIMESTAMPS=
TEMPATURES=
DISTANCES=
LOCATION_X_S=
LOCATION_Y_S=
BPMS=

echo ${TOP_LEVEL}/generated_${TARGET_ANIMAL}/animal_${ANIMAL}

# generate animal results file
grep -A 11 ${TARGET_ANIMAL}-${ANIMAL} ${TARGET_FILE} > /tmp/${WHOAMI}_animal_${ANIMAL}
# generate column results lists
TIMESTAMPS=`grep -n Timestamp /tmp/${WHOAMI}_animal_${ANIMAL} | awk '{print $NF}'`
TEMPATURES=`grep -n temperature /tmp/${WHOAMI}_animal_${ANIMAL} | awk '{print $NF}'`
DISTANCES=`grep -n distance /tmp/${WHOAMI}_animal_${ANIMAL} | awk '{print $NF}'`
LOCATION_X_S=`grep -n location /tmp/${WHOAMI}_animal_${ANIMAL} | awk '{print $2}' | tr -d "[,"`
LOCATION_Y_S=`grep -n location /tmp/${WHOAMI}_animal_${ANIMAL} | awk '{print $NF}' | tr -d "]"`
BPMS=`grep -n pulseOxygen /tmp/${WHOAMI}_animal_${ANIMAL} | awk '{print $3}' | tr -d "[,"`

# find length
LENGTH=0
for RESULT in ${TIMESTAMPS}
do
LENGTH=$(($LENGTH +1))
done
LENGTH=$(($LENGTH -1))
echo $LENGTH

# generate results csv for animal
ITERATOR=1
while [[ $ITERATOR -lt $LENGTH ]]
do
[[ $(($ITERATOR % 500)) -eq 0 ]] && echo "$ITERATOR -lt $LENGTH"
TIMESTAMP=`echo ${TIMESTAMPS} | awk -v i=$ITERATOR '{print $i}'`
TEMPATURE=`echo ${TEMPATURES} | awk -v i=$ITERATOR '{print $i}'`
DISTANCE=`echo ${DISTANCES} | awk -v i=$ITERATOR '{print $i}'`
LOCATION_X=`echo ${LOCATION_X_S} | awk -v i=$ITERATOR '{print $i}'`
LOCATION_Y=`echo ${LOCATION_Y_S} | awk -v i=$ITERATOR '{print $i}'`
BPM=`echo ${BPMS} | awk -v i=$ITERATOR '{print $i}'`
IS_OK=0
[[ ${TIMESTAMP} != '"NaN"' ]] && {
[[ ${TEMPATURE} != '"NaN"' ]] && {
[[ ${DISTANCE} != '"NaN"' ]] && {
[[ ${LOCATION_X} != '"NaN"' ]] && {
[[ ${LOCATION_Y} != '"NaN"' ]] && {
[[ ${BPM} != '"NaN"' ]] && {
[[ ${TIMESTAMP} != "" ]] && {
[[ ${TEMPATURE} != "" ]] && {
[[ ${DISTANCE} != "" ]] && {
[[ ${LOCATION_X} != "" ]] && {
[[ ${LOCATION_Y} != "" ]] && {
[[ ${BPM} != "" ]] && {
IS_OK=1
echo "${TIMESTAMP},${TEMPATURE},${DISTANCE},${LOCATION_X},${LOCATION_Y},${BPM}" >> ${TOP_LEVEL}/generated_${TARGET_ANIMAL}/animal_${ANIMAL}
}
}
}
}
}
}
}
}
}
}
}
}
[[ $IS_OK -eq 0 ]] && echo "error on $ITERATOR : ${TIMESTAMP},${TEMPATURE},${DISTANCE},${LOCATION_X},${LOCATION_Y},${BPM}"
ITERATOR=$(($ITERATOR +1))
done
head -10 ${TOP_LEVEL}/generated_${TARGET_ANIMAL}/animal_${ANIMAL}
echo "..."
tail -10 ${TOP_LEVEL}/generated_${TARGET_ANIMAL}/animal_${ANIMAL}
done
echo "complete"
