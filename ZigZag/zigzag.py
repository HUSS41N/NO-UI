import time,sys
indent = 0
indentIncreasing = True

while True:
	try:
		print(' '*indent,end='')
		print('KYA BOLTIS TUHHHH')
		time.sleep(0.1)

		if indentIncreasing:
			indent = indent + 1
			if indent == 30:
				indentIncreasing=False
		else:
			indent = indent - 1
			if indent == 0 :
				indentIncreasing = True
	except KeyboardInterrupt:
		sys.exit()