#C:\00 Prog\Python37\python.exe "$(FULL_CURRENT_PATH)" -i
import datetime
import time

xxx = datetime.datetime.now()
print (xxx.year + 2)
time.sleep(0)
print (datetime.datetime.now().strftime("%y"))
time.sleep(0)
print (datetime.datetime.now().strftime("%Y"))
time.sleep(1)
