#!/usr/bin/env bash
mkdir -p frequentKmer
for i in `ls *.fa`
do
#out_file="`echo $i`_mers.fa"
awk '$2>=1000 {print $0}' ${i} >frequentKmer/${i}
done
# group samples by continent
# mkdir -p AFR EUR AMR
# mv frequentKmer/*.STU.* 
# mv frequentKmer/*.MXL.* AMR
# mv frequentKmer/*.KHV.* frequentKmer/*.ASW.* frequentKmer/*.LWK.* AFR