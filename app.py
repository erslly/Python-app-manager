import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import subprocess
import threading
import time

# Daha fazla bağlantı ekleyebilirsiniz.
app_download_links = {
    "Discord": "https://discord.com/api/download?platform=win",
    "Google Chrome": "https://dl.google.com/chrome/install/latest/chrome_installer.exe",
    "VLC": "https://get.videolan.org/vlc/last/win64/vlc-3.0.16-win64.exe",
    "Visual Studio Code": "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user",
    "Zoom": "https://zoom.us/client/latest/ZoomInstaller.exe",
    "Slack": "https://slack.com/downloads/instructions/windows",
    "Skype": "https://go.skype.com/windowsdesktop",
    "Notepad++": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/latest/download/npp.8.4.1.Installer.exe",
    "7-Zip": "https://www.7-zip.org/download.html",
    "GIMP": "https://download.gimp.org/mirror/pub/gimp/v2.10/windows/gimp-2.10.32-setup.exe"
}

def install_application(app_name):
    try:
        url = app_download_links[app_name]
        response = requests.get(url)

        if response.status_code == 200:
            filename = f"{app_name}_Installer.exe"
            with open(filename, 'wb') as file:
                file.write(response.content)
            messagebox.showinfo("İndirildi", f"{app_name} yükleyicisi indirildi.")
            threading.Thread(target=start_installation, args=(filename,), daemon=True).start()
        else:
            messagebox.showwarning("Hata", "Uygulama indirilemedi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Yükleme sırasında bir hata oluştu: {e}")

def start_installation(filename):
    progress_bar.start(10)  
    time.sleep(1)  
    try:
        subprocess.run([filename], check=True)  
        messagebox.showinfo("Tamamlandı", f"{filename} başarıyla yüklendi.")
    except Exception as e:
        messagebox.showerror("Hata", f"Yükleme sırasında bir hata oluştu: {e}")
    finally:
        progress_bar.stop()  

def on_install():
    selected_app = app_var.get()
    install_application(selected_app)

# Tkinter GUI oluşturma
root = tk.Tk()
root.title("Uygulama Yükleyicisi")
root.geometry("400x400")
root.configure(bg="black")  

title_label = tk.Label(root, text="Uygulama Yükleyici", font=("Arial", 16, "bold"), bg="black", fg="white")
title_label.pack(pady=10)

app_var = tk.StringVar(value="Discord")  

apps = list(app_download_links.keys())
for app in apps:
    rb = tk.Radiobutton(root, text=app, variable=app_var, value=app, font=("Arial", 12), bg="black", fg="white", selectcolor="gray")
    rb.pack(anchor=tk.W)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
progress_bar.pack(pady=20)

install_button = tk.Button(root, text="Yükle", command=on_install, bg="#4CAF50", fg="white", font=("Arial", 12))
install_button.pack(pady=20)

root.mainloop()
