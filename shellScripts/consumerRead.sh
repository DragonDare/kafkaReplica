#!/bin/sh

export BROKER_FAIL=500
export TOPIC_FAIL=100

a=""
p=$1
s=$2

cd

while true
do
	if [[ ~/brokerFS/$p/partition1_3.txt ]] then
		if [[ $s == "--from-beginning" ]]
		then
			cat ~/brokerFS/$p/tempWhole.txt
			break
		else
			cat ~/brokerFS/$p/temp.txt
			break
		fi	
	fi
done

cd De*/B*/she*
	
