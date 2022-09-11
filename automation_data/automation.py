#!/usr/bin/env python
import subprocess
import pickle
import pandas as pd
from dataframe import dataframe as df
import time
start = time.time()
# from dataframe import code_name

# subprocess.Popen("chmod +x ./bam2fa.sh", shell=True)
# Run the bash script
# subprocess.run("./bam2fa.sh", shell=True)
#Give executable permission to kmer script

subprocess.run("chmod +x ./k-mer.sh", shell=True)
#Execute the k-mer script
subprocess.run("./k-mer.sh", shell=True)

subprocess.run("chmod +x ./frequent_kmer.sh", shell=True)
subprocess.run("./frequent_kmer.sh", shell=True)
# create file list
subprocess.run("chmod +x ./path.sh", shell=True)
subprocess.run("./path.sh", shell=True)
#column names in the dataframe
col_df=pd.read_csv("./col_names",index_col="sample_id")


file=[]
with open("k_merfiles.txt") as f:
    for i in f:
        # print(i)
        file.append(i.split(sep="\n")[0])
for i in file:
    sample = i.split(sep="/")[-1]
    data_df = df(i)

    dff = pd.concat([col_df,data_df])
    dff.fillna(0,inplace=True,axis=1)

    for i in data_df.columns:
        if i not in dff.columns:
            dff.drop(columns=i,axis=1,inplace=True)
    #country={"MXL":0,"LWK":1,"GBR":2}

    with open("./MLRad.pkl","rb") as f:
        loaded_model = pickle.load(f)
        prediction = loaded_model.predict(dff)
    if prediction==0:
        # print(prediction)
        print(f"sample {sample} is a Mexican origin with a prediction probility of",max(loaded_model.predict_proba(dff)[0].tolist()))
    elif prediction==1:
        # print(prediction)
        print(f"sample {sample} is a Luhya origin with a prediction probility of",max(loaded_model.predict_proba(dff)[0].tolist()))
    elif prediction==2:
        # print(prediction)
        print(f"sample {sample} is a British origin with a prediction probabirity of",max(loaded_model.predict_proba(dff)[0].tolist()))
    
end = time.time()
print(end-start)
#Docker refs
#https://medium.com/@chadlagore/conda-environments-with-docker-82cdc9d25754
