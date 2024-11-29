import tkinter as tk
from tkinter import ttk, messagebox

# Main Application Class
class HospitalManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("800x600")
        
        # Data storage
        self.patients = []
        self.staff = []
        self.appointments = []

        # Title
        title = tk.Label(self.root, text="Hospital Management System", font=("Arial", 20, "bold"))
        title.pack(pady=20)

        # Buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Manage Patients", command=self.manage_patients, width=20).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Manage Staff", command=self.manage_staff, width=20).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Manage Appointments", command=self.manage_appointments, width=20).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="Exit", command=self.root.quit, width=20).grid(row=0, column=3, padx=10)

    # Patient Management
    def manage_patients(self):
        self.clear_frame()
        
        tk.Label(self.root, text="Manage Patients", font=("Arial", 16)).pack(pady=10)
        
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="Name: ").grid(row=0, column=0)
        name_entry = tk.Entry(form_frame, width=20)
        name_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Age: ").grid(row=1, column=0)
        age_entry = tk.Entry(form_frame, width=20)
        age_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Gender: ").grid(row=2, column=0)
        gender_entry = ttk.Combobox(form_frame, values=["Male", "Female"], width=18)
        gender_entry.grid(row=2, column=1)

        tk.Label(form_frame, text="Ailment: ").grid(row=3, column=0)
        ailment_entry = tk.Entry(form_frame, width=20)
        ailment_entry.grid(row=3, column=1)

        def add_patient():
            name = name_entry.get()
            age = age_entry.get()
            gender = gender_entry.get()
            ailment = ailment_entry.get()

            if name and age and gender and ailment:
                self.patients.append({"Name": name, "Age": age, "Gender": gender, "Ailment": ailment})
                messagebox.showinfo("Success", "Patient added successfully!")
                name_entry.delete(0, tk.END)
                age_entry.delete(0, tk.END)
                gender_entry.set("")
                ailment_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please fill all fields.")

        tk.Button(form_frame, text="Add Patient", command=add_patient).grid(row=4, column=0, columnspan=2, pady=10)

        # Patient List
        tk.Label(self.root, text="Patient List", font=("Arial", 14)).pack(pady=10)
        
        patient_list = tk.Listbox(self.root, width=80, height=10)
        patient_list.pack(pady=10)
        
        def update_patient_list():
            patient_list.delete(0, tk.END)
            for patient in self.patients:
                patient_list.insert(tk.END, f"{patient['Name']} - {patient['Age']} years - {patient['Gender']} - {patient['Ailment']}")

        tk.Button(self.root, text="View Patients", command=update_patient_list).pack()

    # Staff Management
    def manage_staff(self):
        self.clear_frame()
        
        tk.Label(self.root, text="Manage Staff", font=("Arial", 16)).pack(pady=10)
        
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)
        
        tk.Label(form_frame, text="Name: ").grid(row=0, column=0)
        name_entry = tk.Entry(form_frame, width=20)
        name_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Role: ").grid(row=1, column=0)
        role_entry = tk.Entry(form_frame, width=20)
        role_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Department: ").grid(row=2, column=0)
        dept_entry = tk.Entry(form_frame, width=20)
        dept_entry.grid(row=2, column=1)

        def add_staff():
            name = name_entry.get()
            role = role_entry.get()
            department = dept_entry.get()

            if name and role and department:
                self.staff.append({"Name": name, "Role": role, "Department": department})
                messagebox.showinfo("Success", "Staff member added successfully!")
                name_entry.delete(0, tk.END)
                role_entry.delete(0, tk.END)
                dept_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please fill all fields.")

        tk.Button(form_frame, text="Add Staff", command=add_staff).grid(row=3, column=0, columnspan=2, pady=10)

        # Staff List
        tk.Label(self.root, text="Staff List", font=("Arial", 14)).pack(pady=10)
        
        staff_list = tk.Listbox(self.root, width=80, height=10)
        staff_list.pack(pady=10)
        
        def update_staff_list():
            staff_list.delete(0, tk.END)
            for staff in self.staff:
                staff_list.insert(tk.END, f"{staff['Name']} - {staff['Role']} - {staff['Department']}")

        tk.Button(self.root, text="View Staff", command=update_staff_list).pack()

    # Appointment Management
    def manage_appointments(self):
        self.clear_frame()
        
        tk.Label(self.root, text="Manage Appointments", font=("Arial", 16)).pack(pady=10)

        # Add similar functionality for appointments (as above).

    # Utility to clear the frame
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystem(root)
    root.mainloop()