import tkinter as tk
from tkinter import ttk
from data_manager import load_data, save_data
from vehicle_ops import add_vehicle, delete_vehicle
from driver_ops import add_driver, delete_driver
from trip_ops import add_trip, delete_trip, show_summary

# Load data
data = load_data()

# ---------- Utility ----------
def update_tree(tree, records):
    for i in tree.get_children():
        tree.delete(i)
    for record in records:
        tree.insert("", tk.END, values=list(record.values()))

def refresh_all():
    update_tree(vehicle_tree, data["vehicles"])
    update_tree(driver_tree, data["drivers"])
    update_tree(trip_tree, data["trips"])

# ---------- GUI ----------
root = tk.Tk()
root.title("SafeDrive – Vehicle Trip Logger")
root.geometry("900x600")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# --- Vehicle Tab ---
vehicle_frame = ttk.Frame(notebook)
notebook.add(vehicle_frame, text="Vehicle Manager")

tk.Label(vehicle_frame, text="Vehicle ID").grid(row=0, column=0)
tk.Label(vehicle_frame, text="Name").grid(row=1, column=0)
tk.Label(vehicle_frame, text="Type").grid(row=2, column=0)
vehicle_id = tk.Entry(vehicle_frame)
vehicle_name = tk.Entry(vehicle_frame)
vehicle_type = tk.Entry(vehicle_frame)
vehicle_id.grid(row=0, column=1)
vehicle_name.grid(row=1, column=1)
vehicle_type.grid(row=2, column=1)
tk.Button(vehicle_frame, text="Add Vehicle",
          command=lambda: add_vehicle(vehicle_id, vehicle_name, vehicle_type, data, refresh_all, save_data)).grid(row=3, column=0)
tk.Button(vehicle_frame, text="Delete Vehicle",
          command=lambda: delete_vehicle(vehicle_tree, data, refresh_all, save_data)).grid(row=3, column=1)
vehicle_tree = ttk.Treeview(vehicle_frame, columns=("id", "name", "type"), show="headings", height=10)
for col in ("id", "name", "type"):
    vehicle_tree.heading(col, text=col.title())
vehicle_tree.grid(row=4, column=0, columnspan=2, pady=10)

# --- Driver Tab ---
driver_frame = ttk.Frame(notebook)
notebook.add(driver_frame, text="Driver Manager")

tk.Label(driver_frame, text="Driver ID").grid(row=0, column=0)
tk.Label(driver_frame, text="Name").grid(row=1, column=0)
tk.Label(driver_frame, text="Contact").grid(row=2, column=0)
driver_id = tk.Entry(driver_frame)
driver_name = tk.Entry(driver_frame)
driver_contact = tk.Entry(driver_frame)
driver_id.grid(row=0, column=1)
driver_name.grid(row=1, column=1)
driver_contact.grid(row=2, column=1)
tk.Button(driver_frame, text="Add Driver",
          command=lambda: add_driver(driver_id, driver_name, driver_contact, data, refresh_all, save_data)).grid(row=3, column=0)
tk.Button(driver_frame, text="Delete Driver",
          command=lambda: delete_driver(driver_tree, data, refresh_all, save_data)).grid(row=3, column=1)
driver_tree = ttk.Treeview(driver_frame, columns=("id", "name", "contact"), show="headings", height=10)
for col in ("id", "name", "contact"):
    driver_tree.heading(col, text=col.title())
driver_tree.grid(row=4, column=0, columnspan=2, pady=10)

# --- Trip Tab ---
trip_frame = ttk.Frame(notebook)
notebook.add(trip_frame, text="Trip Manager")

tk.Label(trip_frame, text="Trip ID").grid(row=0, column=0)
tk.Label(trip_frame, text="Vehicle").grid(row=1, column=0)
tk.Label(trip_frame, text="Driver").grid(row=2, column=0)
tk.Label(trip_frame, text="Distance (km)").grid(row=3, column=0)
trip_id = tk.Entry(trip_frame)
trip_vehicle = tk.Entry(trip_frame)
trip_driver = tk.Entry(trip_frame)
trip_distance = tk.Entry(trip_frame)
trip_id.grid(row=0, column=1)
trip_vehicle.grid(row=1, column=1)
trip_driver.grid(row=2, column=1)
trip_distance.grid(row=3, column=1)
tk.Button(trip_frame, text="Add Trip",
          command=lambda: add_trip(trip_id, trip_vehicle, trip_driver, trip_distance, data, refresh_all, save_data)).grid(row=4, column=0)
tk.Button(trip_frame, text="Delete Trip",
          command=lambda: delete_trip(trip_tree, data, refresh_all, save_data)).grid(row=4, column=1)
tk.Button(trip_frame, text="Show Summary",
          command=lambda: show_summary(data)).grid(row=5, column=0, columnspan=2)
trip_tree = ttk.Treeview(trip_frame, columns=("id", "vehicle", "driver", "distance", "date"), show="headings", height=10)
for col in ("id", "vehicle", "driver", "distance", "date"):
    trip_tree.heading(col, text=col.title())
trip_tree.grid(row=6, column=0, columnspan=2, pady=10)

refresh_all()
root.mainloop()
