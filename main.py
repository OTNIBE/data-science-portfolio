import flet as ft


def main(page: ft.Page):
    page.title = "Data Science & Analytics Portfolio"
    page.theme_mode = ft.ThemeMode.DARK  # Dark mode looks incredibly sleek for portfolios
    page.padding = 0

    # ---------------------------------------------------------
    # 1. DEFINE THE CONTENT SCREENS
    # ---------------------------------------------------------

    # Screen 0: About Me
    about_content = ft.Column([
        ft.Text("About Me", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Text(
            "Computer Science and Applied Mathematics. "
            "Passionate about leveraging Python to automate financial workflows and extract actionable data.",
            size=16
        )
    ], visible=True)  # Visible by default when the app loads

    # Screen 1: Work OS | Debtors Manager
    debtors_content = ft.Column([
        ft.Text("Work OS | Debtors Manager", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Text(
            "An offline desktop application built with Python and Flet to automate financial workflows and handle database queries.",
            size=16),
        # You can add GitHub link buttons or screenshots here later!
    ], visible=False)

    # Screen 2: Automated Data Scraper
    scraper_content = ft.Column([
        ft.Text("Automated Web Scraper", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Text(
            "A Python automation pipeline utilizing the Playwright library to extract job postings and compile them into structured spreadsheets.",
            size=16),
    ], visible=False)

    # Screen 3: Web-Based Gaming Logic
    game_content = ft.Column([
        ft.Text("Interactive Web Logic: 30 Seconds", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        ft.Text(
            "A fast-paced browser game showcasing vanilla HTML and JavaScript DOM manipulation and state management.",
            size=16),
    ], visible=False)

    # Group all screens into a single container so we can toggle them easily
    content_area = ft.Container(
        content=ft.Column([about_content, debtors_content, scraper_content, game_content]),
        expand=True,  # Tells the content to take up all remaining screen space
        padding=40
    )

    # ---------------------------------------------------------
    # 2. DEFINE THE NAVIGATION RAIL (SIDEBAR)
    # ---------------------------------------------------------

    def switch_page(e):
        # Hide all screens first
        about_content.visible = False
        debtors_content.visible = False
        scraper_content.visible = False
        game_content.visible = False

        # Reveal the specific screen based on the clicked tab index
        selected_index = e.control.selected_index
        if selected_index == 0:
            about_content.visible = True
        elif selected_index == 1:
            debtors_content.visible = True
        elif selected_index == 2:
            scraper_content.visible = True
        elif selected_index == 3:
            game_content.visible = True

        page.update()  # Push the changes to the browser

    sidebar = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        # The physical buttons on the sidebar
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="Profile"),
            ft.NavigationRailDestination(icon=ft.Icons.DESKTOP_WINDOWS, label="Debtors OS"),
            ft.NavigationRailDestination(icon=ft.Icons.AUTO_GRAPH, label="Data Scraper"),
            ft.NavigationRailDestination(icon=ft.Icons.GAMES, label="Web Logic"),
        ],
        on_change=switch_page,
    )

    # ---------------------------------------------------------
    # 3. COMPILE THE LAYOUT
    # ---------------------------------------------------------

    # Place the sidebar and the content area side-by-side using a Row
    main_layout = ft.Row(
        controls=[
            sidebar,
            ft.VerticalDivider(width=1),
            content_area
        ],
        expand=True
    )

    page.add(main_layout)


app = ft.app(main, export_asgi_app=True)