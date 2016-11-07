
numbers = [0] * 40;
y = [];
para = 0;
for pos1 in ["+","-","*","/"] :
  for pos2 in ["+","-","*","/"] :
    for pos3 in ["+","-","*","/"] :
      for pos4 in ["+","-","*","/"] :
      	for open1 in ["","("] :
      	  for open2 in ["","("] :
      	    for open3 in ["","("] :
      	      for open4 in ["","("] :
      	        for close1 in ["",")"] :
      	          for close2 in ["",")"] :
      	            for close3 in ["",")"] :
      	              for close4 in ["",")"] :
			newstring = open1 + "5" + pos1 + open2 + "4" + close1 + pos2 + open3 + "3" + close2 + pos3 + open4 + "2" + close3 + pos4 + "1" + close4
			para = 0
			for c in newstring :
			  if c == "(" :
			    para = para + 1
			  elif c == ")" :
			    para = para - 1
			  if para < 0 :
			    break

			#print newstring
			if para != 0:
			  continue
			try:
          		  res = eval(newstring);
			except ZeroDivisionError:
			  continue
        		if res > 0 and res < 41 :
        		  numbers[res-1] = 1;
        		y.append(res);
		      


print "Numbers not found:";
for x in range(0,40) :
  if numbers[x] == 0 :
    print str(x+1) + ", ";
