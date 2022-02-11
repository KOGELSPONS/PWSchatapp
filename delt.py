import os

if os.path.exists("firstsetup.py"):
  os.remove("firstsetup.py")
  print("firstsetup.py succesfully removed")
else :
  print("firstsetup.py does not exist")