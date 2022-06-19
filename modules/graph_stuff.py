from . import modules_init()


uri = "bolt://localhost:7688"
user = "neo4j"
password = os.getenv('Prole-Ticker_Passord')
    
    
global graph

try:
  graph = Graph(uri, auth=(user, password))
except:
  log.info("No Database connection can be established\n")
  log.info("Start Database then restart Prole-Ticker server\n")
  input()


def verify_graph_connection():
  
 # Check for main node in database
  
  global graph
  
  main = graph.run("Match (M: Main) RETURN (M)")
  
  if main == null:
    
    # Either no connection or no data, lets assume no connection for now
    
    global log
    
    log.info("No connection to database found, restart database and press any key to continue")
    input()
    
    return false
    
  if main != null:
    
    return true
    
    
def verify_system_data():
  
  # Verify Database connection
  
  connection = verify_graph_connection()
  
  if connection == true:
    
    # Check for main node in database
    
    global graph
    
    main = graph.run("Match (M: Main) RETURN (M)")
    
    if main == null:
     
      # Case where database doesn't exist
      
      global log
      
      log.info("No System found.")
      log.info("Initializing System.")
      
      return false
    elif main != null:
      
      return true
