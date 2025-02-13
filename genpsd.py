import tkinter as tk
from tkinter import filedialog, messagebox
import random

class PseudoGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("s06821Dl3")
        self.root.iconbitmap("s06821Dl3.ico")
        
        # Fichier texte chargé
        self.file_path = None
        self.valid_characters = []

        # Bouton pour sélectionner un fichier
        self.upload_button = tk.Button(root, text="Parcourir", command=self.load_file)
        self.upload_button.pack(pady=10)

        # Zone d'affichage du pseudo généré
        self.output_label = tk.Label(root, text="Pseudo généré :", font=("Arial", 12))
        self.output_label.pack(pady=10)
        
        self.pseudo_display = tk.Entry(root, font=("Arial", 14), width=30, justify="center")
        self.pseudo_display.pack(pady=5)

        # Bouton pour générer un pseudo
        self.generate_button = tk.Button(root, text="Générer", command=self.generate_pseudo)
        self.generate_button.pack(pady=10)

    def load_file(self):
        """Charge un fichier texte et vérifie son contenu."""
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
        if file_path:
            self.file_path = file_path
            self.valid_characters = self.validate_file(file_path)
            if not self.valid_characters:
                messagebox.showerror("Erreur", "Le fichier n'est pas valide. Il doit contenir uniquement des lettres ou chiffres, un par ligne.")
                self.file_path = None

    def validate_file(self, file_path):
        """Vérifie que le fichier contient uniquement des lettres et chiffres, un par ligne."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                characters = [line.strip() for line in file.readlines() if line.strip()]
            
            # Vérifier si tous les caractères sont valides (lettres ou chiffres)
            valid_chars = [char for char in characters if char.isalnum() and len(char) == 1]
            return valid_chars if len(valid_chars) == len(characters) else []
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la lecture du fichier : {e}")
            return []

    def generate_pseudo(self):
        """Génère un pseudo aléatoire à partir du fichier chargé."""
        if not self.file_path:
            messagebox.showerror("Erreur", "Aucun fichier chargé !")
            return

        if not self.valid_characters:
            messagebox.showerror("Erreur", "Le fichier chargé n'est pas valide.")
            return

        # Mélange et applique des majuscules/minuscules aléatoirement
        random.shuffle(self.valid_characters)
        pseudo = "".join([char.upper() if random.choice([True, False]) else char.lower() for char in self.valid_characters])
        
        # Afficher le pseudo généré
        self.pseudo_display.delete(0, tk.END)
        self.pseudo_display.insert(0, pseudo)

# Lancer l'application Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = PseudoGeneratorApp(root)
    root.mainloop()