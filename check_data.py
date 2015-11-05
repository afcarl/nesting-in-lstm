
def check_data(data):
  length = len(data);
  i=-1;
  stack = [];
  while(i+2<len(data)):
    i = i+1;
    dat = data[i];
    if (dat=='[') or (dat=='{') or (dat=='('):
      stack.append(dat);
    else:
      if(len(stack)<1):
        return i+1;
      dat_prev = stack.pop();
      if(dat==']') and (dat_prev=='['):
        continue;
      elif(dat==')') and (dat_prev=='('):
        continue;
      elif(dat=='}') and (dat_prev=='{'):
        continue;
      else:
        return i+1;
  if(len(stack)>0):
    return 0;
  return length;

def find_max_correct_element(txt):
  max_temp = [];
  for i in range(0,len(txt)-2):
    data2 = txt[i:(len(txt)-1)];
    max_temp.append(check_data(data2));
  print max(max_temp);
  f1=open('./testfile.txt', 'a');
  f1.write(`max(max_temp)`+",");
  f1.close();
