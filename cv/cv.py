"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import cv.styles.styles as styles
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box()


app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style= styles.BASE_STYLE
)
app.add_page(
    index,
    title="The Tom World",
    description="You wont leave here alive"
    )

