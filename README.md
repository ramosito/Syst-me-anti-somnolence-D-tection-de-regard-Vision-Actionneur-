# Systeme Anti-Somnolence Edge AI / Edge AI Anti-Drowsiness System

Version francaise ci-dessous | English version below

---

## Francais

### Description
Ce projet d'Intelligence Artificielle Embarquee (Edge AI) utilise la vision par ordinateur pour detecter la somnolence en temps reel. Si l'utilisateur ferme les yeux pendant plus de 2 secondes, un script Python envoie un signal a un microcontroleur Arduino pour declencher une alarme physique (Buzzer + LED).

### 1. Installation Materielle (Cablage Arduino)
**Composants requis (Kit type Miuzei) :** Arduino Uno, 1x LED, 1x Buzzer passif, 1x Resistance (220 ohms), Breadboard, Cables de connexion.

**Branchements sur la Breadboard :**
1. **GND (Terre) :** Reliez une broche `GND` de l'Arduino a la longue ligne bleue (`-`) de la breadboard. Cela servira d'evacuation commune.
2. **La LED :**
   - Branchez la patte longue (Anode, `+`) sur la **Pin 9** de l'Arduino.
   - Branchez la patte courte (Cathode, `-`) a une resistance, puis reliez cette resistance a la ligne bleue (`-`) de la breadboard.
3. **Le Buzzer (Passif) :**
   - Branchez la broche `+` du buzzer sur la **Pin 8** de l'Arduino.
   - Branchez l'autre broche du buzzer directement sur la ligne bleue (`-`) de la breadboard.
   - Point important : si le buzzer ne sonne jamais, verifiez que son deuxieme fil est bien relie au GND. Un circuit non referme ne fait rien, meme si le code et le cablage principal sont corrects.

