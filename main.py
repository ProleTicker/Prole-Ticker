from modules import create_system
from modules.logger import log
from modules import graph_stuff


def welcome():

    global log

    log.info("Welcome to Prole-Ticker Server")


def init():

    graph = graph_stuff.graph_var()

    system_data = graph_stuff.verify_system_data(graph)

    if system_data == True:
        pass

    elif system_data == False:
        create_system.main()


def main():
    
    welcome()

    init()
  

if __name__ == "__main__":
    main()
