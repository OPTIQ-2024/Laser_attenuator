# Atténuateur de puissance laser variable
Ce projet vise à concevoir un atténuateur de puissance laser automatisé basé sur une interface graphique (GUI). Le système permet de contrôler l’atténuation d’un faisceau laser linéairement polarisé à 633 nm à l’aide d’une plaque demi-onde et d’un polariseur.
## Fonctionnement
L'atténuateur utilise :
1. Une plaque demi-onde montée sur un moteur rotatif contrôlé pour modifier la polarisation d’entrée.
2. Un polariseur fixe pour transmettre ou réfléchir le faisceau polarisé.
3. Une photodiode pour détecter une partie du faisceau réfléchi, connectée à un oscilloscope numérique.
## Objectifs
1. Contrôler le moteur rotatif pour ajuster la polarisation.
2. Récupérer les données de l’oscilloscope pour visualiser la puissance du laser.
3. Automatiser ces tâches via une interface utilisateur graphique (GUI).
## Matériel
 
  ### Éléments opto-mécaniques
    -Plaque demi-onde (Thorlabs WPH05M-633)
    -Cube séparateur de faisceau polarisant (Thorlabs PBS251)
    -Lentille plano-convexe de 100 mm (Thorlabs LA1509)
    -Divers supports et bases (Thorlabs).
   
 ### Composants électroniques
   - Servomoteur : Dynamixel MX12
   - Alimentation : SMPS2
   - Contrôleur USB : Dynamixel U2D2
   - Photodiode biaisée : Thorlabs DET10A2
   - Oscilloscope numérique : Picoscope 2406B
## Procédure
  ### I-Contrôle moteur

   ### Étapes de configuration
### I-1. Configuration matérielle

   ### Connectez le moteur :
 1. Utilisez l'alimentation SMPS2 pour alimenter votre moteur Dynamixel.
 2. Connectez le contrôleur USB Dynamixel U2D2 à votre PC via un câble USB.
 3. Reliez le moteur au U2D2 à l'aide du connecteur TTL 3 broches.
    
   ### Vérifiez la vitesse de communication (baud rate) et l’ID :
 1. La vitesse par défaut pour le moteur MX12 est 1000000.
 2. S'assurer que l’ID du moteur est unique dans votre configuration.

 ### I-2. Installation logicielle
 1.	Installez Python : Téléchargez et installez Python depuis python.org.
 2.	Installez le package pypot  : Exécutez la commande suivante dans le terminal ou invite de commande : 	pip install pypot
 
 ### I-3. Tester la communication avec le moteur

 1. Mettre au point l'interface
 2.  Tester premièrement la communication du moteur avec le logiciel Dynamixel Wizard 2, pour certaines valeurs du PID , on etduie le comportement du goal position et present position, dans le but d'avoir une meilleure résolution.
 3. Intercoporer ensuite les valeurs de PID  trouvées correspondant à la meilleure résolution dans notre fichier main.py permettant de générant l'interface du moteur
 4. Ouvrir ensuite une communication avec le moteur.
 5. Scanner le moteur connecté (identification du périphérique COM6).
 6. Contrôler la position du moteur.

  ### II. Oscilloscope
  
1- Téléchargement des bibliothèques Python pour le picoscope
  - Aller [ici](https://github.com/colinoflynn/pico-python/blob/master/picoscope.py) et copier les codes error_codes.py, picobase.py et ps2000a.py
  - Aller [ici](https://www.picotech.com/downloads), choisir PicoScope2000 Series, Picoscope 2406B et télécharger la version recommandé
  - Installer PyQt5 et pyqtgraph

2- Configurer l'interface utilisateur (UI) 

3- Capturer les données de l'oscilloscope

4- Controler l'oscilloscope et afficher en temps réel les signaux
