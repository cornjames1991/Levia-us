import os
import sys
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)
from engine.tool_framework.tool_registry import ToolRegistry
from engine.tool_framework.tool_caller import ToolCaller

def main():
    registry = ToolRegistry()
    # Use absolute path
    tools_dir = os.path.join(os.path.dirname(__file__), "./")
    registry.scan_directory(tools_dir)  # Scan tools directory

    # Create ToolCaller instance
    caller = ToolCaller(registry)
    result = caller.call_tool(tool_name="website_scan_tool", method="website_scan", kwargs={"urls": ["https://leviaprotocol.gitbook.io/leviaprotocol"],"intent":'What is Levia,and how it works?'})
    
    if result:
        if 'error' in result:
            print(f"Tool execution error: {result['error']}")
        else:
            print(f"response info: {result}")
    else:
        print("Tool call failed, no result returned")

if __name__ == "__main__":
    main()