### 2. Prerequis Logiciels
Avant de coder, assurez-vous d'avoir installe les logiciels suivants :
- **[Python](https://www.python.org/downloads/)** (idealement 3.10, 3.11 ou 3.12) : le langage principal pour l'IA (cochez bien "Add Python to PATH" lors de l'installation).
- **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)** : l'editeur de code pour ecrire et lancer le script Python.
- **[Arduino IDE](https://www.arduino.cc/en/software)** : le logiciel pour televerser le code C dans la carte Arduino.

### 3. Installation des dependances (Terminal)
Dans VS Code, ouvrez un nouveau terminal (`Terminal > Nouveau terminal`) et tapez la commande suivante pour installer les bibliotheques d'Intelligence Artificielle et de communication :

```bash
pip install opencv-python mediapipe pyserial
```

Note : les versions recentes de mediapipe (1.0.x) ont retire l'ancienne API `mp.solutions`. Le script `anti_somnolence.py` de ce depot utilise la nouvelle API `mediapipe.tasks` (Face Landmarker) et telecharge automatiquement le modele necessaire (`face_landmarker.task`, environ 3 Mo) au premier lancement, sans manipulation supplementaire.

### 4. Utilisation
1. Televersez `anti_somnolence.ino` sur la carte Arduino via l'IDE Arduino (bouton "Televerser").
2. Fermez le Moniteur Serie de l'IDE Arduino s'il est ouvert : il verrouille le port COM et empeche Python de s'y connecter.
3. Verifiez le port COM utilise par votre Arduino dans le Gestionnaire de peripheriques Windows, et ajustez la ligne `arduino = serial.Serial('COM3', ...)` du script si besoin.
4. Lancez `anti_somnolence.py` depuis VS Code.
5. Calibrez le seuil de detection : la valeur EAR (taux d'ouverture des yeux) s'affiche en direct a l'ecran. Notez sa valeur yeux ouverts puis yeux fermes, et ajustez `EAR_THRESHOLD` dans le script si l'alarme ne se declenche pas ou se declenche trop souvent (valeur par defaut : 0.2).
6. Appuyez sur Echap pour quitter le programme.

### 5. Depannage rapide
| Symptome | Cause probable |
|---|---|
| `AttributeError: module 'mediapipe' has no attribute 'solutions'` | Version de mediapipe trop recente pour l'ancienne API. Utilisez la version du script basee sur `mediapipe.tasks` (deja le cas dans ce depot). |
| Le script tourne mais aucune fenetre camera n'apparait | Verifiez qu'aucune autre application (Teams, Zoom, app Camera) n'utilise deja la webcam, et que l'acces camera est autorise dans les parametres Windows. |
| Le message d'alarme ne s'affiche jamais | Le seuil `EAR_THRESHOLD` (0.2 par defaut) ne correspond pas a votre visage ou a la luminosite. Recalibrez avec la valeur EAR affichee a l'ecran. |
| Le terminal affiche "Arduino OK." mais rien ne s'allume ou ne sonne | Verifiez que le Moniteur Serie de l'IDE Arduino est ferme, que le sketch `.ino` a bien ete televerse (pas seulement verifie), et que le circuit est bien referme sur le GND. |
| Erreur au moment d'ouvrir le port COM | Le port COM a peut-etre change, ou un autre programme (IDE Arduino) l'utilise deja. |

---

## English

### Description
This Edge AI project uses computer vision to detect drowsiness in real-time. If the user closes their eyes for more than 2 seconds, a Python script sends a signal to an Arduino microcontroller to trigger a physical hardware alarm (Buzzer + LED).

### 1. Hardware Setup (Arduino Wiring)
**Required components (Miuzei kit or standard):** Arduino Uno, 1x LED, 1x Passive Buzzer, 1x Resistor (220 ohms), Breadboard, Jumper wires.

**Breadboard Connections:**
1. **GND (Ground):** Connect a `GND` pin from the Arduino to the long blue line (`-`) on the breadboard. This will serve as the common ground.
2. **The LED:**
   - Connect the long leg (Anode, `+`) to **Pin 9** on the Arduino.
   - Connect the short leg (Cathode, `-`) to a resistor, and connect the other end of the resistor to the blue line (`-`).
3. **The Buzzer (Passive):**
   - Connect the `+` pin of the buzzer to **Pin 8** on the Arduino.
   - Connect the other buzzer pin directly to the blue line (`-`).
   - Common pitfall: if the buzzer never sounds, double-check its second pin is actually wired to GND. An open circuit does nothing, even with correct code and wiring elsewhere.

### 2. Software Requirements
Before coding, make sure you have installed the following applications:
- **[Python](https://www.python.org/downloads/)** (ideally 3.10, 3.11 or 3.12): the main programming language for the AI part (make sure to check "Add Python to PATH" during installation).
- **[Visual Studio Code (VS Code)](https://code.visualstudio.com/)**: the code editor used to write and run the Python script.
- **[Arduino IDE](https://www.arduino.cc/en/software)**: the software required to upload the C code to the Arduino board.

### 3. Installing Dependencies (Terminal)
In VS Code, open a new terminal (`Terminal > New Terminal`) and run the following command to install the necessary computer vision and serial communication libraries:

```bash
pip install opencv-python mediapipe pyserial
```

Note: recent mediapipe releases (1.0.x) removed the legacy `mp.solutions` API. The `anti_somnolence.py` script in this repo uses the new `mediapipe.tasks` API (Face Landmarker) and automatically downloads the required model (`face_landmarker.task`, about 3 MB) on first run, no extra setup needed.

### 4. Usage
1. Upload `anti_somnolence.ino` to the Arduino board via the Arduino IDE ("Upload" button).
2. Close the Arduino IDE Serial Monitor if it is open: it locks the COM port and prevents Python from connecting.
3. Check which COM port your Arduino uses in Windows Device Manager, and update the `arduino = serial.Serial('COM3', ...)` line in the script if needed.
4. Run `anti_somnolence.py` from VS Code.
5. Calibrate the detection threshold: the live EAR (Eye Aspect Ratio) value is shown on screen. Note its value with eyes open and eyes closed, and adjust `EAR_THRESHOLD` in the script if the alarm never triggers or triggers too easily (default: 0.2).
6. Press Escape to quit the program.

### 5. Quick Troubleshooting
| Symptom | Likely cause |
|---|---|
| `AttributeError: module 'mediapipe' has no attribute 'solutions'` | mediapipe version too recent for the legacy API. Use the `mediapipe.tasks`-based script version (already the case in this repo). |
| Script runs but no camera window appears | Check that no other app (Teams, Zoom, Camera app) is already using the webcam, and that camera access is allowed in Windows settings. |
| Alarm message never prints | The `EAR_THRESHOLD` (default 0.2) does not match your face or lighting. Recalibrate using the on-screen EAR value. |
| Terminal shows "Arduino OK." but nothing lights up or beeps | Make sure the Arduino IDE Serial Monitor is closed, the `.ino` sketch was actually uploaded (not just verified), and the circuit is properly closed to GND. |
| Error opening the COM port | The COM port may have changed, or another program (Arduino IDE) is already using it. |
