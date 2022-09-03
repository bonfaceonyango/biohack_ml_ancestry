import getopt, sys, subprocess,os

# # Remove 1st argument from the
# # list of command line arguments
# argumentList = sys.argv[1:]
 
# # Options
# options = "hf:"
# # Long options
# long_options = ["help", "folder"]
 
# try:
#     # Parsing argument
#     arguments, values = getopt.getopt(argumentList, options, long_options)
#     #print(argument) # [-f ,file.bam]
     
#     # checking each argument
#     for currentArgument, currentValue in arguments:
#        # print(currentValue) file.bam
#         if currentArgument in ("-h", "--help"):
#             print ("Displaying Help")
             
#         elif currentArgument in ("-f", "--folder"):
#             print ("Displaying folder:", sys.argv[0])
    
             
# except getopt.error as err:
#     # output error, and return with an error code
#     print (str(err))
# #! cd ~/currentValue
# #command=f"['ls', '-l', '~/{currentValue}]"

# # folder path
# list_dir = subprocess.Popen(c)
# list_dir
# #list_dir.wait()

# run in directory containing the data
# SECONDS=0   
# # index the referece genome

# bwa index hs37d5.fa
#list_dir = subprocess.Popen("mkdir -p consensus",shell=True)
#generate vcf 
# vcf= "for i in `ls *.bam` do outfile=`basename $i .bam`.vcf echo 'Creating index of $i' samtools index $i echo 'Creating $outfile'"
# generate_vcf=subprocess.Popen(vcf,shell=True)
#generate_vcf=subprocess.Popen("bash for ls -l do echo {i}",shell=True)
#subprocess.Popen("bash for i in `ls` do echo ${i} done",shell=True)
# print(subprocess.check_output("for file in `ls *.bam`; do echo $file; done", shell=True,executable='/bin/bash').decode())
subprocess.run(["/scripts/bam2fa.sh"])