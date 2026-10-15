import os
import shutil
import queue
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def default_downloads_folder():
    home = os.path.expanduser("~")
    downloads = os.path.join(home, "Downloads")
    return downloads if os.path.isdir(downloads) else home


def unique_destination(destination):
    if not os.path.exists(destination):
        return destination

    base, extension = os.path.splitext(destination)
    counter = 1
    while True:
        candidate = f"{base} ({counter}){extension}"
        if not os.path.exists(candidate):
            return candidate
        counter += 1


def organize_folder(folder, log):
    if not folder or not os.path.isdir(folder):
        log(f"Pasta inválida: {folder}")
        return 0

    moved = 0
    for entry in os.listdir(folder):
        source = os.path.join(folder, entry)
        if not os.path.isfile(source):
            continue

        extension = os.path.splitext(entry)[1][1:].lower() or "sem_extensao"
        target_folder = os.path.join(folder, extension)
        os.makedirs(target_folder, exist_ok=True)

        destination = unique_destination(os.path.join(target_folder, entry))
        try:
            shutil.move(source, destination)
            log(f"{entry}  ->  {extension}/")
            moved += 1
        except Exception as error:
            log(f"Erro ao mover {entry}: {error}")

    return moved


class DownSortApp:
    def __init__(self, root):
        self.root = root
        self.messages = queue.Queue()
        self.folder_var = tk.StringVar(value=default_downloads_folder())

        root.title("DownSort")
        root.geometry("560x420")
        root.minsize(460, 340)

        container = ttk.Frame(root, padding=16)
        container.pack(fill="both", expand=True)

        ttk.Label(
            container,
            text="Organizador de Downloads",
            font=("Segoe UI", 15, "bold"),
        ).pack(anchor="w")

        ttk.Label(
            container,
            text="Escolha a pasta e clique em Organizar. "
            "Os arquivos serão separados em subpastas por extensão.",
            wraplength=520,
            justify="left",
        ).pack(anchor="w", pady=(4, 12))

        row = ttk.Frame(container)
        row.pack(fill="x")
        self.entry = ttk.Entry(row, textvariable=self.folder_var)
        self.entry.pack(side="left", fill="x", expand=True)
        ttk.Button(row, text="Escolher pasta", command=self.choose_folder).pack(
            side="left", padx=(8, 0)
        )

        self.organize_button = ttk.Button(
            container, text="Organizar agora", command=self.start_organize
        )
        self.organize_button.pack(fill="x", pady=12)

        ttk.Label(container, text="Registro:").pack(anchor="w")
        log_frame = ttk.Frame(container)
        log_frame.pack(fill="both", expand=True, pady=(4, 0))
        self.log_widget = tk.Text(log_frame, height=10, wrap="none", state="disabled")
        scrollbar = ttk.Scrollbar(
            log_frame, orient="vertical", command=self.log_widget.yview
        )
        self.log_widget.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.log_widget.pack(side="left", fill="both", expand=True)

        self.root.after(100, self.flush_messages)

    def choose_folder(self):
        selected = filedialog.askdirectory(
            title="Escolha a pasta de downloads",
            initialdir=self.folder_var.get() or default_downloads_folder(),
        )
        if selected:
            self.folder_var.set(selected)
            self.log(f"Pasta selecionada: {selected}")

    def log(self, message):
        self.messages.put(message)

    def flush_messages(self):
        while not self.messages.empty():
            message = self.messages.get()
            self.log_widget.configure(state="normal")
            self.log_widget.insert("end", message + "\n")
            self.log_widget.see("end")
            self.log_widget.configure(state="disabled")
        self.root.after(100, self.flush_messages)

    def start_organize(self):
        folder = self.folder_var.get().strip()
        if not os.path.isdir(folder):
            messagebox.showerror("DownSort", "Selecione uma pasta válida.")
            return

        self.organize_button.configure(state="disabled")
        self.log(f"Organizando: {folder}")
        threading.Thread(
            target=self.run_organize, args=(folder,), daemon=True
        ).start()

    def run_organize(self, folder):
        moved = organize_folder(folder, self.log)
        self.log(f"Concluído. {moved} arquivo(s) organizado(s).")
        self.root.after(0, lambda: self.organize_button.configure(state="normal"))


def main():
    root = tk.Tk()
    DownSortApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
