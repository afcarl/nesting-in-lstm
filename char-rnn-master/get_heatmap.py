import sys
import os
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

def ignore_errors_evaluation(data):
    ##ignore erroneous parentheses
    errorparen = np.array([]);
    errorparendepth = np.array([]);
    i=-1;
    stack = [];
    while(i+1<len(data)):
        i = i+1;
        dat = data[i];
        if (dat=='[') or (dat=='{') or (dat=='('):
            stack.append(dat);
        else:
            if(len(stack)<1):
                errorparen = np.append(errorparen,i);
                errorparendepth = np.append(errorparendepth,len(stack));
                continue
            dat_prev = stack.pop();
            if(dat==']') and (dat_prev=='['):
                continue;
            elif(dat==')') and (dat_prev=='('):
                continue;
            elif(dat=='}') and (dat_prev=='{'):
                continue;
            else:
                errorparen = np.append(errorparen,i);
                stack.append(dat_prev)
                errorparendepth = np.append(errorparendepth,len(stack));
    return errorparen,errorparendepth


def getTxtFiles(a_dir,a):
		return [name for name in os.listdir(a_dir)
				if name.endswith(".txt") and a in name]

def get_correct_perc(some_text):
    depth_array = []
    err_depth = []
    mistake_count = 0
    total_count = len(some_text)
    for c in some_text:
        if c == "(" or c == "[":
            depth_array.append(c)
        else:
            try:
                curr_open = depth_array.pop()
                if (curr_open == "(" and c == ")") or (curr_open == "[" and c == "]"):
                    pass
                else:
                	err_depth += [len(depth_array)]
                	mistake_count +=1
            except:
                mistake_count +=1
    mistake_count+=len(depth_array)
    return  (1-mistake_count/float(total_count))*100,err_depth

data = np.zeros((7,10))
data2 = np.zeros((7,10))
#data[1,2]=1

for num_cellstates in range(1,max_cell_states+1):
	for nesting_depth in range(5,12):
		fls = getTxtFiles("out","lstm_"+str(nesting_depth)+"_"+str(num_cellstates))
		if(len(fls)>0):
			print "starting sampling with "+str(num_cellstates)+" cell states and "+str(nesting_depth)+" average depth of nesting"
			print fls
			print "-------"
			fl = "out/"+fls[0]
			lines = open(fl, 'r').read().splitlines()
			print lines[5]
			print "-------"
			sample = lines[5]
			errorparen,errorparendepth = ignore_errors_evaluation(sample)
			data2[nesting_depth-5,num_cellstates-1],err_dep = get_correct_perc(sample)
			data2[nesting_depth-5,num_cellstates-1] = (100-int(data2[nesting_depth-5,num_cellstates-1]))/100.0
			if(num_cellstates==3 and nesting_depth==8):
				plt.hist(err_dep,bins=100)
				plt.xlabel('Depth of Error',fontsize=24)
				plt.ylabel('Number of Errors',fontsize=24)
				plt.xticks(fontsize = 20)
				plt.yticks(fontsize = 20)
				plt.savefig("hist_depth_4_8_depthoferror.png",bbox_inches='tight')
				#plt.show()
			print "number of errors",len(errorparen)
			data[nesting_depth-5,num_cellstates-1]=len(errorparen)
			data[nesting_depth-5,num_cellstates-1]=int(data[nesting_depth-5,num_cellstates-1])/2000.0
		##now sample the trained model


cell_num = ["1","2","3","4","5","6","7","8","9","10"]
nest_depth = ["5","6","7","8","9","10","11"]
fig, ax = plt.subplots()
heatmap = ax.pcolor(data, cmap=plt.cm.Blues)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)
ax.set_yticks(np.arange(data.shape[0])+0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()
plt.xlabel('Number of Cell States',fontsize=24)
plt.ylabel('Average Nesting Depth',fontsize=24)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

ax.set_xticklabels(cell_num, minor=False)
ax.set_yticklabels(nest_depth, minor=False)

#heatmap = plt.pcolor(data)

for y in range(data.shape[0]):
    for x in range(data.shape[1]):
    	valu = data[y, x]
        plt.text(x + 0.5, y + 0.5, '%.2f' % valu,
                 horizontalalignment='center',
                 verticalalignment='center',
                 )

plt.colorbar(heatmap)

plt.savefig("jump_over_errors_heatmap.png",bbox_inches='tight')
#plt.show()


fig, ax = plt.subplots()
heatmap = ax.pcolor(data2, cmap=plt.cm.Blues)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(data2.shape[1])+0.5, minor=False)
ax.set_yticks(np.arange(data2.shape[0])+0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()
plt.xlabel('Number of Cell States',fontsize=24)
plt.ylabel('Average Nesting Depth',fontsize=24)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

ax.set_xticklabels(cell_num, minor=False)
ax.set_yticklabels(nest_depth, minor=False)

#heatmap = plt.pcolor(data)

for y in range(data2.shape[0]):
    for x in range(data2.shape[1]):
    	valu = data2[y, x]
        plt.text(x + 0.5, y + 0.5, '%.2f' % valu,
                 horizontalalignment='center',
                 verticalalignment='center',
                 )

plt.colorbar(heatmap)

plt.savefig("pop_errors_heatmap.png",bbox_inches='tight')
plt.show()







