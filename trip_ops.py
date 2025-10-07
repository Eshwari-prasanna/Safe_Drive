from tkinter import messagebox
from datetime import datetime

def add_trip(trip_id, trip_vehicle, trip_driver, trip_distance, data, refresh_all, save_data):
    tid = trip_id.get().strip()
    vid = trip_vehicle.get().strip()
    did = trip_driver.get().strip()
    distance = trip_distance.get().strip() or "0"
    date = datetime.now().strftime("%Y-%m-%d")

    if not tid or not vid or not did:
        messagebox.showwarning("Warning", "All fields required!")
        return

    if any(t["Trip ID"] == tid for t in data["trips"]):
        messagebox.showerror("Error", "Trip ID already exists!")
        return

    data["trips"].append({
        "Trip ID": tid,
        "Vehicle": vid,
        "Driver": did,
        "Distance": distance,
        "Date": date
    })

    save_data(data)
    refresh_all()

    trip_id.delete(0, "end")
    trip_vehicle.delete(0, "end")
    trip_driver.delete(0, "end")
    trip_distance.delete(0, "end")

def delete_trip(trip_tree, data, refresh_all, save_data):
    selected = trip_tree.selection()
    if not selected:
        return
    item = trip_tree.item(selected)["values"]
    data["trips"] = [t for t in data["trips"] if t["Trip ID"] != item[0]]
    save_data(data)
    refresh_all()

def show_summary(data):
    total_trips = len(data["trips"])
    total_distance = sum(float(t.get("Distance", 0)) for t in data["trips"])
    messagebox.showinfo(
        "Trip Summary",
        f"Total Trips: {total_trips}\nTotal Distance: {total_distance:.2f} km"
    )
