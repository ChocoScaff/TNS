import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Fonction pour lire les données à partir du port série
def lire_donnees_serial(port, baudrate=9600, timeout=1):
    ser = serial.Serial(port, baudrate, timeout=timeout)
    if ser.isOpen():
        print(f"Connexion établie sur le port {port}")
    return ser

# Fonction pour lire une ligne du port série et convertir en float
def lire_valeur_float(ser):
    try:
        ligne = ser.readline().decode('utf-8').strip()
        return float(ligne)
    except ValueError:
        return None  # Ignore si ce n'est pas un nombre

# Fonction pour créer des graphiques en temps réel
def afficher_graphique(ser, taille_fenetre=100):
    # File pour stocker les données en temps réel
    valeurs = deque([0] * taille_fenetre, maxlen=taille_fenetre)

    # Initialisation du graphique
    fig, ax = plt.subplots()
    ligne, = ax.plot(valeurs)
    ax.set_ylim(0, 1023)  # Modifier en fonction de l'échelle attendue de tes données

    # Fonction d'animation mise à jour à chaque nouvel échantillon
    def mise_a_jour_graphique(i):
        nouvelle_valeur = lire_valeur_float(ser)
        if nouvelle_valeur is not None:
            valeurs.append(nouvelle_valeur)
            ligne.set_ydata(valeurs)
        return ligne,

    # Animation du graphique
    ani = animation.FuncAnimation(fig, mise_a_jour_graphique, interval=100)

    plt.show()

# Point d'entrée du programme
if __name__ == "__main__":
    # Paramètres du port série
    port = 'COM4'  # Modifier selon ton port COM (sous Linux : '/dev/ttyUSB0')
    baudrate = 9600  # Assurez-vous que cela correspond à la configuration de votre appareil

    # Lire les données du port série
    ser = lire_donnees_serial(port, baudrate)

    # Afficher les données dans un graphique en temps réel
    try:
        afficher_graphique(ser)
    except KeyboardInterrupt:
        print("Interruption par l'utilisateur")
    finally:
        ser.close()
