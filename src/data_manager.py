import sqlite3
from datetime import datetime

DB_FILE = "cashflow.db"

def init_db():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT,
            amount REAL NOT NULL,
            date_added TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(amount, category, trans_type, date_str=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if not date_str:
        date_str = datetime.now().strftime("%Y-%m-%d") # simplified to YYYY-MM-DD
    
    cursor.execute("""
        INSERT INTO transactions (type, category, amount, date_added)
        VALUES (?, ?, ?, ?)
    """, (trans_type, category, float(amount), date_str))
    
    conn.commit()
    conn.close()

def get_balance():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = cursor.fetchone()[0] or 0.0
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expense = cursor.fetchone()[0] or 0.0
    conn.close()
    return total_income - total_expense

# --- NEW FUNCTION FOR FILTERING ---
def get_filtered_report(start_date=None, end_date=None):
    """
    Fetches transactions. 
    If dates are provided, filters by range.
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    if start_date and end_date:
        # SQLite 'date()' function ensures we compare date parts correctly
        query = """
            SELECT * FROM transactions 
            WHERE date(date_added) BETWEEN date(?) AND date(?)
            ORDER BY date_added DESC
        """
        cursor.execute(query, (start_date, end_date))
    else:
        # Default: Show everything
        cursor.execute("SELECT * FROM transactions ORDER BY date_added DESC")
        
    rows = cursor.fetchall()
    conn.close()
    return rows

# --- ADD THIS NEW FUNCTION AT THE BOTTOM ---
def get_current_month_stats():
    """Calculates Income and Expense for the current month."""
    conn = sqlite3.connect("cashflow.db")
    cursor = conn.cursor()
    
    # Get current YYYY-MM string (e.g., '2023-10')
    current_month_str = datetime.now().strftime("%Y-%m")
    
    # Calculate Income for this month
    cursor.execute("""
        SELECT SUM(amount) FROM transactions 
        WHERE type='income' AND strftime('%Y-%m', date_added) = ?
    """, (current_month_str,))
    income = cursor.fetchone()[0] or 0.0
    
    # Calculate Expense for this month
    cursor.execute("""
        SELECT SUM(amount) FROM transactions 
        WHERE type='expense' AND strftime('%Y-%m', date_added) = ?
    """, (current_month_str,))
    expense = cursor.fetchone()[0] or 0.0
    
    conn.close()
    return income, expense