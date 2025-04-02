from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("LearningDemo", dependencies=["requests"])


@mcp.tool()
def add(a: int, b: int):
    """Add two numbers"""
    return a + b

@mcp.tool()
def random_person():
    """Gives the placeholder data for a random person"""
    result = requests.get("https://randomuser.me/api/")

    return result

@mcp.tool()
def age_of_barack_obama():
    """Gives the age of Barack Obama"""
    return 36
