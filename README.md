# bateau-de-thesee

projet individuel class/

# 🚢 Gestion de Bateau - Ship Management

## 📌 Description

Ce projet implémente un système de gestion de bateau en Python. Il permet d'ajouter, de remplacer et de modifier des pièces d'un navire tout en gardant un historique des modifications.

## 🛠️ Fonctionnalités

- Ajouter des pièces au bateau
- Remplacer une pièce existante
- Modifier le matériau d'une pièce
- Afficher l'état actuel du bateau
- Gérer un historique des modifications
- Gérer les bateaux de course avec une vitesse maximale

## 📂 Structure du Projet

- `Part` : Classe représentant une pièce avec un nom et un matériau.
- `Ship` : Classe de base représentant un bateau avec un dictionnaire privé de pièces.
- `Racingship` : Hérite de `Ship` et ajoute une gestion de vitesse et un historique des modifications.

## 🚀 Installation et Utilisation

### 1️⃣ Cloner le projet

```bash
 git clone https://github.com/ton-repo.git
 cd ton-repo
```

### 2️⃣ Exécuter le programme

```bash
 python main.py
```

## ✨ Exemples d'utilisation

### Ajouter une pièce :

```python
bateau.add_part(Part("Mât", "Bois"))
```

### Modifier le matériau d'une pièce :

```python
bateau.change_part("Mât", "Acier")
```

## 📜 Licence

Ce projet est sous licence MIT.

## 🤝 Contribution

Les contributions sont les bienvenues ! Forkez le projet et proposez vos améliorations.
