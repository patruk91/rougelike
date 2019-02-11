import ui


def validate_string_input(string, condition=""):
    """
    Validate if string from input is not empty and is in given condition.
    Condition must be in format: ["a", "b", "c".....]

    >>> validate_string_input("", ["s"])
    ERROR: Input can't be empty
    False
    >>> validate_string_input("s", ["c"])
    ERROR: Input must be in ['c']
    False
    >>> validate_string_input("Not_empty", "")
    True
    >>> validate_string_input("content", ["content"])
    True
    """
    is_string_correct = True
    if not string:
        ui.print_error("Input can't be empty")
        is_string_correct = False
    if condition:
        if string:
            if string not in condition:
                ui.print_error("Input must be in {}".format(condition))
                is_string_correct = False

    return is_string_correct
