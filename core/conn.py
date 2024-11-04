import duckdb

conn:duckdb.DuckDBPyConnection = None
def getConn() -> duckdb.DuckDBPyConnection:
    global conn
    if conn == None:
        conn = duckdb.connect("database/linklayer.db")
    return conn