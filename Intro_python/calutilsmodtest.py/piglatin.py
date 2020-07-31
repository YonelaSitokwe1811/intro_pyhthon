
def to_pig_latin(sentence):
	    i = 0
	    while i < (len(sentence)-1): 
	        if sentence[i] in {'a','e','i','o','u'} and (i == 0 or sentence[i-1] ==' '):
	            while sentence[i] != ' ' and i < (len(sentence)-1):
	                i +=1
	            if i == len(sentence) -1:
	                sentence = sentence[:i+1] + 'way' + sentence[i+2:]
	            else:
	                sentence = sentence[:i] + 'way ' + sentence[i+1:]
	        elif sentence[i] not in {'a','e','i','o','u'} and (i == 0 or sentence[i-1] ==' '):
	            x =''
	            while (sentence[i] != ' ' and sentence[i] not in {'a','e','i','o','u'}) and i < (len(sentence)-1):
	                x += sentence[i]
	                sentence = sentence = sentence[:i] + '' + sentence[i+1:]
	            while sentence[i] != ' '  and i < (len(sentence)-1):
	                i += 1
	            if i == len(sentence) -1:
	                sentence = sentence[:i+1] + 'a' + x + 'ay' + sentence[i+2:]
	            else:
	                sentence = sentence[:i] + 'a' + x + 'ay '+ sentence[i+1:]
	        i +=1
	    return sentence
def to_english(sentence):
	    i=0
	    while i < (len(sentence)-1):
	        i = sentence.find('way')
	        if sentence.find('way') != 0:
	            sentence = sentence[:i] + '' + sentence[i+3:]
	            i += 1	 
	    while sentence.find('ay') != -1 :
	        front = ''
	        i_1 = sentence.find('ay') 
	        i_2 = i_1-1  
	        while sentence[i_2] != 'a' and i_2 >=0:
	            i_2 -= 1	      
	        i_2 += 1
	        front += sentence[i_2:i_1]
	        buffer = memoryview
	        part1 = buffer(sentence,i_2-1, i_2-1 )
	        part2 = buffer(sentence,i_2+len(front)+2,len(sentence) -2+len(front)+2 )
	        sentence= part1+ '' + part2   
	        i_2 -= 2 
	        while sentence[i_2] != ' ' and i_2 > 0:
	            i_2 -= 1
	        sentence = sentence[:i_2] +'' + front + sentence[i_2+1:]
	    return sentence
