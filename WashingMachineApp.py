import tkinter as tk

class WashingMachineControlPanel:
    def __init__(self, master):
        self.master = master
        master.title("Washing Machine Control Panel")

        # Set the minimum size of the window
        master.minsize(400, 200)  # Width x Height

        # Create a frame to contain all the content
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)  # Add padding around the frame

        # Label for wash cycle selection
        self.label_cycle = tk.Label(self.frame, text="Select Wash Cycle:")
        self.label_cycle.grid(row=0, column=0, sticky="nsew")

        # Combobox for wash cycle selection
        self.combo_cycle = tk.StringVar()
        self.combo_cycle.set("Normal")  # Default wash cycle
        self.options_cycle = ["Normal", "Quick", "Delicate", "Heavy Duty"]
        self.combobox_cycle = tk.OptionMenu(self.frame, self.combo_cycle, *self.options_cycle)
        self.combobox_cycle.grid(row=0, column=1, sticky="nsew")

        # Label for temperature selection
        self.label_temp = tk.Label(self.frame, text="Select Temperature:")
        self.label_temp.grid(row=1, column=0, sticky="nsew")

        # Combobox for temperature selection
        self.combo_temp = tk.StringVar()
        self.combo_temp.set("Warm")  # Default temperature
        self.options_temp = ["Cold", "Warm", "Hot"]
        self.combobox_temp = tk.OptionMenu(self.frame, self.combo_temp, *self.options_temp)
        self.combobox_temp.grid(row=1, column=1, sticky="nsew")

        # Label for spin speed selection
        self.label_spin = tk.Label(self.frame, text="Select Spin Speed:")
        self.label_spin.grid(row=2, column=0, sticky="nsew")

        # Combobox for spin speed selection
        self.combo_spin = tk.StringVar()
        self.combo_spin.set("Medium")  # Default spin speed
        self.options_spin = ["Low", "Medium", "High"]
        self.combobox_spin = tk.OptionMenu(self.frame, self.combo_spin, *self.options_spin)
        self.combobox_spin.grid(row=2, column=1, sticky="nsew")

        # Button to start the washing process
        self.button_start = tk.Button(self.frame, text="Start Washing", command=self.start_washing)
        self.button_start.grid(row=3, column=0, columnspan=2, sticky="nsew")

        # Configure grid to expand widgets to fill available space
        for i in range(4):
            self.frame.grid_rowconfigure(i, weight=1)
        for i in range(2):
            self.frame.grid_columnconfigure(i, weight=1)

    def start_washing(self):
        cycle = self.combo_cycle.get()
        temp = self.combo_temp.get()
        spin = self.combo_spin.get()
        print(f"Starting {cycle} cycle with {temp} temperature and {spin} spin speed.")

root = tk.Tk()
app = WashingMachineControlPanel(root)
root.mainloop()
