from fastmcp import FastMCP

mcp = FastMCP("LearningDemo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
