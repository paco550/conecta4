# Conecta 4

¡Bienvenido a **Conecta 4**! Este proyecto es una implementación del clásico juego de mesa "Conecta 4" utilizando [Reflex](https://reflex.dev/), un framework de Python para construir interfaces de usuario interactivas.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Agradecimientos](#agradecimientos)

## Descripción

"Conecta 4" es un juego para dos jugadores en el que se turnan para dejar caer fichas de color en una cuadrícula vertical. El objetivo es ser el primero en formar una línea horizontal, vertical o diagonal de cuatro fichas consecutivas del mismo color.

Este proyecto busca replicar esa experiencia de manera interactiva y amigable utilizando Reflex.

## Características

- **Interfaz Intuitiva**: Diseño limpio y fácil de usar.
- **Juego en Tiempo Real**: Los jugadores pueden alternar turnos sin retrasos.
- **Indicador de Turno**: Muestra claramente de quién es el turno actual.
- **Detección de Ganador**: Identifica automáticamente al ganador y muestra un mensaje de felicitación.
- **Reinicio de Partida**: Permite reiniciar el juego en cualquier momento.
- **Contador de Victorias**: Lleva un registro de las victorias de cada jugador.

## Instalación

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/tu_usuario/conecta_4.git
    ```

2. **Navega al directorio del proyecto**:

    ```bash
    cd conecta_4
    ```

3. **Crea un entorno virtual (opcional pero recomendado)**:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa 'env\Scripts\activate'
    ```

4. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Para iniciar la aplicación, ejecuta:

```bash
python main.py
