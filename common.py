import ui


def validate_string_input(string):
    is_string_correct = True
    if not string:
        ui.print_error("Input can't be empty")
        is_string_correct = False

    return is_string_correct
