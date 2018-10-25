#Python3
import sys
from datetime import timedelta, datetime

__author__      = "Devendra Dora"

if __name__== "__main__":
   #date in yyyy-MM-dd
  if len(sys.argv) == 2:
  	inparg = sys.argv[1]
  	inpdate = datetime.strptime(inparg, '%Y-%m-%d').date()
  else:
  	inpdate = datetime.utcnow() - timedelta(days=1) + timedelta(hours=5,minutes=30)
  print(str(inpdate))
