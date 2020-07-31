# somehelp.py
	

import random
	

def welcome():
	    print('Welcome to the automated technical support system.')
	    print('Please describe your problem.')
	

def get_input():
	    return input().lower()
	

	

def main():
	

	    response = ['Have you tried it on a different operating system?','Did you reboot it?','What colour is it?','You should consider installing anti-virus software.','Contact Telkom.','I should get that looked at if I were you.']
	

	    
	    welcome()    
	    query = get_input()
	    
	    while (not query=='quit'):
	        print(response[random.randint(0,5)])
	

	        query = get_input()    
	    
#if __name__=='__main__':
main() 