from time import sleep
def ticker(usertext):
    for x in usertext:                     
        print(x, sep='', end='')  
        sleep(0.01)
    print()
