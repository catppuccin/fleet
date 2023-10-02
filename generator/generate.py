from catppuccin import Flavour

import os


flavours = {
    "Latte": Flavour.latte(),
    "Frappe": Flavour.frappe(),
    "Macchiato": Flavour.macchiato(),
    "Mocha": Flavour.mocha(),
}


template_file = open(f"{os.path.realpath(os.path.dirname(__file__))}/theme.template")
template_content = template_file.read()
template_file.close()


def main() -> None:
    for name in flavours:
        flavour = flavours[name]
        kind = "Light" if flavour == Flavour.latte() else "Dark"
        replace = {
            "KIND": kind,
            "NAME": f"Catppuccin {name}",
            "BASE": flavour.base.hex,
            "BLUE": flavour.blue.hex,
            "CRUST": flavour.crust.hex,
            "FLAMINGO": flavour.flamingo.hex,
            "GREEN": flavour.green.hex,
            "LAVENDER": flavour.lavender.hex,
            "MANTLE": flavour.mantle.hex,
            "MAROON": flavour.maroon.hex,
            "MAUVE": flavour.mauve.hex,
            "OVERLAY0": flavour.overlay0.hex,
            "OVERLAY1": flavour.overlay1.hex,
            "OVERLAY2": flavour.overlay2.hex,
            "PEACH": flavour.peach.hex,
            "PINK": flavour.pink.hex,
            "RED": flavour.red.hex,
            "ROSEWATER": flavour.rosewater.hex,
            "SAPPHIRE": flavour.sapphire.hex,
            "SKY": flavour.sky.hex,
            "SUBTEXT0": flavour.subtext0.hex,
            "SUBTEXT1": flavour.subtext1.hex,
            "SURFACE0": flavour.surface0.hex,
            "SURFACE1": flavour.surface1.hex,
            "SURFACE2": flavour.surface2.hex,
            "TEAL": flavour.teal.hex,
            "TEXT": flavour.text.hex,
            "TRANSPARENT": "ffffff" if kind == "Dark" else "000000",
            "YELLOW": flavour.yellow.hex,
            "DIFF_ADDED_OPACITY": "40%" if kind == "Dark" else "20%",
            "DIFF_CONFLICT_OPACITY": "30%" if kind == "Dark" else "20%",
            "DIFF_DELETED_OPACITY": "20%" if kind == "Dark" else "10%",
            "IDENTIFIER_FIELD": "Text" if kind == "Dark" else "DarkViolet",
            "IDENTIFIER_FIELD_STATIC": "Teal" if kind == "Dark" else "DarkViolet",
            "IDENTIFIER_FIELD_BOOLEAN": "false" if kind == "Dark" else "true",
        }
        with open(
            f"{os.path.realpath(os.path.dirname(__file__))}/../themes/catppuccin-{name.lower()}.json",
            "w",
        ) as file:
            content = template_content
            for key in replace:
                content = content.replace(f"{{{{{key}}}}}", replace[key])
            file.write(content)


if __name__ == "__main__":
    main()
