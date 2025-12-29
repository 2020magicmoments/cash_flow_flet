import flet as ft
from datetime import datetime
from components import BalanceCard
from data_manager import add_transaction, get_balance

def IncomeView(page):
    current_balance = get_balance()

    # 1. Define the Date Picker
    def change_date(e):
        if e.control.value:
            txt_date.value = e.control.value.strftime("%Y-%m-%d")
            txt_date.update()

    date_picker = ft.DatePicker(
        on_change=change_date,
    )

    # 2. Logic to open it using page.open()
    def open_date_picker(e):
        page.open(date_picker)

    # --- UI Fields ---
    txt_amount = ft.TextField(
        label="Amount", prefix_text="₹ ", keyboard_type=ft.KeyboardType.NUMBER,
        border_color="white", cursor_color="white",
        label_style=ft.TextStyle(color="grey"), text_style=ft.TextStyle(color="white", size=18)
    )

    txt_category = ft.TextField(
        label="Category", hint_text="e.g. Salary",
        border_color="white", cursor_color="white",
        label_style=ft.TextStyle(color="grey"), text_style=ft.TextStyle(color="white")
    )

    txt_date = ft.TextField(
        label="Date",
        value=datetime.now().strftime("%Y-%m-%d"),
        read_only=True,
        border_color="white", cursor_color="white",
        label_style=ft.TextStyle(color="grey"), text_style=ft.TextStyle(color="white"),
        expand=True
    )

    btn_pick_date = ft.IconButton(
        icon=ft.Icons.CALENDAR_MONTH,
        icon_color="white",
        on_click=open_date_picker  # Calls the function above
    )

    def save_income(e):
        if not txt_amount.value:
            return
        try:
            add_transaction(txt_amount.value, txt_category.value, "income", txt_date.value)
            page.go("/")
        except ValueError:
            pass

    btn_submit = ft.ElevatedButton(
        text="SAVE INCOME", bgcolor="white", color="black", height=50, width=float("inf"),
        on_click=save_income
    )

    return ft.View(
        "/income_add",
        controls=[
            ft.Container(
                padding=20,
                content=ft.Column([
                    BalanceCard(current_balance),
                    ft.Text("Enter Income Details", size=16, color="grey"),
                    ft.Container(height=20),
                    txt_amount,
                    ft.Container(height=20),
                    txt_category,
                    ft.Container(height=20),
                    ft.Row([txt_date, btn_pick_date]),
                    ft.Container(height=40),
                    btn_submit
                ])
            )
        ],
        appbar=ft.AppBar(
            leading=ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/")),
            title=ft.Text("Add Income", weight="bold"),
            center_title=True,
            bgcolor="#111111",
        ),
        bgcolor="black"
    )