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
