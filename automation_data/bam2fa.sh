#! /usr/bin/env bash
#import sys
# run in directory containing the data
SECONDS=0   
# index the referece genome
#echo "Indexing refence file"
# bwa index hs37d5.fa
#samtools faidx hs37d5.fa
mkdir -p consensus_auto
#generate vcf 
for i in `ls *.bam`
do
outfile=`basename $i .bam`.vcf
echo "Creating index of $i"
samtools index $i
echo "Creating $outfile"

freebayes -f hs37d5.fa $i >${outfile}

out_gz=`basename $i .bam`.vcf.gz
echo "Creating $out_gz"
bgzip ${outfile} 

# indexing the vcf
echo "indexing  $outfile"
tabix -fp vcf ${out_gz} 

echo "$out_gz"
out_fa=`basename $i .bam`.fa
echo "generating consensus_auto ${out_fa}"

cat hs37d5.fa | bcftools consensus ${out_gz}> consensus_auto/${out_fa}

echo "Completed runing $i in $SECONDS seconds"
done
#timing the run time
if (( $SECONDS > 3600 )) ; then
    let "hours=SECONDS/3600"
    let "minutes=(SECONDS%3600)/60"
    let "seconds=(SECONDS%3600)%60"
    echo "Completed in $hours hour(s), $minutes minute(s) and $seconds second(s)" 
elif (( $SECONDS > 60 )) ; then
    let "minutes=(SECONDS%3600)/60"
    let "seconds=(SECONDS%3600)%60"
    echo "Completed in $minutes minute(s) and $seconds second(s)"
else
    echo "Completed in $SECONDS seconds"
fi

