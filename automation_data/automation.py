#!/usr/bin/env python
import subprocess
subprocess.run("chmod +x ../script/bam2fa.sh", shell=True)
# Run the bash script
subprocess.run("../script/bam2fa.sh", shell=True)





#Docker refs
#https://medium.com/@chadlagore/conda-environments-with-docker-82cdc9d25754