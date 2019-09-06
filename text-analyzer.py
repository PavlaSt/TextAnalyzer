# PROJECT 1: TEXT ANALYZER


# Password check
print('-'*64)
print('Welcome to the app. Please log in:')
user_pasw = {'bob': '123', 'ann': 'pass123', 'mike': 'password123','liz': 'pass123'}
username = input('USERNAME: ')
password = input('PASSWORD: ')
if username not in user_pasw or password != user_pasw[username]:
	print('Username or password is wrong.')

else:
	# Choise of text
	TEXTS = ['''
	Situated about 10 miles west of Kemmerer, 
	Fossil Butte is a ruggedly impressive 
	topographic feature that rises sharply 
	some 1000 feet above Twin Creek Valley 
	to an elevation of more than 7500 feet 
	above sea level. The butte is located just 
	north of US 30N and the Union Pacific Railroad, 
	which traverse the valley. ''',

	'''At the base of Fossil Butte are the bright 
	red, purple, yellow and gray beds of the Wasatch 
	Formation. Eroded portions of these horizontal 
	beds slope gradually upward from the valley floor 
	and steepen abruptly. Overlying them and extending 
	to the top of the butte are the much steeper 
	buff-to-white beds of the Green River Formation, 
	which are about 300 feet thick.''',

	'''The monument contains 8198 acres and protects 
	a portion of the largest deposit of freshwater fish 
	fossils in the world. The richest fossil fish deposits 
	are found in multiple limestone layers, which lie some 
	100 feet below the top of the butte. The fossils 
	represent several varieties of perch, as well as 
	other freshwater genera and herring similar to those 
	in modern oceans. Other fish such as paddlefish, 
	garpike and stingray are also present.'''
	]
	print('-'*64)
	choice = input('We have 3 texts to be analyzed. \nEnter a number btw. 1 and 3 to select: ')
	print('-'*64)

	
		
	if choice in ['1','2','3']:
		# List from string		
		words = TEXTS[int(choice)-1].split()
		# Analysis of text, saving results in list and in dictionary
		descr_nums = [0, 0, 0, 0, 0, 0]
		frq_word_len = dict()
		
		descr_nums[0] = len(words)
		while words:
			word = words.pop(0)
			word = word.strip('.,')
			if word.istitle():
				descr_nums[1] += 1
			if word.isupper():
				descr_nums[2] += 1
			if word.islower():
				descr_nums[3] += 1
			if word.isnumeric():
				descr_nums[4] += 1
				descr_nums[5] += float(word)
			frq_word_len[len(word)]= frq_word_len.get(len(word),0) + 1
		
		sort_frq = dict(sorted(frq_word_len.items()))
		
		# Printing results	
		print('There are '+ str(descr_nums[0]) + ' words in the selected text.')
		print('There are '+ str(descr_nums[1]) + ' titlecase words.')
		print('There are '+ str(descr_nums[2]) + ' uppercase words.')
		print('There are '+ str(descr_nums[3]) + ' lowercase words.')
		print('There are '+ str(descr_nums[4]) + ' numeric strings.')
		print('-'*64)

		for k,v in sort_frq.items():
			print(f"{k:>2d} {v*'*'} {v:>2d}")

		print('-'*64)
		print('If we summed all the numbers in this text, we would get:', descr_nums[5])
		print('-'*64)


	else:
		print('Incorrect input.')