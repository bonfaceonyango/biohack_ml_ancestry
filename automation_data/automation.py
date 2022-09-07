#!/usr/bin/env python
import subprocess
import pickle
import pandas as pd
from dataframe import dataframe as df
# from dataframe import code_name

subprocess.Popen("chmod +x ./bam2fa.sh", shell=True)
# Run the bash script
subprocess.run("./bam2fa.sh", shell=True)
#Give executable permission to kmer script

subprocess.Popen("chmod +x ./k-mer.sh", shell=True)
#Execute the k-mer script
subprocess.Popen("./k-mer.sh", shell=True)

subprocess.Popen("chmod +x ./frequent_kmer.sh", shell=True)
subprocess.Popen("./frequent_kmer.sh", shell=True)

col_df=pd.read_csv("col_names",index_col="sample_id")
data_df = df("consensus_auto/27_mers/frequentKmer/HG02061.mapped.ILLUMINA.bwa.KHV.exome.20120522.fa_27_mers.fa")

dff = pd.concat([col_df,data_df])
dff.fillna(0,inplace=True,axis=1)

for i in data_df.columns:
    if i not in dff.columns:
        dff.drop(columns=i,axis=1,inplace=True)
#country={"MXL":0,"LWK":1,"GBR":2,"STU":3}

with open("ANCmodel.pkl","rb") as f:
    loaded_model = pickle.load(f)
prediction = loaded_model.predict(dff)
if prediction==0:
    print(prediction)
    print("This an American with (MXL) Mexican Ancestry origin with prediction score of")#,loaded_model.score(y))
elif prediction==1:
    print(prediction)
    print("This an african with (LWK) Luhya in Webuye, Kenya origin with prediction score of")#)#,loaded_model.score(y))
elif prediction==2:
    print(prediction)
    print("This an British with GBR origin with prediction score of")#,loaded_model.score(y))
elif prediction==3:
    print(prediction)
    print("This an South Asian Ancestry with (STU) Tamil origin with prediction score of")#,loaded_model.score(y))

#Docker refs
#https://medium.com/@chadlagore/conda-environments-with-docker-82cdc9d25754