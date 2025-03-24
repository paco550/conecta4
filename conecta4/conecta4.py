"""Conecta 4 en Reflex."""
import reflex as rx
from typing import List, Optional

from conecta4.components.footer import footer

class GameState(rx.State):
    tablero: List[List[Optional[bool]]] = [[None for _ in range(7)] for _ in range(6)]
    turno_rojo: bool = True
    contador_partidas: int = 1
    victorias_rojo: int = 0
    victorias_amarillo: int = 0
    hay_ganador: bool = False
    ultimo_ganador: Optional[bool] = None

    def verificar_victoria(self) -> bool:
        # Verificar horizontal
        for fila in range(6):
            for col in range(4):  # Solo necesitamos verificar hasta la columna 4
                if (self.tablero[fila][col] is not None and
                    self.tablero[fila][col] == self.tablero[fila][col + 1] == 
                    self.tablero[fila][col + 2] == self.tablero[fila][col + 3]):
                    return True

        # Verificar vertical
        for fila in range(3):  # Solo necesitamos verificar hasta la fila 3
            for col in range(7):
                if (self.tablero[fila][col] is not None and
                    self.tablero[fila][col] == self.tablero[fila + 1][col] == 
                    self.tablero[fila + 2][col] == self.tablero[fila + 3][col]):
                    return True

        # Verificar diagonal descendente
        for fila in range(3):
            for col in range(4):
                if (self.tablero[fila][col] is not None and
                    self.tablero[fila][col] == self.tablero[fila + 1][col + 1] == 
                    self.tablero[fila + 2][col + 2] == self.tablero[fila + 3][col + 3]):
                    return True

        # Verificar diagonal ascendente
        for fila in range(3, 6):
            for col in range(4):
                if (self.tablero[fila][col] is not None and
                    self.tablero[fila][col] == self.tablero[fila - 1][col + 1] == 
                    self.tablero[fila - 2][col + 2] == self.tablero[fila - 3][col + 3]):
                    return True

        return False
    
    def colocar_ficha(self, columna: int):
        if self.hay_ganador:
            return
            
        for fila in range(5, -1, -1):
            if self.tablero[fila][columna] is None:
                self.tablero[fila][columna] = self.turno_rojo
                
                # Verificar si hay victoria
                if self.verificar_victoria():
                    if self.turno_rojo:
                        self.victorias_rojo += 1
                        self.ultimo_ganador = True
                    else:
                        self.victorias_amarillo += 1
                        self.ultimo_ganador = False
                    self.hay_ganador = True
                    return
                
                self.turno_rojo = not self.turno_rojo
                break

    def nueva_partida(self):
        """Reinicia solo la partida actual."""
        self.tablero = [[None for _ in range(7)] for _ in range(6)]
        self.contador_partidas += 1
        self.turno_rojo = self.contador_partidas % 2 == 1
        self.hay_ganador = False
        self.ultimo_ganador = None

    def resetear_todo(self):
        """Reinicia todo el juego, incluyendo contadores de victoria."""
        self.tablero = [[None for _ in range(7)] for _ in range(6)]
        self.contador_partidas = 1
        self.turno_rojo = True
        self.victorias_rojo = 0
        self.victorias_amarillo = 0
        self.hay_ganador = False
        self.ultimo_ganador = None

def create_cell(x: int, y: int):
    return rx.table.cell(
        rx.button(
            style={
                "width": "50px",
                "height": "50px",
                "border": "1px solid black",
                "background": rx.cond(
                    GameState.tablero[y][x] == None,
                    "white",
                    rx.cond(
                        GameState.tablero[y][x] == True,
                        "red",
                        "yellow"
                    )
                ),
                "border-radius": "25px",
            },
            on_click=lambda: GameState.colocar_ficha(x),
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
                href="https://github.com/paco550/conecta4",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",      
        ),
        rx.vstack(
        # Marcador
        rx.hstack(
            rx.vstack(
                rx.heading("ROJO"),
                rx.heading(GameState.victorias_rojo, size="4"),
                color="red",
            ),
            rx.vstack(
                rx.heading("AMARILLO"), 
                rx.heading(GameState.victorias_amarillo, size="4"),
                color="yellow",
            ),
            spacing="5",  # Cambiado de "20" a "5"
        ),
        
        # Mensaje de victoria
        rx.cond(
            GameState.hay_ganador,
            rx.heading(
                rx.cond(
                    GameState.ultimo_ganador == False,
                    "¡GANÓ AMARILLO!",
                    "¡GANÓ ROJO!"
                ),
                color=rx.cond(
                    GameState.ultimo_ganador == False,
                    "yellow",
                    "red"
                ),
                size="6",
            ),
        ),
        
        # Turno actual (solo se muestra si no hay ganador)
        rx.cond(
            ~GameState.hay_ganador,
            rx.heading(
                rx.cond(
                    GameState.turno_rojo,
                    "Turno: ROJO",
                    "Turno: AMARILLO"
                )
            ),
        ),
        
        # Tablero
        create_board(),
        
        # Botones
        rx.hstack(
            rx.button(
                "Nueva Partida",
                on_click=GameState.nueva_partida
            ),
            rx.button(
                "Resetear Todo",
                on_click=GameState.resetear_todo
            ),
            spacing="5",
        ),
        
        align="center",
        spacing="5",
        width="100%"
    ),
    rx.box(
    footer(),
    rx.logo(),
    ),
    align="center",
        margin_top="20px",
        # spacing="5",
        width="100%",
        size="4",

)

    


app = rx.App()
app.add_page(index)

