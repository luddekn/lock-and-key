import customtkinter
import mysql.connector
import time

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def remove_right_objects():
    for widget in right_frame.winfo_children():
        widget.destroy()

def remove_sidebar_objects():
    for widget in login_frame.winfo_children():
        widget.destroy()

def copy_to_clipboard(password, button):
    root.clipboard_clear()
    root.clipboard_append(password)
    button.configure(text="Copied!")
    scrollable_frame.after(2000, lambda: button.configure(text="Copy Pass"))

def adding_entry():
    remove_right_objects()

    add_entry_label = customtkinter.CTkLabel(right_frame, text="Add New Entry")
    add_entry_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    username_label = customtkinter.CTkLabel(right_frame, text="Username:")
    username_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
    username_entry = customtkinter.CTkEntry(right_frame)
    username_entry.grid(row=1, column=0, padx=100, pady=10, sticky="ew")
    
    password_label = customtkinter.CTkLabel(right_frame, text="Password:")
    password_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
    password_entry = customtkinter.CTkEntry(right_frame, show="*")
    password_entry.grid(row=2, column=0, padx=100, pady=10, sticky="ew")

    cursor.execute("SELECT folder FROM passwords")
    rows = cursor.fetchall()
    folder_list = [row[0] for row in rows]
    unique_set = set(folder_list)
    unique_list = list(unique_set)
    if "None" in unique_list:
        unique_list.remove("None")
    else:
        pass

    folder_label = customtkinter.CTkLabel(right_frame, text="Folder:")
    folder_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
    folder_entry = customtkinter.CTkEntry(right_frame)
    folder_entry.grid(row=3, column=0, padx=100, pady=10, sticky="ew")
    folder_menu = customtkinter.CTkOptionMenu(right_frame, values=["None"]+unique_list)
    folder_menu.grid(row=3, column=1, padx=0, pady=10)

    def add_database_entry():
        try:
            username = username_entry.get()
            password = password_entry.get()
            folder = folder_entry.get()
            folder_select = folder_menu.get()

            if len(username) > 0 :
                if len(password) > 0:
                    if len(folder) > 0:
                        cursor.execute(f"INSERT INTO passwords (username, password, folder) VALUES ('{username}','{password}','{folder}');")
                        connection.commit()
                        message_label.configure(text=f"New entry for '{username}' added!")
                        right_frame.after(2000, lambda: message_label.configure(text=""))
                    else:
                        cursor.execute(f"INSERT INTO passwords (username, password, folder) VALUES ('{username}','{password}','{folder_select}');")
                        connection.commit()
                        message_label.configure(text=f"New entry for '{username}' added!")
                        right_frame.after(2000, lambda: message_label.configure(text=""))
                else:
                    message_label.configure(text=f"Password cannot be empty.")
                    right_frame.after(2000, lambda: message_label.configure(text=""))
            else:
                message_label.configure(text=f"Username cannot be empty.")
                right_frame.after(2000, lambda: message_label.configure(text=""))
        except mysql.connector.Error:
            message_label.configure(text="Failed to add new entry!")
            right_frame.after(2000, lambda: message_label.configure(text=""))
    
    add_button = customtkinter.CTkButton(right_frame, text="Add Entry", command=add_database_entry)
    add_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

    message_label = customtkinter.CTkLabel(right_frame, text="")
    message_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

def updating_entry():
    remove_right_objects()

    update_entry_label = customtkinter.CTkLabel(right_frame, text="Update Entry")
    update_entry_label.grid(row=0, column=0, padx=20, pady=20)

def deleting_entry():
    remove_right_objects()

    delete_entry_label = customtkinter.CTkLabel(right_frame, text="Delete Entry")
    delete_entry_label.grid(row=0, column=0, padx=20, pady=20)

