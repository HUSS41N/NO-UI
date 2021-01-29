print('-----Welcome to Miles per hour to Metres per second APP------')
mph = float(input('What is your speed in miles per hour? '))
mps  = round((mph*1609.34/60)/60,2)
print(f'Your speed in metre per second will be {mps}')