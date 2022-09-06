#!/usr/bin/env python
import subprocess
subprocess.Popen("chmod +x ./bam2fa.sh", shell=True)
# Run the bash script
subprocess.run("./bam2fa.sh", shell=True)
#Give executable permission to kmer script
subprocess.Popen("chmod +x ./k-mer.sh", shell=True)
#Execute the k-mer script
subprocess.Popen("./k-mer.sh", shell=True)




#Docker refs
#https://medium.com/@chadlagore/conda-environments-with-docker-82cdc9d25754