def run_timing():
    """"This function continuously asks how long it takes a runner 
    to finish their 10km and averages the responses."""

    number_of_runs = 0
    total_time = 0

    while True:
        a_run = input("Enter 10 km run time here: ")
        if not a_run:
            break
        number_of_runs += 1
        total_time += float(a_run)

    average_time = float(total_time/number_of_runs)

    print(f"You had an average of {average_time} over {number_of_runs} runs.")


run_timing()