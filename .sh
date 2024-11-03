#!/bin/bash

# Copyright (c) 2020 Michael Neill Hartman. All rights reserved.
# mnh_license@proton.me
# https://github.com/hartmanm

# invoke with as-such-invoke

# cd /workspaces/relata
# bash r ${@};
# alias r="bash /workspaces/relata/r ${@}"

echo "${#@} ${@}"

EXEC=0

#### exec loop
COUNT=1
for ITEM in ${@}
do 
IS_EXEC=$(awk '{print $1}' database | grep -nw ${ITEM}  | tr ':' ' ' | awk '{print $1}')
[[ ${IS_EXEC} != "" ]] && {
EXEC=1
echo "
executing parameter $COUNT: $ITEM

------------------------------
"
head -$IS_EXEC database | tail -1 | cut -f1,2 -d" " --complement
(`head -$IS_EXEC database | tail -1 | cut -f1,2 -d" " --complement`)
echo "

------------------------------
"

} ## [[ ${IS_EXEC} != "" ]] && {
COUNT=$(($COUNT+1))
done ## for ITEM in ${@}

#echo "exec loop complete"

#### add note group
DTG=$(date | tr ': ' '_')
IS_NOTE=0
NOTE=""
COUNT=1
for ITEM in ${@}
do 
[[ $IS_NOTE -eq 1 ]] && NOTE="${NOTE} ${ITEM}"
[[ ${ITEM} == "note" ]] && IS_NOTE=1
COUNT=$(($COUNT+1))
done ## for ITEM in ${@}
[[ $IS_NOTE -eq 1 ]] && {
echo "" >> database 
echo "${DTG} note${NOTE}" >> database 
echo "
added note:

------------------------------


${DTG} note${NOTE}


------------------------------

"
}

#echo "add note loop complete"


#### get notes group
for ITEM in ${@}
do 
[[ ${ITEM} == "notes" ]] && {
echo "
"
grep note database | grep -v "#" | cut -f1,2 -d" " --complement > /tmp/notes
LONGEST=$(awk '{print $1}' /tmp/notes)
LENGTH=1
for TOKEN in ${LONGEST}; do [[ $((${#TOKEN})) -gt $LENGTH ]] && LENGTH=$((${#TOKEN})); done
COUNT=$((`wc -l /tmp/notes | awk '{print $1}'`))
while [[ $COUNT -gt 0 ]]
do
OUT=$(head -$(($COUNT*1)) /tmp/notes | tail -1 | awk '{print $1}')
WHITE_SPACE=$(($LENGTH-$((${#OUT}))+$LENGTH))
SPACE=" "
OUT_SPACE=""
while [[ $WHITE_SPACE -gt 0 ]]; do OUT_SPACE="${OUT_SPACE}${SPACE}"; WHITE_SPACE=$(($WHITE_SPACE-1)); done
OUT="${OUT}"
OUT_2=$(head -$(($COUNT*1)) /tmp/notes | tail -1 | cut -f1 -d" " --complement)
echo "${OUT}${OUT_SPACE}${OUT_2}
"
COUNT=$(($COUNT-1))
done ## while [[ $COUNT -gt 0 ]]
}
echo "
"
done ## for ITEM in ${@}


#### produce repository hash and hash list
#### remove previous directory hash
#TOP_LEVEL=$(ls)
#LAST=""
#for ITEM in ${TOP_LEVEL}
#do
#[[ $((${#ITEM})) -gt 15 ]] && {
#rm ${ITEM}
#LAST=${ITEM}
#} ## [[ $((${#ITEM})) -gt 15 ]] && {
#done ## for ITEM in ${TOP_LEVEL}

[[ $EXEC -eq 0 ]] && {

HASHLIST=$(md5sum `du -a | awk '{print $2}'` 2>/dev/null)
#md5sum `du -a | awk '{print $2}'` 2>/dev/null > hash_list

#LENGTH_F=$(($(wc -l hash_list | awk '{print $1}')))
LENGTH_V=$(($(echo "${TEMP_STORE}" | wc -l  )-1))

#LINE_F=$(head -1 hash_list | tail -1)
LINE_V=$(echo "${HASHLIST}" | head -1 | tail -1)

TEMP_STORE=""
INDEX=1
LENGTH=$(($(echo "${HASHLIST}" | wc -l  )-1))
while [[ $INDEX -lt $LENGTH ]] 
do
LINE=$(echo "${HASHLIST}" | head -$INDEX | tail -1)
IS_EXCLUDE=$(echo ${LINE} | grep ".git")
[[ ${IS_EXCLUDE} == "" ]] && {
TEMP_STORE="${TEMP_STORE}
${LINE}"
} ## && [[ ${IS_EXCLUDE} == "" ]] && {
INDEX=$(($INDEX+1))
done ##  [[ $INDEX -lt $LENGTH ]] 
HASHLIST=$(echo "${TEMP_STORE}")

HASH=`echo "${HASHLIST}" | md5sum | awk '{print $1}'`
LAST=$(tail -1 hash_list)
echo "${HASHLIST}" > hash_list
echo "${HASH}" >> hash_list

[[ ${LAST} != ${HASH} ]] && echo "modified since ${LAST}"
echo "
               ${HASH}"
echo ""
} ## [[ $EXEC -ne 1 ]] && {


exec true

#for ITEM in ${@}; do echo "${ITEM} is "; done

[[ ${#@} -gt 1 ]] && for ITEM in ${@}; do echo "${ITEM} is "; done

#for mac
[[ ${#@} -gt 0 ]] && cd ${1}; md5 `du -a | awk '{print $2}'` 2>/dev/null  > /tmp/1; DH=`md5 /tmp/1 | awk  '{print $4}'`; echo ${DH}
