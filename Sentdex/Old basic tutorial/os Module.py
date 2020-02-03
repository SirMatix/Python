import os



#get current directory
curDir = os.getcwd()
print(curDir)

#create new directory

os.mkdir('newDir')

#rename directory
import time

time.sleep(2)
os.rename('newDir', 'newDir2')

#delete directory
time.sleep(2)
os.rmdir('newDir2')
