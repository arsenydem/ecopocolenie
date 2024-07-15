import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedTk

class ForestMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Forest Ecosystem Monitoring")
        self.root.geometry("600x350")

        # Apply theme
        self.root.set_theme("radiance")

        # Main frame
        self.frame = ttk.Frame(root, padding="10 10 10 10")
        self.frame.pack(pady=20, padx=20)

        # Title
        self.title_label = ttk.Label(self.frame, text="Forest Ecosystem Monitoring", font=("Arial", 18, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Forest Section Name
        self.section_label = ttk.Label(self.frame, text="Forest Section Name:", font=("Arial", 12))
        self.section_label.grid(row=1, column=0, pady=5, sticky="e")
        self.section_entry = ttk.Entry(self.frame, width=30)
        self.section_entry.grid(row=1, column=1, pady=5, padx=10)

        # Biodiversity Score
        self.biodiversity_label = ttk.Label(self.frame, text="Biodiversity Score:", font=("Arial", 12))
        self.biodiversity_label.grid(row=2, column=0, pady=5, sticky="e")
        self.biodiversity_entry = ttk.Entry(self.frame, width=30)
        self.biodiversity_entry.grid(row=2, column=1, pady=5, padx=10)

        # Deforestation Risk
        self.risk_label = ttk.Label(self.frame, text="Deforestation Risk:", font=("Arial", 12))
        self.risk_label.grid(row=3, column=0, pady=5, sticky="e")
        self.risk_entry = ttk.Entry(self.frame, width=30)
        self.risk_entry.grid(row=3, column=1, pady=5, padx=10)
        
        # Coordinates
        self.coords_label = ttk.Label(self.frame, text="Coordinates (Lat, Long):", font=("Arial", 12))
        self.coords_label.grid(row=4, column=0, pady=5, sticky="e")
        self.coords_entry = ttk.Entry(self.frame, width=30)
        self.coords_entry.grid(row=4, column=1, pady=5, padx=10)

        # Save Button
        self.save_button = ttk.Button(self.frame, text="Save Data", command=self.save_data)
        self.save_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Display Data Button
        self.display_button = ttk.Button(self.frame, text="Display Data", command=self.display_data)
        self.display_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.data = []

    def save_data(self):
        section = self.section_entry.get()
        biodiversity = self.biodiversity_entry.get()
        risk = self.risk_entry.get()
        coordinates = self.coords_entry.get()

        if section and biodiversity and risk and coordinates:
            self.data.append({
                "section": section,
                "biodiversity": biodiversity,
                "risk": risk,
                "coordinates": coordinates
            })
            self.show_warning("Success", "Data saved successfully!")
            self.section_entry.delete(0, tk.END)
            self.biodiversity_entry.delete(0, tk.END)
            self.risk_entry.delete(0, tk.END)
            self.coords_entry.delete(0, tk.END)
        else:
            self.show_warning("Input Error", "Please fill out all fields")

    def display_data(self):
        if not self.data:
            self.show_warning("No Data", "No data to display")
            return

        data_str = "Forest Section Data:\n"
        for entry in self.data:
            data_str += f"\nSection: {entry['section']}\n"
            data_str += f"Biodiversity Score: {entry['biodiversity']}\n"
            data_str += f"Deforestation Risk: {entry['risk']}\n"
            data_str += f"Coordinates: {entry['coordinates']}\n"
            data_str += "-" * 20

        self.show_info("Forest Data", data_str)

    def show_info(self, title, message):
        top = tk.Toplevel(self.root)
        top.title(title)
        top.geometry("400x300")
        top.transient(self.root)
        top.grab_set()

        msg_frame = ttk.Frame(top, padding="10 10 10 10")
        msg_frame.pack(expand=True, fill=tk.BOTH)

        msg_text = scrolledtext.ScrolledText(msg_frame, wrap=tk.WORD, font=("Arial", 12))
        msg_text.insert(tk.END, message)
        msg_text.config(state=tk.DISABLED)
        msg_text.pack(expand=True, fill=tk.BOTH)

        ok_button = ttk.Button(msg_frame, text="OK", command=top.destroy)
        ok_button.pack(pady=10)

    def show_warning(self, title, message):
        top = tk.Toplevel(self.root)
        top.title(title)
        top.geometry("300x150")
        top.transient(self.root)
        top.grab_set()

        msg_frame = ttk.Frame(top, padding="10 10 10 10")
        msg_frame.pack(expand=True, fill=tk.BOTH)

        msg_label = ttk.Label(msg_frame, text=message, wraplength=250, font=("Arial", 12))
        msg_label.pack(pady=10)

        ok_button = ttk.Button(msg_frame, text="OK", command=top.destroy)
        ok_button.pack(pady=10)

if __name__ == "__main__":
    root = ThemedTk()
    app = ForestMonitorApp(root)
    root.mainloop()
