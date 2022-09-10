#!/usr/bin/env python
import subprocess
import pickle
import pandas as pd
from dataframe import dataframe as df
# from dataframe import code_name

# subprocess.Popen("chmod +x ./bam2fa.sh", shell=True)
# # Run the bash script
# subprocess.run("./bam2fa.sh", shell=True)
# #Give executable permission to kmer script

# subprocess.Popen("chmod +x ./k-mer.sh", shell=True)
# #Execute the k-mer script
# subprocess.Popen("./k-mer.sh", shell=True)

# subprocess.Popen("chmod +x ./frequent_kmer.sh", shell=True)
# subprocess.Popen("./frequent_kmer.sh", shell=True)
# # create file list
subprocess.Popen("chmod +x ../path.sh", shell=True)
subprocess.Popen("../path.sh", shell=True)
col_df=pd.read_csv("../col_names",index_col="sample_id")


file=[]
with open("k_merfiles.txt") as f:
    for i in f:
        
        file.append(i.split(sep="\n")[0])
# print(file)   
for i in file:
    sample = i.split(sep="/")[-1]
    data_df = df(i)

    dff = pd.concat([col_df,data_df])
    dff.fillna(0,inplace=True,axis=1)

    for i in data_df.columns:
        if i not in dff.columns:
            dff.drop(columns=i,axis=1,inplace=True)
    #country={"MXL":0,"LWK":1,"GBR":2,"STU":3}

    with open("../MLRad.pkl","rb") as f:
        loaded_model = pickle.load(f)
        prediction = loaded_model.predict(dff)
    if prediction==0:
        print(prediction)
        print(f"sample {sample} is an American with (MXL) Mexican Ancestry origin with a probility of",max(loaded_model.predict_proba(dff)[0].tolist()))
    elif prediction==1:
        print(prediction)
        print(f"sample {sample} is an african with (LWK) Luhya in Webuye, Kenya origin with a probility of",max(loaded_model.predict_proba(dff)[0].tolist()))
    # print("This an african with (LWK) Luhya in Webuye, Kenya origin with prediction score of")#)#,loaded_model.score(y))
    elif prediction==2:
        print(prediction)
        print(f"sample {sample} is a British with GBR origin with a probility of",max(loaded_model.predict_proba(dff)[0].tolist()))
        # print("This an British with GBR origin with prediction score of")#,loaded_model.score(y))
    elif prediction==3:
        print(prediction)
        print(f"sample {sample} is an South Asian Ancestry with (STU) Tamil origin origin with a probility of",max(loaded_model.predict_proba(dff)[0].tolist()))
        # print("This an South Asian Ancestry with (STU) Tamil origin with prediction score of")#,loaded_model.score(y))



#Docker refs
#https://medium.com/@chadlagore/conda-environments-with-docker-82cdc9d25754