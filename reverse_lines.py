def reverse_lines(file_begin, file_result):
    with open(file_begin) as input_file, open(file_result, 'w') as output_file:
        for line in input_file:
            output_file.write(f'{line.rstrip()[::-1]}\n')
