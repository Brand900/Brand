
import os,platform
os.system('git pull')
# exit(' Wait Tool On updating ')
Brand=platform.architecture()[0]
if Brand=="32bit":__import__("Brand32")
elif Brand=="64bit":__import__("Brand64")
