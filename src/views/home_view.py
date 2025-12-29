import flet as ft
from components import BalanceCard, Sidebar, MonthlyStatsRow
from data_manager import get_balance, get_current_month_stats

def HomeView(page):
    # Load Real Data from DB
    current_balance = get_balance()
    month_income, month_expense = get_current_month_stats()
    
    sidebar = Sidebar(page)
    def open_drawer(e):
        page.open(sidebar)

    def open_income(e):
        page.go("/income_add")

    def open_expense(e):
        page.go("/expense_add")

    btn_income = ft.ElevatedButton(
        text="ADD INCOME",
        icon=ft.Icons.ADD,
        bgcolor="black", color="white", height=50, width=float("inf"),
        style=ft.ButtonStyle(side=ft.BorderSide(1, "white"), shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=open_income
    )

    btn_expense = ft.ElevatedButton(
        text="ADD EXPENSE",
        icon=ft.Icons.REMOVE,
        bgcolor="black", color="white", height=50, width=float("inf"),
        style=ft.ButtonStyle(side=ft.BorderSide(1, "white"), shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=open_expense
    )

    return ft.View(
        "/",
        controls=[
            ft.Column(
                controls=[
                    ft.Container(height=20),
                    BalanceCard(current_balance),
                    ft.Text("THIS MONTH", size=12, color="grey"),
                    ft.Container(height=15),
                    MonthlyStatsRow(month_income, month_expense),
                    ft.Container(expand=True),
                    ft.Text("ACTIONS", color="grey", size=12),
                    btn_income,
                    ft.Container(height=10),
                    btn_expense,
                ],
                expand=True
            )
        ],
        drawer=sidebar,
        appbar=ft.AppBar(
            leading=ft.IconButton(ft.Icons.MENU, on_click=open_drawer),
            title=ft.Text("Cash Flow", weight="bold"),
            center_title=True,
            bgcolor="#111111",
        ),
        bgcolor="black"
    )