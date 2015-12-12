import sys
import os

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
		print "starting iteration with "+str(num_cellstates)+" cell states and "+str(nesting_depth)+" average depth of nesting"
		print "th train.lua -data_dir data/dyck-"+str(nesting_depth)+" -rnn_size "+str(num_cellstates)+" -num_layers "+str(num_layers)+" -dropout 0.5 -gpuid "+str(gpuid)+" -model lstm -savefile lstm_"+str(nesting_depth)+"_"+str(num_cellstates)
		os.system("th train.lua -data_dir data/dyck-"+str(nesting_depth)+" -max_epochs 0.5 -rnn_size "+str(num_cellstates)+" -num_layers "+str(num_layers)+" -dropout 0.5 -gpuid "+str(gpuid)+" -model lstm -savefile lstm_"+str(nesting_depth)+"_"+str(num_cellstates))
		#fls = getTxtFiles("cv","lstm_"+str(nesting_depth)+"_"+str(num_cellstates))
		#print fls
		print "-------"
		##now sample the trained model
