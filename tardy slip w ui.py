import datetime
import csv
import os
import tkinter as tk
from tkinter import ttk
  
 
LARGEFONT =("Verdana", 35)


    
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Home, Tardy, Checkin):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # Home, Tardy, Checkin respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Home)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame Home
  
class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Home", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Tardy",
        command = lambda : controller.show_frame(Tardy))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Check in",
        command = lambda : controller.show_frame(Checkin))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
          
  
  
# second window frame Tardy
class Tardy(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Tardy", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
         # Entry widget to get input from user
        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Button to submit the input
        submit_button = ttk.Button(self, text="Submit", command=self.submit)
        submit_button.grid(row=2, column=1, padx=10, pady=10)
        
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Check in",
                            command = lambda : controller.show_frame(Checkin))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
  
    def submit(self):
        # Get the input value and do something with it
        input_value = self.entry.get()

        # Prompt the user to enter the student's name
        student_number = self.entry.get()

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
            writer.writerow([student_number, class_period, current_time.date(), current_time.time(),"Tardy"])

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
#    else:  # For other operating systems, you'll need to find a suitable print command
#        print("Printing not supported on this operating system")

        print("Input value:", input_value)
        self.entry.delete(0, 'end')
  
  
# third window frame Checkin
class Checkin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Check in", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

         # Entry widget to get input from user
        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Button to submit the input
        submit_button = ttk.Button(self, text="Submit", command=self.submit)
        submit_button.grid(row=2, column=1, padx=10, pady=10)
        

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Tardy",
                            command = lambda : controller.show_frame(Tardy))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Home",
                            command = lambda : controller.show_frame(Home))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
    
    def submit(self):
        # Get the input value and do something with it
        input_value = self.entry.get()

        # Prompt the user to enter the student's name
        student_number = self.entry.get()

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

        # Print out the tardy slip
        print("Check in SLIP")
        print("Student Name:", student_number)
        print("Class Period:", class_period)
        #print("Arrival Time:", late_time)
        print("Date:", current_time.date())
        print("Time:", current_time.time())

        # Write the tardy slip information to a CSV file
        with open('tardy_slips.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_number, class_period, current_time.date(), current_time.time(),"Check in"])

        # Send the tardy slip output to the default printer
        printer_name = None  # Change this to the name of your printer if necessary
        if os.name == 'nt':  # Check if the operating system is Windows
            from win32 import win32print
            printer_name = win32print.GetDefaultPrinter()
            print_job = win32print.OpenPrinter(printer_name)
            win32print.StartDocPrinter(print_job, 1, ('Tardy Slip', None, None))
            win32print.StartPagePrinter(print_job)
            win32print.WritePrinter(print_job, str.encode('\n'.join([
                "Check in Slip",
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
#    else:  # For other operating systems, you'll need to find a suitable print command
#        print("Printing not supported on this operating system")

        print("Input value:", input_value)
        self.entry.delete(0, 'end')  
  
# Driver Code
app = tkinterApp()
app.mainloop()