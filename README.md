# Expense Tracker MCP Server

A simple [Model Context Protocol](https://modelcontextprotocol.io) server, built with FastMCP and SQLite, for tracking expenses.

## Tools

- `expense_add(amount, category)` - record an expense
- `expense_list()` - list all recorded expenses
- `expense_summary()` - show total spending per category

## Setup

```
pip install "mcp[cli]"
python server.py
```

Expenses are stored in a local SQLite file (`expenses.db`), created automatically on first run. Update `DB_PATH` in `server.py` to match your machine.

## Connect to Claude Desktop

1. Install the dependency in your virtualenv:

   ```
   .venv\Scripts\pip install "mcp[cli]"
   ```

2. In Claude Desktop, open Settings > Developer > Edit Config. This opens `%APPDATA%\Claude\claude_desktop_config.json`.

3. Add the server, using the virtualenv's Python and double backslashes in paths:

   ```json
   {
     "mcpServers": {
       "expense_mcp": {
         "command": "C:\\path\\to\\mcp server\\.venv\\Scripts\\python.exe",
         "args": ["C:\\path\\to\\mcp server\\server.py"]
       }
     }
   }
   ```

4. Fully quit Claude Desktop (including the system tray) and reopen it.

5. The tools `expense_add`, `expense_list` and `expense_summary` should appear. Try: "Add a 250 expense for food", then "Show my expense summary".

### Troubleshooting

- Check the logs at `%APPDATA%\Claude\logs\mcp-server-expense_mcp.log`.
- `ModuleNotFoundError: mcp` means `command` is not pointing at the virtualenv's `python.exe`.
- A JSON error usually means a missing comma or single backslashes in a path.
