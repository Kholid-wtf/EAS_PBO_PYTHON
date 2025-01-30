class Task:
    """Kelas untuk merepresentasikan sebuah tugas."""
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False  # Default status belum selesai

    def mark_completed(self):
        """Menandai tugas sebagai selesai."""
        self.completed = True

    def __str__(self):
        status = "Selesai" if self.completed else "Belum Selesai"
        return f"Tugas: {self.title}\nDeskripsi: {self.description}\nStatus: {status}\n"


class TaskManager:
    """Kelas untuk mengelola daftar tugas."""
    
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        """Menambahkan tugas baru."""
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Tugas '{title}' berhasil ditambahkan!")

    def show_tasks(self):
        """Menampilkan semua tugas dalam daftar."""
        if not self.tasks:
            print("Belum ada tugas yang ditambahkan.")
            return
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def mark_task_completed(self, task_index):
        """Menandai tugas sebagai selesai berdasarkan indeks."""
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].mark_completed()
            print(f"Tugas '{self.tasks[task_index - 1].title}' telah selesai!")
        else:
            print("Indeks tugas tidak valid!")

    def remove_task(self, task_index):
        """Menghapus tugas dari daftar berdasarkan indeks."""
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Tugas '{removed_task.title}' telah dihapus!")
        else:
            print("Indeks tugas tidak valid!")


def main():
    """Fungsi utama untuk menjalankan program."""
    manager = TaskManager()

    while True:
        print("\n=== Aplikasi Manajemen Tugas ===")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")
        
        choice = input("Pilih menu (1-5): ")

        if choice == "1":
            title = input("Masukkan judul tugas: ")
            description = input("Masukkan deskripsi tugas: ")
            manager.add_task(title, description)

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            manager.show_tasks()
            try:
                task_index = int(input("Masukkan nomor tugas yang selesai: "))
                manager.mark_task_completed(task_index)
            except ValueError:
                print("Masukkan angka yang valid!")

        elif choice == "4":
            manager.show_tasks()
            try:
                task_index = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                manager.remove_task(task_index)
            except ValueError:
                print("Masukkan angka yang valid!")

        elif choice == "5":
            print("Keluar dari aplikasi...")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi!")


if __name__ == "__main__":
    main()
