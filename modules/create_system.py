from .logger import log
from . import graph_stuff


global graph

global log

graph = graph_stuff.graph_var()


def verify_data_empty():
    
    global graph
    
    global log

    # Check for main node in database

    main = graph.run("Match (M: Main) RETURN (M)")

    if str(main) == "(No data)":
        log.info("Verified, No Graph Data")
        return False
    elif str(main) == "(No data)":
        log.info("Error: Data found")
        return True


def main():
   
    global log

    log.info("checking database")


    data_exists = verify_data_empty()


    if data_exists == True:
        pass
    elif data_exists == False:
        try:
            create()
            log.info("Database Creation Sucessfull")
        except Exception as e:
            log.info("Database creation unsucessful")
            log.info(e)


def create():
    global graph

    graph.run("CREATE (M: Main),\
            (G: Global_Settings),\
            (Sys: System_Info),\
            (UM: User_Master),\
            (UsrS: User_Settings),\
            (UDD: User_Dashboard_Data),\
            (AD: Application_Data),\
            (TM: Telemetry_Master),\
            (TAD: Telemetry_Application_Data),\
            (TND: Telemetry_Neo4j_Data),\
            (TDD: Telemetry_Docker_Data),\
            (TRD: Telemetry_Redis_Data),\
            (TRMD: Telemetry_Rabbitmq_Data),\
            (FD: File_Database),\
            (SC: Server_Code),\
            (GG: Generated_Graphs),\
            (AXD: Axis_Data),\
            (TMP: Temp_Data)\
            SET M.name = 'Main',\
            G.name = 'Global Settings',\
            Sys.name = 'System Info',\
            UM.name = 'User Master',\
            UsrS.name = 'User Settings',\
            UDD.name = 'User Dashboard Data',\
            AD.name = 'Application Data',\
            TM.name = 'Telemetry Master',\
            TAD.name = 'Telemetry Application Data',\
            TND.name = 'Telemetry Neo4j Data',\
            TDD.name = 'Telemetry Docker Data',\
            TRD.nme = 'Telemetry Redis Data',\
            TRMD.name = 'Telemetry Rabbitmq Data',\
            FD.name = 'File Databaase',\
            SC.name = 'Server Code',\
            GG.name = 'Generated Graphs',\
            AXD.name = 'Axis Data',\
            TMP.name = 'Temp Data'\
            CREATE (G)-[a: Link]->(M),\
            (Sys)-[b: Link]->(M),\
            (UM)-[c: Link]->(M),\
            (UsrS)-[d: Link]->(UM),\
            (UDD)-[e: Link]->(UM),\
            (AD)-[f: Link]->(M),\
            (TM)-[g: Link]->(M),\
            (TAD)-[h: Link]->(TM),\
            (TND)-[i: Link]->(TM),\
            (TDD)-[j: Link]->(TM),\
            (TRD)-[k: Link]->(TM),\
            (TRMD)-[l: Link]->(TM),\
            (FD)-[m: Link]->(M),\
            (SC)-[n: Link]->(M),\
            (GG)-[o: Limk]->(M),\
            (AXD)-[p: Link]->(M),\
            (TMP)-[q: Link]->(M) ")
