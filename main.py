import flet as ft


def main(page: ft.Page):
    # Set the browser tab title and alignment
    page.title = "Data Science & Analytics Portfolio"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Define a clean header banner
    header = ft.Container(
        content=ft.Text(
            "My Data Portfolio",
            size=32,
            weight=ft.FontWeight.BOLD
        ),
        padding=20,
    )

    # Placeholder layout for upcoming project showcase cards
    project_grid = ft.Column(
        controls=[
            ft.Text("Project showcase modules coming soon...", size=16),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Compile the interface elements onto the viewable page
    page.add(
        header,
        ft.Divider(),
        project_grid
    )


# The critical hook that allows cloud providers to execute the UI via Uvicorn
app = ft.app(main, export_asgi_app=True)