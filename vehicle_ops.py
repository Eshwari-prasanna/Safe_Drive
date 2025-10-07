from tkinter import messagebox

def add_vehicle(vehicle_id, vehicle_name, vehicle_type, data, refresh_all, save_data):
    vid = vehicle_id.get().strip()
    name = vehicle_name.get().strip()
    vtype = vehicle_type.get().strip()

    if not vid or not name:
        messagebox.showwarning("Warning", "All fields required!")
        return

    if any(v["Vehicle ID"] == vid for v in data["vehicles"]):
        messagebox.showerror("Error", "Vehicle ID already exists!")
        return

    data["vehicles"].append({"Vehicle ID": vid, "Name": name, "Type": vtype})
    save_data(data)
    refresh_all()

    vehicle_id.delete(0, "end")
    vehicle_name.delete(0, "end")
    vehicle_type.delete(0, "end")

def delete_vehicle(vehicle_tree, data, refresh_all, save_data):
    selected = vehicle_tree.selection()
    if not selected:
        return
    item = vehicle_tree.item(selected)["values"]
    data["vehicles"] = [v for v in data["vehicles"] if v["Vehicle ID"] != item[0]]
    save_data(data)
    refresh_all()
