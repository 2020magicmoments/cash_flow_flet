import flet as ft

def main(page: ft.Page):
    page.title = "My First App"
    page.window_width = 350  # Make it look like a phone on PC
    page.window_height = 600
    page.adaptive = True

    # --- 1. DEFINE THE DRAWER (SIDEBAR) ---
    def handle_drawer_change(e):
        # e.control.selected_index tells us which item was clicked (0, 1, 2...)
        if e.control.selected_index == 0:
            print("Report Selected!")
            page.go("/report")
        e.control.open = False
        e.control.update()

    # --- 2. BUTTON ACTIONS (Placeholders) ---
    def open_income(e):
        print("Income Clicked")
        page.go("/income_add")

    def open_expense(e):
        print("Expense Clicked")
        page.go("/expense_add")





    nav_drawer = ft.NavigationDrawer(
        bgcolor="#1A1A1A",
        controls=[
            ft.Container(height=12), # Spacer at top
            ft.Text("  Menu", size=20, weight="bold", color="white"),
            ft.Divider(color="grey"),
            
            # The Report Item
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ANALYTICS, # Icon for report
                label="Transaction Report",
            ),
        ],
        on_change=handle_drawer_change,
    )

    def route_change(route):
        page.views.clear()

        # 2. Define Balance Card
        balance_card = ft.Container(
                content=ft.Column(
                    [
                        ft.Text("TOTAL BALANCE", size=12, color="grey"),
                        ft.Text("₹ 0", size=45, weight="bold", color="white")
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor="#1A1A1A",
                border_radius=25,
                padding=40,
                width=float("inf"),
                border=ft.border.all(1, "white"),
                alignment=ft.alignment.center
            )
        # === HOME VIEW ===
        if page.route == "/":

            # Define Buttons
            btn_income = ft.ElevatedButton(
                text="ADD INCOME",
                icon=ft.Icons.ADD,
                bgcolor="black",
                color="white",
                height=50,
                width=float("inf"), # Full Width
                style=ft.ButtonStyle(
                    side=ft.BorderSide(1, "white"), # White Border
                    shape=ft.RoundedRectangleBorder(radius=10)
                ),
                on_click=open_income
            )

            btn_expense = ft.ElevatedButton(
                text="ADD EXPENSE",
                icon=ft.Icons.REMOVE,
                bgcolor="black",
                color="white",
                height=50,
                width=float("inf"), # Full Width
                style=ft.ButtonStyle(
                    side=ft.BorderSide(1, "white"), # White Border
                    shape=ft.RoundedRectangleBorder(radius=10)
                ),
                on_click=open_expense
            )

            page.views.append(
                ft.View(
                    "/", # Route name
                    controls=[
                        ft.Column(
                            controls=[
                                # Balance Card
                                ft.Container(height=20),
                                balance_card,

                                ft.Container(expand=True),

                                # 2. Buttons Section
                                ft.Text("ACTIONS", color="grey", size=12),
                                btn_income,
                                ft.Container(height=10), # Spacer
                                btn_expense,
                            ],
                        expand=True # Tells column to fill the screen height
                        )
                    ],
                    padding=20,
                    appbar=ft.AppBar(
                        leading=ft.IconButton(ft.Icons.MENU,on_click=lambda e: page.open(nav_drawer)),
                        title=ft.Text("Cash Flow", weight="bold"),
                        center_title=True,
                        bgcolor="#111111",
                    ),
                    drawer=nav_drawer, # Attach drawer to Home View
                    bgcolor="black"
                )
            )



        if page.route == "/report":
            page.views.append(
                ft.View(
                    "/report",
                    controls=[
                        ft.Container(
                            content=ft.Text("Transaction History will appear here.", color="grey"),
                            padding=20,
                            alignment=ft.alignment.center
                        )
                    ],
                    # App Bar for Report (With Back Button)
                    appbar=ft.AppBar(leading=ft.IconButton(ft.Icons.ARROW_BACK, 
                            on_click=lambda e: page.go("/") # Go back home
                        ),
                        title=ft.Text("Report", weight="bold"),
                        center_title=True,
                        bgcolor="#111111",
                    ),
                    bgcolor="black"
                )
            )

        if page.route == "/income_add":            
            # 1. Create Input Fields
            txt_amount = ft.TextField(
                label="Amount",
                prefix_text="₹ ",
                keyboard_type=ft.KeyboardType.NUMBER, # Numeric keyboard
                border_color="white",
                cursor_color="white",
                label_style=ft.TextStyle(color="grey"),
                text_style=ft.TextStyle(color="white", size=18)
            )

            txt_category = ft.TextField(
                label="Category",
                hint_text="e.g. Salary, Gift",
                hint_style=ft.TextStyle(color="#444444"),
                border_color="white",
                cursor_color="white",
                label_style=ft.TextStyle(color="grey"),
                text_style=ft.TextStyle(color="white")
            )

            # 2. Submit Logic
            def save_income(e):
                print(f"Saving Income: {txt_amount.value} - {txt_category.value}")

            btn_submit = ft.ElevatedButton(
                text="SAVE INCOME",
                bgcolor="white", # White button
                color="black",   # Black text
                height=50,
                width=float("inf"),
                on_click=save_income
            )
            page.views.append(
                ft.View(
                    "/income_add",
                    controls=[
                        ft.Container(
                            padding=20,
                            content=ft.Column([
                                balance_card,
                                ft.Text("Enter Income Details", size=16, color="grey"),
                                ft.Container(height=20),
                                txt_amount,
                                ft.Container(height=20),
                                txt_category,
                                ft.Container(height=40), # Spacer
                                btn_submit
                            ])
                        )
                    ],
                    # App Bar for Report (With Back Button)
                    appbar=ft.AppBar(leading=ft.IconButton(ft.Icons.ARROW_BACK, 
                            on_click=lambda e: page.go("/") # Go back home
                        ),
                        title=ft.Text("Add Income", weight="bold"),
                        center_title=True,
                        bgcolor="#111111",
                    ),
                    bgcolor="black"
                )
            )

        if page.route == "/expense_add":            
            # 1. Create Input Fields
            txt_amount = ft.TextField(
                label="Amount",
                prefix_text="₹ ",
                keyboard_type=ft.KeyboardType.NUMBER, # Numeric keyboard
                border_color="white",
                cursor_color="white",
                label_style=ft.TextStyle(color="grey"),
                text_style=ft.TextStyle(color="white", size=18)
            )

            txt_category = ft.TextField(
                label="Category",
                hint_text="e.g. Salary, Gift",
                hint_style=ft.TextStyle(color="#444444"),
                border_color="white",
                cursor_color="white",
                label_style=ft.TextStyle(color="grey"),
                text_style=ft.TextStyle(color="white")
            )

            # 2. Submit Logic
            def save_income(e):
                print(f"Saving Expense: {txt_amount.value} - {txt_category.value}")

            btn_submit = ft.ElevatedButton(
                text="SAVE",
                bgcolor="white", # White button
                color="black",   # Black text
                height=50,
                width=float("inf"),
                on_click=save_income
            )
            page.views.append(
                ft.View(
                    "/expense_add",
                    controls=[
                        ft.Container(
                            padding=20,
                            content=ft.Column([
                                balance_card,
                                ft.Text("Enter Expense Details", size=16, color="grey"),
                                ft.Container(height=20),
                                txt_amount,
                                ft.Container(height=20),
                                txt_category,
                                ft.Container(height=40), # Spacer
                                btn_submit
                            ])
                        )
                    ],
                    # App Bar for Report (With Back Button)
                    appbar=ft.AppBar(leading=ft.IconButton(ft.Icons.ARROW_BACK, 
                            on_click=lambda e: page.go("/") # Go back home
                        ),
                        title=ft.Text("Add Expense", weight="bold"),
                        center_title=True,
                        bgcolor="#111111",
                    ),
                    bgcolor="black"
                )
            )






        page.update()

    def view_pop(view):
        page.go("/")

    # txt_balance = ft.Text("$ 0", size=40,weight="bold",color="white")
    page.on_route_change = route_change
    page.on_view_pop = view_pop # Handles the Android physical back button

    # Start at Home
    page.go("/")

ft.app(target=main)