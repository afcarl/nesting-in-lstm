import sys
import os
import re
import os.path

##script workflow:
#vary number of cell states
#vary depth of nesting
#for each scenario, record:
#a) loss
#b) likelihood for each character
#c) cell state

max_cell_states = 10;
num_layers = 2;
gpuid = 0


def getTxtFiles(a_dir,a):
		return [name for name in os.listdir(a_dir)
				if name.endswith(".t7") and a in name]


for num_cellstates in range(1,max_cell_states+1):
	for nesting_depth in range(5,12):
		print "starting sampling with "+str(num_cellstates)+" cell states and "+str(nesting_depth)+" average depth of nesting"
		if not os.path.isfile("out/lstm_"+str(nesting_depth)+"_"+str(num_cellstates)+".txt") or (num_cellstates==9 and nesting_depth==7):
			fls = getTxtFiles("cv","lstm_"+str(nesting_depth)+"_"+str(num_cellstates))
			print fls
			if len(fls)>0:
				flmax = fls[0]
				m = re.search('epoch(.+?)_', flmax)
				number = ""
				if m:
					number = m.group(1)
					print "--"+number+"---"
				flnum = float(number)
				for fl in fls:
					m = re.search('epoch(.+?)_', fl)
					number = ""
					if m:
						number = m.group(1)
					number = float(number)
					if number>flnum:
						flmax = fl
						flnum = number
				print flmax
				print "sampling file:"
				os.system("th sample.lua cv/"+flmax+" >out/lstm_"+str(nesting_depth)+"_"+str(num_cellstates)+".txt")
			print "-------"
		##now sample the trained model
