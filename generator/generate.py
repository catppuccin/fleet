from catppuccin import Flavour
from dataclasses import fields

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
        file_content = template_content
        flavour = flavours[name]
        kind = "Light" if flavour == Flavour.latte() else "Dark"

        # These are special values to replace with different values depending on the theme kind so that it looks good
        replace_special = {
            "KIND": kind,
            "NAME": f"Catppuccin {name}",
            "DIFF_ADDED_OPACITY": "40%" if kind == "Dark" else "20%",
            "DIFF_CONFLICT_OPACITY": "30%" if kind == "Dark" else "20%",
            "DIFF_DELETED_OPACITY": "20%" if kind == "Dark" else "10%",
            "IDENTIFIER_FIELD": "Text" if kind == "Dark" else "DarkViolet",
            "IDENTIFIER_FIELD_STATIC": "Teal" if kind == "Dark" else "DarkViolet",
            "IDENTIFIER_FIELD_BOOLEAN": "false" if kind == "Dark" else "true",
            "TRANSPARENT": "ffffff" if kind == "Dark" else "000000",
        }
        with open(
            f"{os.path.realpath(os.path.dirname(__file__))}/../themes/catppuccin-{name.lower()}.json",
            "w",
        ) as file:
            # Normal colours
            for field in fields(flavour):
                colour = getattr(flavour, field.name)
                file_content = file_content.replace(
                    f"{{{{{field.name.upper()}}}}}", colour.hex
                )

            # Special replacements
            for key in replace_special:
                file_content = file_content.replace(
                    f"{{{{{key}}}}}", replace_special[key]
                )
            file.write(file_content)


if __name__ == "__main__":
    main()
