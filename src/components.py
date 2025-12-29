import flet as ft

def BalanceCard(current_balance):
    return ft.Container(
        content=ft.Column(
            [
                # --- TOP ROW: Bank Name & Contactless Icon ---
                ft.Row(
                    [
                        ft.Text("CASH FLOW", size=14, weight="bold", color="#AAAAAA", font_family="monospace"),
                        ft.Icon(ft.Icons.WIFI, color="#AAAAAA", size=24, rotate=1.57), # Rotated wifi looks like contactless
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                
                ft.Container(height=15),

                # --- CHIP SIMULATION ---
                ft.Container(
                    width=45,
                    height=35,
                    bgcolor="#222222",
                    border=ft.border.all(1, "#555555"),
                    border_radius=5,
                    content=ft.Stack([
                        ft.Container(border=ft.border.all(1, "#444444"), border_radius=2, width=45, height=35),
                        ft.Container(border=ft.border.all(1, "#444444"), width=20, height=20, left=12, top=7),
                    ])
                ),

                ft.Container(height=10),

                # --- MIDDLE: Balance (Acting as Card Number) ---
                ft.Text(
                    f"₹ {current_balance:,.2f}", 
                    size=32, 
                    weight="bold", 
                    color="white",
                    font_family="monospace", # Looks like embossed numbers
                ),

                ft.Container(height=20),

                # --- BOTTOM ROW: Labels & Logo ---
                ft.Row(
                    [
                        # Left: Holder Name / Label
                        ft.Column(
                            [
                                ft.Text("CURRENT BALANCE", size=8, color="#888888"),
                                ft.Text("WALLET OWNER", size=12, color="#CCCCCC", font_family="monospace"),
                            ],
                            spacing=2
                        ),
                        # Right: Circles (Mastercard/Visa style logo)
                        ft.Stack(
                            [
                                ft.Container(width=30, height=30, bgcolor="#555555", border_radius=15, opacity=0.8),
                                ft.Container(width=30, height=30, bgcolor="#222222", border_radius=15, opacity=0.8, left=18, border=ft.border.all(1, "#555555")),
                            ],
                            width=50, height=30
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.END
                )
            ],
        ),
        # --- CARD STYLING ---
        width=float("inf"),
        height=220,
        border_radius=20,
        padding=25,
        # Gradient Background for depth (Black to Dark Grey)
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#222222", "#000000"],
        ),
        # Shadow to make it pop
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.with_opacity(0.5, "white"),
            offset=ft.Offset(0, 0),
        ),
        border=ft.border.all(1, "#333333"), # Subtle border
    )

def Sidebar(page):
    def handle_change(e):
        if e.control.selected_index == 0:
            page.go("/report")
        
        # Close the drawer logic
        e.control.open = False
        e.control.update()

    return ft.NavigationDrawer(
        bgcolor="#1A1A1A",
        indicator_color="black", 
        controls=[
            ft.Container(height=12),
            ft.Text("  Menu", size=20, weight="bold", color="white"),
            ft.Divider(color="black"),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ANALYTICS,
                label="Transaction Report",
            ),
        ],
        on_change=handle_change,
    )

# --- ADD THIS NEW COMPONENT AT THE BOTTOM ---
def MonthlyStatsRow(income, expense):
    return ft.Row(
        controls=[
            # Income Box
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.ARROW_DOWNWARD, color="green", size=20),
                    ft.Column([
                        ft.Text("INCOME", size=10, color="grey"),
                        ft.Text(f"₹{income:,.0f}", weight="bold", size=16, color="white")
                    ], spacing=2)
                ]),
                bgcolor="#1A1A1A",
                border_radius=15,
                padding=15,
                expand=True, # Take up half the space
                border=ft.border.all(1, "#333333")
            ),
            
            ft.Container(width=10), # Space between boxes

            # Expense Box
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.Icons.ARROW_UPWARD, color="red", size=20),
                    ft.Column([
                        ft.Text("EXPENSE", size=10, color="grey"),
                        ft.Text(f"₹{expense:,.0f}", weight="bold", size=16, color="white")
                    ], spacing=2)
                ]),
                bgcolor="#1A1A1A",
                border_radius=15,
                padding=15,
                expand=True, # Take up half the space
                border=ft.border.all(1, "#333333")
            ),
        ]
    )