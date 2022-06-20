from .logger import log


def graph_var():

    import os
    from py2neo import Graph

    uri = "bolt://localhost:7688"
    user = "neo4j"
    password = os.environ["ProlePassword"]


    try:
        graph = Graph(uri, auth=(user, password))
        
        return graph
    except Exception as e:
        log.info(e)
        log.info("No Database connection can be established\n")
        log.info("Start Database then restart Prole-Ticker server\n")
        input()

        return False
    

def verify_graph_connection(graph):

    # Check for main node in database

    main = graph.run("Match (M: Main) RETURN (M)")

    if main == None:

        # Either no connection or no data, lets assume no connection for now

        global log

        log.info("No connection to database found, restart database and press any key to continue")

        input()

        return False
    
    elif main != None:
        return True
    
    
def verify_system_data(graph):
  
  # Verify Database connection
  
  connection = verify_graph_connection(graph)
  
  if connection == True:
    
    # Check for main node in database
    
    main = graph.run("Match (M: Main) RETURN (M)")
    
    if str(main) == "(No data)":
     
      # Case where database doesn't exist
      
      global log
      
      log.info("No System found.")
      log.info("Initializing System.")
      
      return False
    elif str(main) != "(No data)":
        log.info("Data Found")
        return True
