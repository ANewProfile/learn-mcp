from fastmcp import FastMCP
import sqlite3

mcp = FastMCP("SQL AI Agent")


# Register a tool
@mcp.tool()
def query_data(sql: str):
    """Execute SQL queries safely"""
    conn = sqlite3.connect("./database.db")
    result = conn.execute(sql).fetchall()
    return "\n".join(str(row) for row in result)
