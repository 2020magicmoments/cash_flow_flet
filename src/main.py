import flet as ft
from views.home_view import HomeView
from views.income_view import IncomeView
from views.expense_view import ExpenseView
from views.report_view import ReportView
from data_manager import init_db

def main(page: ft.Page):

    init_db() 

    page.title = "Cash Flow App"
    page.window_width = 350
    page.window_height = 600
    page.adaptive = True
    page.bgcolor = "black"
    page.theme_mode = ft.ThemeMode.DARK

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(HomeView(page))
        elif page.route == "/report":
            page.views.append(ReportView(page))
        elif page.route == "/income_add":
            page.views.append(IncomeView(page))
        elif page.route == "/expense_add":
            page.views.append(ExpenseView(page))

        page.update()

    def view_pop(view):
        page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Start at Home
    page.go("/")

ft.app(target=main)