from datetime import datetime

""" The add_time function takes in two hours of the day in HH:MM format,
initial time and final time, 
and outputs the number of minutes passed between the initial time
"""
def add_time(initial_time, final_time):
    initial_time = datetime.strptime(initial_time, "%H:%M")
    final_time = datetime.strptime(final_time, "%H:%M")
    elapsed_time = final_time - initial_time
    elapsed_time =int(elapsed_time.seconds/60)
    return elapsed_time
