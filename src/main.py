# Thêm đường dẫn project vào sys.path để Python có thể tìm thấy các module
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.server import MCPServer

if __name__ == "__main__":
    server = MCPServer()
    server.run()