import tkinter
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random as rd
import dictionaries


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r", encoding="utf-8") as f:
        text_edit.insert(tk.END, f.read())
    window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not filepath:
        return
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text_edit.get("1.0", tk.END))
    window.title(f"Open File: {filepath}")


def insert_face(text_edit):
    random_key, random_value = rd.choice(list(dictionaries.faces_dict.items()))
    text_edit.insert(tk.INSERT, random_value)


def insert_animal(text_edit):
    random_key, random_value = rd.choice(list(dictionaries.animals_dict.items()))
    text_edit.insert(tk.INSERT, random_value)


def insert_object(text_edit):
    random_key, random_value = rd.choice(list(dictionaries.objects_dict.items()))
    text_edit.insert(tk.INSERT, random_value)


def insert_food(text_edit):
    random_key, random_value = rd.choice(list(dictionaries.food_dict.items()))
    text_edit.insert(tk.INSERT, random_value)


def insert_clothes(text_edit):
    random_key, random_value = rd.choice(list(dictionaries.clothes_dict.items()))
    text_edit.insert(tk.INSERT, random_value)


def main():
    window = tk.Tk()
    window.title("Alex's Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font=("Century", 25), bg="white", fg="black", wrap=tk.WORD)
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit))
    insert_button_face = tk.Button(frame, text="😀", command=lambda: insert_face(text_edit))
    insert_button_animals = tk.Button(frame, text="🐶", command=lambda: insert_animal(text_edit))
    insert_button_objects = tk.Button(frame, text="🔑", command=lambda: insert_object(text_edit))
    insert_button_food = tk.Button(frame, text="🍣", command=lambda: insert_food(text_edit))
    insert_button_clothes = tk.Button(frame, text="👗", command=lambda: insert_clothes(text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    insert_button_face.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    insert_button_animals.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    insert_button_objects.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
    insert_button_food.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
    insert_button_clothes.grid(row=6, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")
    frame.grid(row=0, column=0, sticky="ns")
    scrollb = tkinter.Scrollbar(window, command=text_edit.yview)
    scrollb.grid(row=0, column=1, sticky='nse')
    text_edit['yscrollcommand'] = scrollb.set
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.bind("<Control-e>", lambda x: insert_face(text_edit))
    window.bind("<Control-a>", lambda x: insert_animal(text_edit))
    window.bind("<Control-o>", lambda x: insert_object(text_edit))
    window.bind("<Control-f>", lambda x: insert_food(text_edit))
    window.bind("<Control-c>", lambda x: insert_clothes(text_edit))
    window.mainloop()


main()
