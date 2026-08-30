# 🚗 Système Anti-Somnolence Edge AI / Edge AI Anti-Drowsiness System

*🇫🇷 Version française ci-dessous | 🇬🇧 English version below*

---

## 🇫🇷 Français

### Description
Ce projet d'Intelligence Artificielle Embarquée (Edge AI) utilise la vision par ordinateur pour détecter la somnolence en temps réel. Si l'utilisateur ferme les yeux pendant plus de 2 secondes, un script Python envoie un signal à un microcontrôleur Arduino pour déclencher une alarme physique (Buzzer + LED).

### 1. Installation Matérielle (Câblage Arduino)
**Composants requis (Kit type Miuzei) :** Arduino Uno, 1x LED, 1x Buzzer passif, 1x Résistance (220 ohms), Breadboard, Câbles de connexion.

**Branchements sur la Breadboard :**
1. **GND (Terre) :** Reliez une broche `GND` de l'Arduino à la longue ligne bleue (`-`) de la breadboard. Cela servira d'évacuation commune.
2. **La LED :**
   - Branchez la patte longue (Anode, `+`) sur la **Pin 9** de l'Arduino.
   - Branchez la patte courte (Cathode, `-`) à une résistance, puis reliez cette résistance à la ligne bleue (`-`) de la breadboard.
3. **Le Buzzer (Passif) :**
   - Branchez la broche `+` du buzzer sur la **Pin 8** de l'Arduino.
   - Branchez l'autre broche directement sur la ligne bleue (`-`) de la breadboard.

### 2. Prérequis Logiciels
Avant de coder, assurez-vous d'avoir installé les logiciels suivants :
- **[Python](https://www.python.org/downloads/)** : Le langage principal pour l'IA (cochez bien "Add Python to PATH" lors de l'installation).
- **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)** : L'éditeur de code pour écrire et lancer le script Python.
- **[Arduino IDE](https://www.arduino.cc/en/software)** : Le logiciel pour téléverser le code C dans la carte Arduino.

### 3. Installation des dépendances (Terminal)
Dans VS Code, ouvrez un nouveau terminal (`Terminal > Nouveau terminal`) et tapez la commande suivante pour installer les bibliothèques d'Intelligence Artificielle et de communication :

pip install opencv-python mediapipe pyserial


# Edge AI Anti-Drowsiness System

###  Description
This Edge AI project uses computer vision to detect drowsiness in real-time. If the user closes their eyes for more than 2 seconds, a Python script sends a signal to an Arduino microcontroller to trigger a physical hardware alarm (Buzzer + LED).

###  1. Hardware Setup (Arduino Wiring)
**Required components (Miuzei kit or standard):** Arduino Uno, 1x LED, 1x Passive Buzzer, 1x Resistor (220 ohms), Breadboard, Jumper wires.

**Breadboard Connections:**
1. **GND (Ground):** Connect a `GND` pin from the Arduino to the long blue line (`-`) on the breadboard. This will serve as the common ground.
2. **The LED:**
   - Connect the long leg (Anode, `+`) to **Pin 9** on the Arduino.
   - Connect the short leg (Cathode, `-`) to a resistor, and connect the other end of the resistor to the blue line (`-`).
3. **The Buzzer (Passive):**
   - Connect the `+` pin of the buzzer to **Pin 8** on the Arduino.
   - Connect the other pin directly to the blue line (`-`).

###  2. Software Requirements
Before coding, make sure you have installed the following applications:
- **[Python](https://www.python.org/downloads/)**: The main programming language for the AI part (make sure to check "Add Python to PATH" during installation).
- **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)**: The code editor used to write and run the Python script.
- **[Arduino IDE](https://www.arduino.cc/en/software)**: The software required to upload the C code to the Arduino board.

###  3. Installing Dependencies (Terminal)
In VS Code, open a new terminal (`Terminal > New Terminal`) and run the following command to install the necessary computer vision and serial communication libraries:


```bash
pip install opencv-python mediapipe pyserial


