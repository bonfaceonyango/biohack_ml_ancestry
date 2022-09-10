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
Export tools from configuration file to set up the conda environment.
```
conda export machine_learning.yml
conda activate machine_learning
```
# Usage

# Contributors
- Henry Ndugwa
- Bonface Onyango
