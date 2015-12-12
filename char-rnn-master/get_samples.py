import glob
import os
filelist = glob.glob("/Users/macuser/Dropbox/Dokumente/ad_final_project/char-rnn-master/cv/*.t7")
#/Users/macuser/Dropbox/Dokumente/ad_final_project/char-rnn-master/data
#th sample.lua cv/lm_lstmr_epoch1.42_1.0487.t7 -gpuid 0 > file.txt

for obj in filelist:
	print obj
	os.system("echo '"+obj+"' >> file.txt")

	os.system("th sample.lua "+obj+" -gpuid 0 >> file.txt")