import flet as ft
import flet_video as fv

def main(page = ft.Page):
    page.title = "Padres de la informatica.",
    page.bgcolor = ft.Colors.AMBER

    videos = [{
        "titulo" : "Charles Babbage"
        "descripcion:" "Conocido como el padre de la computadora..."
        "video:"},
        {"titulo" : "Ada Lovelace"
        "descripcion:" "Ada lovelace fue reconocida como la primera programadora."
        "video:"},
        {"titulo" : "Blaise Pascal"
        "descripcion:" "Blaise Pascal fue matematico, fisico y filosofo frances"
        "video:"}
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
                playtist=[ft.VideoMedia(vid["video"])],
                width=600,
                height=350,
                autoplay=True,
                show_controls=True,
            ),
            ft.Text(vid["titulo"],size=28,weight=ft.FrontWeigt.BOLD,color=ft.Colors.WHITE),
            ft.Text(vid["descripcion"],size=16,italic=True,text_align=ft.TextAlign.CENTER,color=ft.Colors.WHITE70),
            ft.Row([boton_anterior, boton_siguiente],
                   alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=40
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