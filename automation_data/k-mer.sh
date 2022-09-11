#!/usr/bin/env bash
cd "consensus_auto/"
for k in 27
do
kmer_prof_dir="${k}_mers/"

mkdir -p ${kmer_prof_dir}


#    Generate k-mers
for sample in `ls *.fa`
do
echo "starting generating kmers for $sample"
sample_file="${sample}"

jf_file="${kmer_prof_dir}${sample}_${k}_mers.jf"
fa_file="${kmer_prof_dir}${sample}_${k}_mers.fa"


jellyfish count ${sample_file} -m ${k} -s 100M -t 50 -L 10 -C --disk -o ${jf_file}

jellyfish dump ${jf_file} > ${fa_file} -c


rm ${jf_file}
echo "completed generating kmers for $sample"
done


done

cd -


