from modules import modules_init

from modules import create_system



def welcome():
  
  global log

  log.info("Welcome to Prole-Ticker Server")


def init():
  
 system_data = graph_stuff.verify_system_data()
  
 if system_data == true:
   pass
 
 elif system_data == false:
   create_system.main()


def main():
  
  welcome()
  
  init()
  

if __name__ == "__main__":
  
  main()
