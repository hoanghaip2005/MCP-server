from mcp.server.fastmcp import FastMCP
from typing import Dict, Any
import sys

# Import factory từ module joke của chúng ta
from src.joke import joke_factory


class MCPServer:
    def __init__(self):
        # Đặt tên cho server của bạn, tên này sẽ hiển thị trên Claude
        self.mcp = FastMCP("Joke API Server")
        self._register_tools()

    def _register_tools(self):
        """Đăng ký tất cả các tool mà Claude có thể gọi."""

        # Tool 1: Lấy một truyện cười ngẫu nhiên theo loại
        @self.mcp.tool()
        async def get_joke_by_type(joke_type: str) -> Dict[str, Any]:
            """
            Lấy một truyện cười ngẫu nhiên.
            Các loại hợp lệ là: 'hoang', 'tin'.
            """
            print(f"Received request for joke type: {joke_type}", file=sys.stderr)
            try:
                provider = joke_factory.get_joke_provider(joke_type.lower())
                if not provider:
                    return {"error": f"Không tìm thấy loại truyện cười '{joke_type}'."}

                joke_text = provider.get_random_joke()
                return {"joke_type": joke_type, "joke": joke_text}
            except Exception as e:
                print(f"Error getting joke: {e}", file=sys.stderr)
                return {"error": str(e)}

        # Tool 2: Liệt kê các loại truyện cười có sẵn
        @self.mcp.tool()
        async def list_available_joke_types() -> Dict[str, Any]:
            """Liệt kê tất cả các loại truyện cười hiện có."""
            print("Received request to list joke types", file=sys.stderr)
            try:
                types = joke_factory.get_available_types()
                return {"available_types": types}
            except Exception as e:
                print(f"Error listing types: {e}", file=sys.stderr)
                return {"error": str(e)}

    def run(self):
        """Khởi động MCP server."""
        try:
            print("Running the MCP server, waiting for Claude...", file=sys.stderr)
            # Chạy server với giao thức stdio
            self.mcp.run(transport="stdio")
        except Exception as e:
            print(f"MCP server crashed: {e}", file=sys.stderr)
            sys.exit(1)