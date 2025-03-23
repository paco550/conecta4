"""Conecta 4 en Reflex."""

import reflex as rx
from typing import List, Optional

# Definimos primero la clase State
class GameState(rx.State):  # Cambiamos el nombre de State a GameState
    tablero: List[List[Optional[bool]]] = [[None for _ in range(7)] for _ in range(6)]
    turno_rojo: bool = True
    contador_partidas: int = 1
    
    def colocar_ficha(self, columna: int):
        for fila in range(5, -1, -1):
            if self.tablero[fila][columna] is None:
                self.tablero[fila][columna] = self.turno_rojo
                self.turno_rojo = not self.turno_rojo
                break

    def nueva_partida(self):
        self.tablero = [[None for _ in range(7)] for _ in range(6)]
        self.contador_partidas += 1
        self.turno_rojo = self.contador_partidas % 2 == 1

# Luego las funciones auxiliares
def create_cell(x: int, y: int):
    return rx.table.cell(
        rx.button(
            style={
                "width": "50px",
                "height": "50px",
                "border": "1px solid black",
                "background": rx.cond(
                    GameState.tablero[y][x] == None,  # Usamos GameState en lugar de State
                    "white",
                    rx.cond(
                        GameState.tablero[y][x] == True,
                        "red",
                        "yellow"
                    )
                ),
                "border-radius": "25px",
            },
            on_click=lambda: GameState.colocar_ficha(x),  # Usamos GameState
        ),
        style={
            "border": "1px solid black",
            "width": "50px",
            "height": "50px",
            "padding": "0px"
        }
    )

def create_board():
    return rx.table.root(
        rx.table.body(
            rx.foreach(
                range(6),
                lambda y: rx.table.row(
                    *[create_cell(x, y) for x in range(7)],
                    style={"border": "1px solid black"}
                )
            )
        ),
        variant="surface",
        size="3",
        width="fit-content",
        style={
            "border": "2px solid black",
            "border-collapse": "collapse"
        }
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to conecta 4!", size="9"),
            rx.text(
                "Get started!",
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",      
    ),
    rx.vstack(
        rx.heading(
            rx.cond(
                GameState.turno_rojo,  # Usamos GameState
                "Turno: ROJO",
                "Turno: AMARILLO"
            )
        ),
        create_board(),
        rx.button(
            "Nueva Partida",
            on_click=GameState.nueva_partida  # Usamos GameState
        ),
        align="center",
        spacing="5",
        width="100%"
    ),
    
   
        rx.logo(),
    ),

    


app = rx.App()
app.add_page(index)

