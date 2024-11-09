import os
import customtkinter
from os import path
import base64
import random
os.system("mkdir saves")
os.system("python -m venv env")

if not path.exists("package.txt"):
    
    os.system("sudo apt-get install sshpass")
    check = open("package.txt", "w+")
    check.close
    root = customtkinter.CTk()
    def mode():
        mode.configure(text="On")
    def run_saves():
        print(f"Connecting to {user_get}'s machine at {ip_get}...")
        os.system(f"sshpass -p {pass_get} ssh {user_get}@{ip_get}")
        print("\nIt's work !")
    def run():
        user_var = user.get()
        ip_var = ip.get()
        port_var = port.get()
        pass_var = password.get()
        
        
        print(f"Connecting to {user_var}'s machine at {ip_var}...")
        os.system(f"sshpass -p {pass_var} ssh {user_var}@{ip_var}")
        print("\nIt's work !")
        
    root.title("sshLite v1.0.0")
    root.minsize(300, 400)
    root.maxsize(300, 400)
    if path.exists("saves/ip.txt"):
        pass_r = open("saves/pass.txt", "r")
        pass_get = pass_r.read()
        ip_r = open("saves/ip.txt", "r")
        ip_get = ip_r.read()
        user_r = open("saves/user.txt", "r")
        user_get = user_r.read()
        saves_button = customtkinter.CTkButton(master=root, text=f"{user_get}@{ip_get}", command=run_saves)
        saves_button.pack(padx=60, pady=10)
    ip = customtkinter.CTkEntry(master=root, placeholder_text="127.0.0.1")
    ip.pack(padx=20, pady=10)
    user = customtkinter.CTkEntry(master=root, placeholder_text="root")
    user.pack(padx=30, pady=10)
    port = customtkinter.CTkEntry(master=root, placeholder_text="22")
    port.pack(padx=40, pady=10)
    password = customtkinter.CTkEntry(master=root, placeholder_text="123", show="*")
    password.pack(padx=45, pady=10)

    encode_label = customtkinter.CTkLabel(master=root, text="Encode Mode")
    encode_label.pack(padx=50, pady=10)

    mode = customtkinter.CTkSwitch(master=root, text="Off", command=mode)
    mode.pack(padx=30, pady=5)

    run_button = customtkinter.CTkButton(master=root, text="Connect", command=run)
    run_button.pack(padx=55, pady=10)


    root.mainloop()
else:
    root = customtkinter.CTk()
    def mode():
        mode.configure(text="On")
    def run_saves():
        print(f"Connecting to {user_get}'s machine at {ip_get}...")
        os.system(f"sshpass -p {pass_get} ssh {user_get}@{ip_get}")
        print("\nIt's work !")
    def run():
        user_var = user.get()
        ip_var = ip.get()
        port_var = port.get()
        pass_var = password.get()
        
        
        print(f"Connecting to {user_var}'s machine at {ip_var}...")
        os.system(f"sshpass -p {pass_var} ssh {user_var}@{ip_var}")
        print("\nIt's work !")
        pass_file = open("saves/pass.txt", "w+")
        pass_file.write(pass_var)
        
        ip_file = open("saves/ip.txt", "w+")
        ip_file.write(ip_var)
        
        user_file = open("saves/user.txt", "w+")
        user_file.write(user_var)
        
        
    root.title("sshLite v1.0.0")
    root.minsize(300, 400)
    root.maxsize(300, 400)
    if path.exists("saves/ip.txt"):
        pass_r = open("saves/pass.txt", "r")
        pass_get = pass_r.read()
        ip_r = open("saves/ip.txt", "r")
        ip_get = ip_r.read()
        user_r = open("saves/user.txt", "r")
        user_get = user_r.read()
        saves_button = customtkinter.CTkButton(master=root, text=f"{user_get}@{ip_get}", command=run_saves)
        saves_button.pack(padx=60, pady=10)
        
    ip = customtkinter.CTkEntry(master=root, placeholder_text="127.0.0.1")
    ip.pack(padx=20, pady=10)
    user = customtkinter.CTkEntry(master=root, placeholder_text="root")
    user.pack(padx=30, pady=10)
    port = customtkinter.CTkEntry(master=root, placeholder_text="22")
    port.pack(padx=40, pady=10)
    password = customtkinter.CTkEntry(master=root, placeholder_text="123", show="*")
    password.pack(padx=45, pady=10)

    encode_label = customtkinter.CTkLabel(master=root, text="Encode Mode")
    encode_label.pack(padx=50, pady=10)

    mode = customtkinter.CTkSwitch(master=root, text="Off", command=mode)
    mode.pack(padx=30, pady=5)

    run_button = customtkinter.CTkButton(master=root, text="Connect", command=run)
    run_button.pack(padx=55, pady=10)
    
    ssh_ver_label = customtkinter.CTkLabel(master=root, text="Work on OpenSSH_9.6p1")
    ssh_ver_label.pack(padx=50, pady=10)
    
    


    root.mainloop()