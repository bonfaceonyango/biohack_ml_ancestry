#!/usr/bin/env bash
cd consensus_auto/27_mers
mkdir -p frequentKmer
for i in `ls *.fa`
do
#out_file="`echo $i`_mers.fa"
awk '$2>=1000 {print $0}' ${i} >frequentKmer/${i}
done
cd -