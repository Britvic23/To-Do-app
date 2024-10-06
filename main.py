import tkinter as tk
from tkinter import messagebox
import json
import os

# Datoteka za spremanje zadataka
FILE_NAME = 'tasks.json'

# Funkcija za učitavanje zadataka iz datoteke
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Funkcija za spremanje zadataka u datoteku
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file)

# Dodavanje zadatka
def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Upozorenje", "Unesite zadatak!")

# Označavanje zadatka kao dovršenog
def complete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks[index]['completed'] = not tasks[index]['completed']
        update_task_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Upozorenje", "Odaberite zadatak!")

# Brisanje zadatka
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        tasks.pop(index)
        update_task_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Upozorenje", "Odaberite zadatak!")

# Ažuriranje prikaza zadataka
def update_task_listbox():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        task_str = task["task"]
        if task["completed"]:
            task_str += " (Završeno)"
        tasks_listbox.insert(tk.END, task_str)

# Inicijalizacija aplikacije
root = tk.Tk()
root.title("To-Do Lista")

# Lista zadataka
tasks = load_tasks()

# Unos novog zadatka
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Gumbi za rad s zadacima
add_task_button = tk.Button(root, text="Dodaj zadatak", command=add_task)
add_task_button.pack(pady=5)

complete_task_button = tk.Button(root, text="Označi kao dovršeno", command=complete_task)
complete_task_button.pack(pady=5)

delete_task_button = tk.Button(root, text="Obriši zadatak", command=delete_task)
delete_task_button.pack(pady=5)

# Prikaz zadataka
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

# Popunjava listbox s učitanim zadacima
update_task_listbox()

# Pokretanje glavne petlje aplikacije
root.mainloop()
