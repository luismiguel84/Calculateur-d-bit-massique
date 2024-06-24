import tkinter as tk
from tkinter import messagebox

def calculer_resultat():
    try:
        # Récupérer les valeurs saisies par l'utilisateur
        volume = float(entry1.get())
        pression_atm_mbar = float(entry2.get())
        temperature = float(entry3.get())
        humidite_relative = float(entry4.get())
        unite = unite_var.get()

        # Convertir le volume en mètres cubes par seconde selon l'unité sélectionnée
        if unite == "m3/h":
            volume_m3 = volume / 3600  # Convertir m3/h en m3/s
        elif unite == "l/h":
            volume_m3 = volume / 1000 / 3600  # Convertir l/h en m3/s
        elif unite == "l/min":
            volume_m3 = volume / 1000 / 60  # Convertir l/min en m3/s

        # Calculer le volume en normo mètres cubes selon la norme ISO 2533
        volume_nm3 = volume_m3 * (pression_atm_mbar / 1013.25) * (288.15 / (temperature + 273.15)) * ((1 + (40 * 0.00367)) / (1 + (0.00367 * humidite_relative)))

        # Reconvertir le résultat en volume selon l'unité sélectionnée
        if unite == "m3/h":
            volume_nm3_unite = volume_nm3 * 3600  # Convertir m3/s en m3/h
        elif unite == "l/h":
            volume_nm3_unite = volume_nm3 * 3600 * 1000  # Convertir m3/s en l/h
        elif unite == "l/min":
            volume_nm3_unite = volume_nm3 * 60 * 1000  # Convertir m3/s en l/min

        # Afficher le résultat dans le label de résultat
        resultat_label.config(text=f"Le volume en normo mètres cubes est : {volume_nm3_unite:.2f} {unite}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")

# Créer une fenêtre principale
root = tk.Tk()
root.title("Calculateur de Volume d'Air en Masse (ISO 2533)")
root.geometry("600x350")  # Redimensionner la fenêtre principale

# Créer des étiquettes et des champs de saisie pour les variables
label1 = tk.Label(root, text="Volume :", font=("Helvetica", 12))
label1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(root, font=("Helvetica", 12), width=10)
entry1.grid(row=0, column=1, padx=10, pady=5)

unite_var = tk.StringVar(root)
unite_var.set("m3/h")  # Valeur par défaut

unite_menu = tk.OptionMenu(root, unite_var, "m3/h", "l/h", "l/min")
unite_menu.grid(row=0, column=2, padx=10, pady=5)

label2 = tk.Label(root, text="Pression atmosphérique (mbar) :", font=("Helvetica", 12))
label2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(root, font=("Helvetica", 12), width=10)
entry2.grid(row=1, column=1, padx=10, pady=5)

label3 = tk.Label(root, text="Température (°C) :", font=("Helvetica", 12))
label3.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry3 = tk.Entry(root, font=("Helvetica", 12), width=10)
entry3.grid(row=2, column=1, padx=10, pady=5)

label4 = tk.Label(root, text="Humidité relative (%) :", font=("Helvetica", 12))
label4.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry4 = tk.Entry(root, font=("Helvetica", 12), width=10)
entry4.grid(row=3, column=1, padx=10, pady=5)

# Bouton pour calculer le résultat
calculate_button = tk.Button(root, text="Calculer", font=("Helvetica", 12), command=calculer_resultat)
calculate_button.grid(row=4, columnspan=3, pady=10)

# Label pour afficher le résultat
resultat_label = tk.Label(root, text="", font=("Helvetica", 12))
resultat_label.grid(row=5, columnspan=3, pady=10)

# Lancer la boucle principale
root.mainloop()
