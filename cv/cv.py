"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box()


app = rx.App()
app.add_page(
    index,
    title="The Tom World",
    description="You wont leave here alive"
    )

