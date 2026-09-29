"""Simple expense tracker MCP server (SQLite-backed)."""

import sqlite3

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("expense_mcp")

# Full path to the database file, so it always works no matter
# where this script is run from.
DB_PATH = r"C:\Users\Manav Negi\Downloads\mcp server\expenses.db"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
conn.execute(
    "CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, amount REAL, category TEXT)"
)
conn.commit()


@mcp.tool()
async def expense_add(amount: float, category: str) -> str:
    """Record an expense with an amount and category."""
    conn.execute("INSERT INTO expenses (amount, category) VALUES (?, ?)", (amount, category))
    conn.commit()
    return f"Added {amount} to {category}"


@mcp.tool()

async def expense_list() -> str:
    """List all recorded expenses."""
    cursor = conn.execute("SELECT id, amount, category FROM expenses")

    result = ""
    for r in cursor:
        result += f"#{r[0]} {r[2]}: {r[1]}\n"

    if not result:
        return "No expenses yet."
    return result


@mcp.tool()
async def expense_summary() -> str:
    """Show total spending per category."""
    cursor = conn.execute(
        "SELECT category, SUM(amount) FROM expenses GROUP BY category"
    )

    result = ""
    for category, total in cursor:
        result += f"{category}: {total}\n"

    if not result:
        return "No expenses yet."
    return result


if __name__ == "__main__":
    mcp.run()
