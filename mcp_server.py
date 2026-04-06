from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."

if __name__ == "__main__":
    mcp.run()
