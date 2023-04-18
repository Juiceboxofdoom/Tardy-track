import datetime
import csv
import os

while True:
    # Prompt the user to enter the student's name
    student_number = input("Enter the student's number: ")

    # Get the current date and time
    current_time = datetime.datetime.now()

    # Determine the current class period based on the current time
    if current_time.time() >= datetime.time(8, 15) and current_time.time() < datetime.time(9, 5):
        class_period = "1st Period"
    elif current_time.time() >= datetime.time(9, 7) and current_time.time() < datetime.time(9, 57):
        class_period = "2nd Period"
    elif current_time.time() >= datetime.time(10, 5) and current_time.time() < datetime.time(10, 55):
        class_period = "3rd Period"
    elif current_time.time() >= datetime.time(10, 57) and current_time.time() < datetime.time(11, 47):
        class_period = "4th Period"
    elif current_time.time() >= datetime.time(12, 12) and current_time.time() < datetime.time(13, 2):
        class_period = "5th Period"
    elif current_time.time() >= datetime.time(13, 4) and current_time.time() < datetime.time(13, 54):
        class_period = "6th Period"
    elif current_time.time() >= datetime.time(14, 2) and current_time.time() < datetime.time(14, 52):
        class_period = "7th Period"
    elif current_time.time() >= datetime.time(14, 54) and current_time.time() < datetime.time(15, 44):
        class_period = "8th Period"
    elif current_time.time() >= datetime.time(15, 55) and current_time.time() < datetime.time(15, 15):
        class_period = "9th Period"
    else:
        class_period = "Unknown"

    # Prompt the user to enter the time the student arrived late
    #late_time = input("Enter the time the student arrived late: ")

    # Print out the tardy slip
    print("TARDY SLIP")
    print("Student Name:", student_number)
    print("Class Period:", class_period)
    #print("Arrival Time:", late_time)
    print("Date:", current_time.date())
    print("Time:", current_time.time())

    # Write the tardy slip information to a CSV file
    with open('tardy_slips.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([student_number, class_period, current_time.date(), current_time.time()])

#delete all #'s below on the fist collom
    # Send the tardy slip output to the default printer
    printer_name = None  # Change this to the name of your printer if necessary
    if os.name == 'nt':  # Check if the operating system is Windows
        from win32 import win32print
        printer_name = win32print.GetDefaultPrinter()
        print_job = win32print.OpenPrinter(printer_name)
        win32print.StartDocPrinter(print_job, 1, ('Tardy Slip', None, None))
        win32print.StartPagePrinter(print_job)
        win32print.WritePrinter(print_job, str.encode('\n'.join([
            "TARDY SLIP",
            "Student Name: " + student_number,
            "Class Period: " + class_period,
            "Date: " + str(current_time.date()),
            "Time: " + str(current_time.time()),
            "",
            "",
            "",
            "",
            "",
            "Rip Off"
        ])))
        win32print.EndPagePrinter(print_job)
        win32print.EndDocPrinter(print_job)
    else:  # For other operating systems, you'll need to find a suitable print command
        print("Printing not supported on this operating system")
