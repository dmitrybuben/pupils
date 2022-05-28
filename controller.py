import user_interface as ui
import input_data as id
import find_data as fd


def run():
    ui.welcome()
    if ui.init() == 1:
        id.namesurname()
        id.address()
        id.cabinet()
    else:
        fd.findattr()
