from tkinter import messagebox

def add_driver(driver_id, driver_name, driver_contact, data, refresh_all, save_data):
    did = driver_id.get().strip()
    name = driver_name.get().strip()
    contact = driver_contact.get().strip()

    if not did or not name:
        messagebox.showwarning("Warning", "All fields required!")
        return

    if any(d["Driver ID"] == did for d in data["drivers"]):
        messagebox.showerror("Error", "Driver ID already exists!")
        return

    data["drivers"].append({"Driver ID": did, "Name": name, "Contact": contact})
    save_data(data)
    refresh_all()

    driver_id.delete(0, "end")
    driver_name.delete(0, "end")
    driver_contact.delete(0, "end")

def delete_driver(driver_tree, data, refresh_all, save_data):
    selected = driver_tree.selection()
    if not selected:
        return
    item = driver_tree.item(selected)["values"]
    data["drivers"] = [d for d in data["drivers"] if d["Driver ID"] != item[0]]
    save_data(data)
    refresh_all()
