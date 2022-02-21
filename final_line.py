from urllib.parse import ParseResultBytes


def get_final_line(filename):
    f = open(filename)

    final_line = ''

    for current_line in f:
        final_line = current_line

    return final_line

print(get_final_line('/etc/passwd'))