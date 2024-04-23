from typing import Callable
from random import choice

def handle_hello() -> str:
    return "Hello There!"

def handle_ankle() -> str:
    return "It's Angel not Ankle"

def handle_angel() -> str:
    return "It's Ankle not Angel"

def handle_nico() -> str:
    return "Yes Nico is Gay"

def handle_default() -> str:
    return choice([
        "Stfu I can't understand you",
        "What the sigma...",
        "Chat ban this kid",
        "Angel ban this kid",
        "kys",
        "L rizz",
        "IM GONNA TOUCH YOU",
        "Check Behind You"
    ])

def handle_skinwalker() -> str:
    return "https://media1.tenor.com/m/b8gWCDKua2oAAAAd/side-eye.gif"

def handle_sigma() -> str:
    return "https://media1.tenor.com/m/--QA_a_2QSgAAAAC/what-the-sigma.gif"

def get_response(user_input: str) -> str:
    if user_input.startswith('#'):
        lowerd: str = user_input.lower()
        
        switch_case: dict[str, Callable[[], str]] = {
            '#hello': handle_hello,
            '#ankle': handle_ankle,
            '#angel': handle_angel,
            '#nico': handle_nico,
            "#whatthesigma": handle_sigma,
            "#skinwalker": handle_skinwalker
        }

        for key, value in switch_case.items():
            if key in lowerd:
                return value()
        
        return handle_default()
    else:
        return