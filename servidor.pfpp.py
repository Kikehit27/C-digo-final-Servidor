import socket
import threading
import tkinter as tk
from tkinter import ttk, messagebox

class ArduinoServer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Servidor")

        self.host_var = tk.StringVar()
        self.port_var = tk.IntVar()
        self.host_var.set("192.168.66.143")  # Dirección IP predeterminada
        self.port_var.set(12345)  # Puerto predeterminado

        ttk.Label(self.root, text="Dirección IP del Servidor:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
        ttk.Entry(self.root, textvariable=self.host_var).grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(self.root, text="Puerto del Servidor:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
        ttk.Entry(self.root, textvariable=self.port_var).grid(row=1, column=1, padx=10, pady=10)
        ttk.Button(self.root, text="Iniciar Servidor", command=self.start_server).grid(row=2, column=0, columnspan=2, pady=10)

        self.server_socket = None
        self.client_socket = None

    def start_server(self):
        host = self.host_var.get()
        port = self.port_var.get()
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((host, port))
            self.server_socket.listen(1)
            messagebox.showinfo("Servidor Conectado", f"El servidor está escuchando en {host}:{port}")
            client_thread = threading.Thread(target=self.handle_client)
            client_thread.start()
        except Exception as e:
            messagebox.showerror("Error al Iniciar Servidor", f"No se pudo iniciar el servidor: {e}")

    def handle_client(self):
        try:
            while True:
                self.client_socket, client_address = self.server_socket.accept()
                messagebox.showinfo("Conexión Establecida", f"Conexión establecida con {client_address}")
        except KeyboardInterrupt:
            self.server_socket.close()
            messagebox.showinfo("Servidor Cerrado", "El servidor ha sido cerrado")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    server = ArduinoServer()
    server.run()
