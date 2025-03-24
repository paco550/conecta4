import reflex as rx
import datetime



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/python.svg" , width="50px", height="50px", margin_bottom="10px !important", margin_top="50px !important"),
        rx.link(
           f"© 2022 - {datetime.date.today().year} Francisco Fernández Bailén. Todos los derechos reservados.",
            href="https://www.linkedin.com/in/francisco-fern%C3%A1ndez-bail%C3%A9n/",
            is_external=True,
            font_size="xs",
            color="blue",
        ),
                rx.text("Hecho con 💻 y ☕ por Francisco Fernández Bailén. Construyendo ideas en la web. ", color="#C3C7CB"),
                rx.link("¿Hablamos?", href="mailto: pacofb70@gmail.com", color="blue",underline="hover"),
                margin_bottom="0px !important",
                margin_top="0px !important",
                align="center",
        )
    