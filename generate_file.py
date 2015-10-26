import numpy as np

alphabet = ['(','[','{',')',']','}'];

def generate_data(length):
  stack = [];
  iter = 0;
  while (iter < length):
    iter = iter + 1;
#if at beginning go always in first loop.
#stack has to be equal or smaller than remaining number of characters
    if(np.random.random()>0.5 or len(stack)<1) and (len(stack)<length/2) and (len(stack)<(length - iter)):
      i = np.random.randint(0,2);
      print alphabet[i],
      stack.append(alphabet[i+3]);
    else:
      out = stack.pop();
      print out,

generate_data(16);
