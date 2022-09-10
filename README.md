# Pipeline for prediction of ancestry using whole exom data: African Talent 2022 Biohack 
Ancestry prediction is important in forensic analysis, Genome wide association studies ,evolutionary Biology and it provide information about geographic origin. 
#  Workflow
- BAM files are the input for the pipeline
- Generate a data frame using k-mers
- dimensional reduction
- model training
- model evalution
- model testing 
- model saving
- model deployment
# setting up conda environment
Export tools from configuration file [here](https://github.com/bonfaceonyango/biohack_ml_ancestry/blob/main/conda_env/conda_env.yml) to set up the conda environment.
```
conda env create -f conda_env.yml
conda activate conda_env
```
# Usage

# Contributors
- Henry Ndugwa
- Bonface Onyango
