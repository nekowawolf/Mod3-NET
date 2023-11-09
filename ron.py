import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Aplikasi GUI Python")

    # Buat label dan entry untuk nama mahasiswa
    label_nama_mahasiswa = tk.Label(root, text="Nama Mahasiswa:")
    label_nama_mahasiswa.grid(row=0, column=0)
    entry_nama_mahasiswa = tk.Entry(root)
    entry_nama_mahasiswa.grid(row=0, column=1)

    # Buat label dan entry untuk NPM
    label_npm = tk.Label(root, text="NPM:")
    label_npm.grid(row=1, column=0)
    entry_npm = tk.Entry(root)
    entry_npm.grid(row=1, column=1)

    # Buat label dan entry untuk kelas
    label_kelas = tk.Label(root, text="Kelas:")
    label_kelas.grid(row=2, column=0)
    entry_kelas = tk.Entry(root)
    entry_kelas.grid(row=2, column=1)

    # Buat tombol untuk menampilkan informasi mahasiswa
    button_tampilkan = tk.Button(root, text="Tampilkan", command=lambda: tampilkan_informasi_mahasiswa())
    button_tampilkan.grid(row=3, column=0)

    # Buat fungsi untuk menampilkan informasi mahasiswa
    def tampilkan_informasi_mahasiswa():
        nama_mahasiswa = entry_nama_mahasiswa.get()
        npm = entry_npm.get()
        kelas = entry_kelas.get()

        # Tampilkan informasi mahasiswa di terminal
        print(f"Nama mahasiswa: {nama_mahasiswa}")
        print(f"NPM: {npm}")
        print(f"Kelas: {kelas}")

    root.mainloop()

if __name__ == "__main__":
    main()
