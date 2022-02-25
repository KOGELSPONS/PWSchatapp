import os
import time

if os.path.exists("firstsetup.py"):
  import firstsetup
  time.sleep(1)
  #os.remove("firstsetup.py")
  print("firstsetup.py succesfully removed")
else :
  print("firstsetup.py does not exist")