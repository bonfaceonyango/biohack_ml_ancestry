import subprocess

#make file executable
subprocess.Popen("chmod +x ../script/bam2fa.sh", shell=True)
# Export conda Environment
#subprocess("conda env create -f  ml_ancestry_conda.yml",shell=True) # 

# Activate conda environment 
subprocess("conda activate ml_ancestry_conda",shell=True) # Activate your conda environment 
# Generate concessus sequence from bam file
subprocess.Popen(["../script/bam2fa.sh"]) # bash script has shebang, hence avoid shell =True