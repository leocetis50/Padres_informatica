import flet as ft
import flet_video as fv

def main(page:ft.Page):
    page.title = "Padres de la informatica."
    page.bgcolor = ft.Colors.BLUE_GREY_900

    videos = [
        {"titulo" : "Blaise Pascal",
        "descripcion": "Blaise Pascal fue matematico, fisico y filosofo frances.",
        "video": "https://drive.google.com/uc?export=download&id=1lSZ3jGopBYp8ZSIq3L9PwuiGIzJ9WHHl"},
        {"titulo" : "Charles Babbage",
        "descripcion": "Conocido como el padre de la computadora...",
        "video": "https://drive.google.com/uc?export=download&id=1Ce0qOKghbjfqcQUpRpIDgs4HsQ5JMsSU"},
        {"titulo" : "Ada Lovelace",
        "descripcion": "Ada lovelace fue reconocida como la primera programadora.",
        "video": "https://drive.google.com/uc?export=download&id=15QgQgiQzxUa9IhYrdYd47_gkEPJsAW6m"},
        {"titulo" : "Hedy Lamarr",
        "descripcion": "A de mas de actris inventora de la tecnologia salto de fracuencia.",
        "video": "https://drive.google.com/uc?export=download&id=1DJSrPRUUM1RjpUPouBX1IA5OXHWbQyqy"},
        {"titulo": "John Backus",
        "descripcion": "Lidereo la creacion del primer lenguaje de programacion FORTRAN.",
        "video": "https://drive.google.com/uc?export=download&id=1ucAoT-JDD8gN6A9Lv0fYyAtAUU__Zvn7"},
        {"titulo": "Gido Van Rossum",
        "descripcion": "Creador del lenguaje de programacion Python.",
        "video": "https://drive.google.com/uc?export=download&id=1buCeF6EKBjF1KuHS4FED86Z7tR-P_BGC"}
        
        ]
    
    indice_actual=[0]
    contenedor=ft.Container(width=700,height=600)

    boton_anterior = ft.ElevatedButton("⏮ Anterior", width=150)
    boton_siguiente = ft.ElevatedButton("⏭ Siguiente", width=150)

    def mostrar_video():
        vid = videos [indice_actual[0]]
        contenedor.content = ft.Column([
            ft.Video(
                expand=True,
                playlist=[ft.VideoMedia(vid["video"])],
                width=600,
                height=350,
                autoplay=True,
                show_controls=True,
            ),
            ft.Text(vid["titulo"],size=28,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),
            ft.Text(vid["descripcion"],size=16,italic=True,text_align=ft.TextAlign.CENTER,color=ft.Colors.WHITE70),
            ft.Row([boton_anterior, boton_siguiente],
                   alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20)
        ],
        alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )
    page.update()

    def anterior_click(e):
        indice_actual[0] = (indice_actual[0]-1) % len (videos)
        mostrar_video()

    def siguiente_click(e):
        indice_actual[0] = (indice_actual[0]+1) % len (videos)
        mostrar_video()

    boton_anterior.on_click = anterior_click
    boton_siguiente.on_click = siguiente_click

    page.add(ft.Container(expand=True,alignment=ft.alignment.center,content=contenedor))
    mostrar_video()

ft.app(target=main)