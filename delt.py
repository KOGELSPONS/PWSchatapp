import os
import time

if os.path.exists("firstsetup.py"):
  import firstsetup
  time.sleep(1)
  print("!!!After sleep")
  os.remove("firstsetup.py")
  print("firstsetup.py succesfully removed")
else :
  print("firstsetup.py does not exist")