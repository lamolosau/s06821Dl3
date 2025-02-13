### 📌 **README.md**  

```md
# 🎭 s06821Dl3 - Générateur de Pseudo Aléatoire  

🚀 **s06821Dl3** est une application Python avec une interface graphique (Tkinter) permettant de générer des pseudos uniques à partir d'un fichier texte contenant des caractères personnalisés.  

---

## 🛠️ Fonctionnalités  
✅ **Interface intuitive** avec upload de fichier texte 📂  
✅ **Vérification du fichier** (seuls les caractères valides sont pris en compte) ✅  
✅ **Génération aléatoire** en mélangeant les caractères avec majuscules/minuscules 🔀  
✅ **Icône personnalisée** pour l’application 🖼️  
✅ **Version `.exe` disponible** pour exécution sans Python  

---

## 📦 Installation et Exécution  

### **1️⃣ Cloner le projet**  
Si tu veux modifier ou tester le script Python :
```sh
git clone https://github.com/lamolosau/s06821Dl3.git
```

### **2️⃣ Créer un environnement Conda** *(recommandé)*
```sh
conda create --name pseudo_gen python=3.9
conda activate pseudo_gen
```

### **3️⃣ Installer les dépendances**
```sh
pip install tk
pip install pyinstaller
```

### **4️⃣ Exécuter l’application**  
```sh
python genpsd.py
```

---

## 📂 Utilisation  

1️⃣ **Lancer l’application**  
2️⃣ **Uploader un fichier texte** (`.txt`) contenant des caractères **un par ligne**  
3️⃣ **Cliquer sur "Générer"** pour afficher un pseudo aléatoire basé sur ton fichier  
4️⃣ **Réessayer autant de fois que nécessaire** (chaque clic génère un pseudo unique)  

📌 **Exemple de fichier `.txt` valide :**  
```
S
D
L
1
3
2
8
6
```

---

## 🎨 Personnalisation  

📌 **Modifier la longueur des pseudos générés :**  
Dans `generate_pseudo()`, limite la sortie :
```python
pseudo = pseudo[:10]  # Limite à 10 caractères
```

---
