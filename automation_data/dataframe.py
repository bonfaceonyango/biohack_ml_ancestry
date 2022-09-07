import pandas as pd
import pickle
code_name =[]
def dataframe(filename):
    """
    generate a data from frequent k-mer
    filename: file containing k-mers
    returns: a dataframe
    """
    ID,code = filename.split(sep=".")[0],filename.split(sep=".")[4] # ID sample name, code country code as of 1000geneomes
    code_name.append(code)
    
    with open(filename) as file:

        k_mer ={}
        for line in file:
            col,row=line.split()[0],line.split()[1]
            k_mer[col]=row
        #create a dataframe from k-mer dictionary
        df = pd.DataFrame.from_dict(k_mer,orient="index")
        #transpose the data frame where k-mers are the features and add country codes
        dft=df.transpose() 
        # dft["code"] = code
        dft["sample_id"]=ID
        df=dft.set_index("sample_id")
    
    return df
        