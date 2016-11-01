
numbers = [0] * 40;
y = [];
for pos1 in ["+","-","*","/"] :
  for pos2 in ["+","-","*","/"] :
    for pos3 in ["+","-","*","/"] :
      for pos4 in ["+","-","*","/"] :
        res = eval("5" + pos1 + "4" + pos2 + "3" + pos3 + "2" + pos4 + "1");
        if res > 0 and res < 41 :
          numbers[res-1] = 1;
        y.append(res);

print "Numbers not found:";
for x in range(0,40) :
  if numbers[x] == 0 :
    print str(x+1) + ", ";
