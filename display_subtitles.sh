#!/bin/bash

# Copyright (c) 2022 Michael Neill Hartman. All rights reserved.
# mnh_license@proton.me
# https://github.com/hartmanm

TARGET_VTT_DIRECTORY=${1}
PWD=`pwd`
SRC="${PWD}/${TARGET_VTT_DIRECTORY}/`ls ${TARGET_VTT_DIRECTORY} | grep vtt`"
echo $SRC

LENGTH=`wc -l ${SRC} | awk '{print $1}'`



# line iterator skip WEBVTT 
ITERATOR=3
# start at a given linenumber
##[[ ${2} != "" ]] && $ITERATOR=$((${2}-1+1))

AWAIT_NEXT=0

# initial starting time
START_TIME=`date | awk '{print $4}'`
HOUR=`echo $START_TIME | tr ':' ' ' | awk '{print $1}'`
MINUTE=`echo $START_TIME | tr ':' ' ' | awk '{print $2}'`
SECOND=`echo $START_TIME | tr ':' ' ' | awk '{print $3}'`

get_current_time_delta_from_start(){

DELTA_START_TIME=`date | awk '{print $4}'`
D_HOUR=`echo $DELTA_START_TIME | tr ':' ' ' | awk '{print $1}'`
D_MINUTE=`echo $DELTA_START_TIME | tr ':' ' ' | awk '{print $2}'`
D_SECOND=`echo $DELTA_START_TIME | tr ':' ' ' | awk '{print $3}'`

## deal with zeropad 
## TODO 24hr rollover
HOUR_DURATION=0
MINUTE_DURATION=$D_MINUTE
SECOND_DURATION=$D_SECOND
[[ $D_HOUR -gt $HOUR || $D_HOUR -eq $HOUR ]] && HOUR_DURATION=$(($D_HOUR-$HOUR))
[[ $D_MINUTE -gt $MINUTE || $D_MINUTE -eq $MINUTE  ]] && MINUTE_DURATION=$(($D_MINUTE-$MINUTE))
[[ $D_SECOND -gt $SECOND || $D_SECOND  -eq $SECOND   ]] && SECOND_DURATION=$(($D_SECOND-$SECOND))

HOURS_IN_SECONDS=$(($HOUR_DURATION * 60 * 60))
MINUTES_IN_SECONDS=$(($MINUTE_DURATION * 60))
FULL_DURATION_IN_SECONDS=$(($HOUR_DURATION + $MINUTE_DURATION + $SECOND_DURATION))


echo "$D_SECOND -gt $SECOND "

echo ${FULL_DURATION_IN_SECONDS}


} ## get_current_time_delta_from_start(){


#sleep 3
#get_current_time_delta_from_start


remove_zero_pad(){

#LENGTH_OF_INPUT=$((`echo $1 | wc -c`-1))
NO_PAD=${1}

[[ ${NO_PAD:0:1} == "0" ]] && NO_PAD=${NO_PAD:1:1}

echo $NO_PAD
}

get_duration_of_subtitle(){
START_TIME_OF_SUBTITLE=`head -$ITERATOR ${SRC} | tail -1 | awk '{print $1}'`
END_TIME_OF_SUBTITLE=`head -$ITERATOR ${SRC} | tail -1 | awk '{print $NF}'`

# start time segments
SS_HOUR=`echo ${START_TIME_OF_SUBTITLE} | tr ':' ' ' | awk '{print $1}'`
SS_MINUTE=`echo ${START_TIME_OF_SUBTITLE} | tr ':.' ' ' | awk '{print $2}'`
SS_SECOND=`echo ${START_TIME_OF_SUBTITLE} | tr ':.' ' ' | awk '{print $3}'`




SS_HOUR=`remove_zero_pad $SS_HOUR`
SS_MINUTE=`remove_zero_pad $SS_MINUTE`
SS_SECOND=`remove_zero_pad $SS_SECOND`


SS_HOUR=$(($SS_HOUR+1-1))
SS_MINUTE=$(($SS_MINUTE+1-1))
SS_SECOND=$(($SS_SECOND+1))

# end time segments
SE_HOUR=`echo ${END_TIME_OF_SUBTITLE} | tr ':' ' ' | awk '{print $1}'`
SE_MINUTE=`echo ${END_TIME_OF_SUBTITLE} | tr ':.' ' ' | awk '{print $2}'`
SE_SECOND=`echo ${END_TIME_OF_SUBTITLE} | tr ':.' ' ' | awk '{print $3}'`


SE_HOUR=`remove_zero_pad $SE_HOUR`
SE_MINUTE=`remove_zero_pad $SE_MINUTE`
SE_SECOND=`remove_zero_pad $SE_SECOND`


SE_HOUR=$(($SE_HOUR+1-1))
SE_MINUTE=$(($SE_MINUTE+1-1))
SE_SECOND=$(($SE_SECOND+1))

HOUR_DURATION=$(($SE_HOUR-$SS_HOUR))
MINUTE_DURATION=$(($SE_MINUTE-$SS_MINUTE))
SECOND_DURATION=$(($SE_SECOND-$SS_SECOND))


#get_current_time_delta_from_start
#[[ $HOUR_DURATION -gt 0 ]]

## TODO do more than assume its only seconds
echo $SECOND_DURATION
} ## get_duration_of_subtitle(){

get_next_subtitle(){
CURRENT_SUBTITLE=/tmp/current_subtitle
> $CURRENT_SUBTITLE
LINE="aa"
while [[ `echo $LINE | grep -e "-->"` != "" ]]
do
LINE=`head -$ITERATOR ${SRC} | tail -1`
ITERATOR=$(($ITERATOR+1))
done

ITERATOR=$(($ITERATOR+1))

AWAIT_NEXT=`get_duration_of_subtitle`



ITERATOR=$(($ITERATOR+1))

LINE="aa"
while [[ $((`echo $LINE | wc -c`)) -gt 1 ]]
do
LINE=`head -$ITERATOR ${SRC} | tail -1`
echo ${LINE} >> $CURRENT_SUBTITLE


ITERATOR=$(($ITERATOR+1))
done

cat $CURRENT_SUBTITLE | tr '\n' ' '
echo "








"


} ## get_next_subtitle(){


while [[ $ITERATOR -lt $LENGTH+1 ]]
do
get_next_subtitle

sleep $AWAIT_NEXT



done
