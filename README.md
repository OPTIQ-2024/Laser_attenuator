# Atténuateur de puissance laser variable
Ce projet vise à concevoir un atténuateur de puissance laser automatisé basé sur une interface graphique (GUI). Le système permet de contrôler l’atténuation d’un faisceau laser linéairement polarisé à 633 nm à l’aide d’une plaque demi-onde et d’un polariseur.

## Fonctionnement
L'atténuateur utilise :

1. Une plaque demi-onde montée sur un moteur rotatif contrôlé pour modifier la polarisation d’entrée.
2. Un polariseur fixe pour transmettre ou réfléchir le faisceau polarisé.
3. Une photodiode pour détecter une partie du faisceau réfléchi, connectée à un oscilloscope numérique.

## Ojectifs

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

  ### Contrôle moteur

  ### Oscilloscope
  
1- Téléchargement des bibliothèques Python pour le picoscope
  - pico-python
  - PicoDSK
2- Intégration de l'affichage des données dans le GUI

Utilisation de ctypes pour une bibliothèque C