def listing_entries():
    remove_right_objects()
    global scrollable_frame

    scrollable_frame = customtkinter.CTkScrollableFrame(right_frame, width=550, height=290)
    scrollable_frame.grid(row=1, column=0, padx=(20, 0), pady=(10, 0), sticky="nsew")
    scrollable_frame.grid_columnconfigure(0, weight=1)

    list_entry_label = customtkinter.CTkLabel(right_frame, text="Listing Entries")
    list_entry_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

    cursor.execute("SELECT username, password, folder FROM passwords ORDER BY folder;")
    entries = cursor.fetchall()

    entry_id = 1
    for entry in entries:
        username_label = customtkinter.CTkLabel(scrollable_frame, text=f"{entry[0]}")
        username_label.grid(row=entry_id, column=0, padx=0, pady=5, sticky="w")
        
        copy_button = customtkinter.CTkButton(scrollable_frame, text="Copy Pass")
        copy_button.grid(row=entry_id, column=1, padx=5, pady=5)
        copy_button.configure(command=lambda p=entry[1], b=copy_button: copy_to_clipboard(p, b))

        folder_label = customtkinter.CTkLabel(scrollable_frame, text=f"{entry[2]}")
        folder_label.grid(row=entry_id, column=2, padx=20, pady=5, sticky="w")
        entry_id += 1

def exit_application():
    cursor.close()
    connection.close()
    time.sleep(2)
    quit()

def main():
    remove_sidebar_objects()
    cursor.execute("CREATE DATABASE IF NOT EXISTS passwordmanager")
    cursor.execute("USE passwordmanager")
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100) NOT NULL, password VARCHAR(255) NOT NULL, folder VARCHAR(50) DEFAULT 'None')")
    connection.commit()

    global right_frame, sidebar_frame
    root.geometry(f"{850}x{400}")
    root.title("Password Manager V1.0")

    sidebar_frame = customtkinter.CTkFrame(root, width=300, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
    sidebar_frame.grid_rowconfigure(6, weight=1)

    label = customtkinter.CTkLabel(sidebar_frame, text="Password Manager", font=customtkinter.CTkFont(size=20, weight="bold"))
    label.grid(row=0, column=0, padx=20, pady=(20, 10))

    button_adding_entry = customtkinter.CTkButton(sidebar_frame, text="Add", command=adding_entry)
    button_adding_entry.grid(row=1, column=0, padx=20, pady=10)

    button_updating_entry = customtkinter.CTkButton(sidebar_frame, text="Update", command=updating_entry)
    button_updating_entry.grid(row=2, column=0, padx=20, pady=10)

    button_deleting_entry = customtkinter.CTkButton(sidebar_frame, text="Delete", command=deleting_entry)
    button_deleting_entry.grid(row=3, column=0, padx=20, pady=10)

    button_exit_application = customtkinter.CTkButton(sidebar_frame, text="List Entries", command=listing_entries)
    button_exit_application.grid(row=4, column=0, padx=20, pady=10)

    button_exit_application = customtkinter.CTkButton(sidebar_frame, text="Exit", command=exit_application)
    button_exit_application.grid(row=5, column=0, padx=20, pady=10)

    right_frame = customtkinter.CTkFrame(root)
    right_frame.grid(row=0, column=1, rowspan=5, sticky="nsew")
    root.mainloop()

def login():
    global root, login_frame, message_label
    root = customtkinter.CTk()
    root.geometry(f"{180}x{220}")
    root.title("Login")
    root.resizable(False, False)

    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure((2, 3), weight=0)
    root.grid_rowconfigure((0, 1, 2), weight=1)

    login_frame = customtkinter.CTkFrame(root)
    login_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
    login_frame.grid_rowconfigure(6, weight=1)

    label = customtkinter.CTkLabel(login_frame, text="MySQL Login", font=customtkinter.CTkFont(size=20, weight="bold"))
    label.grid(row=0, column=0, padx=20, pady=(10,10), sticky="w")

    username_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Username")
    username_entry.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

    password_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Password", show="*")
    password_entry.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

    def authentication():
        global connection, cursor
        try:
            username = username_entry.get()
            password = password_entry.get()
            connection = mysql.connector.connect(user = username, password = password, host = '192.168.0.141')
            cursor = connection.cursor()
            main()
        except mysql.connector.Error:
            message_label.configure(text="Login failed.")
            login_frame.after(2000, lambda: message_label.configure(text=""))

    button_exit_application = customtkinter.CTkButton(login_frame, text="Login", command=authentication)
    button_exit_application.grid(row=3, column=0, padx=20, pady=(10,5), sticky="w")

    message_label = customtkinter.CTkLabel(login_frame, text="")
    message_label.grid(row=4, column=0, padx=20, pady=0, sticky="w")

    root.mainloop()

login()