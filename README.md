# Mercadonamarket
Documentation technique pour l’application Mercadona  
1. Introduction  
Objectif de la documentation : La présente documentation vise à fournir une ressource complète 
et accessible destinée aux membres de l'équipe de développement, aux futurs contributeurs, ainsi 
qu'à toute personne impliquée dans la maintenance ou la compréhension de notre application Mer
cadona. Elle a pour objectif de faciliter le processus de développement, de favoriser la collabora
tion efficace, et d'assurer une gestion transparente du projet.  
Contexte du projet : Notre application e-commerce Django représente une plateforme robuste 
conçue pour répondre aux besoins spécifiques du commerce en ligne. Elle offre des fonctionnalités 
avancées telles que la gestion des produits, des utilisateurs, des commandes, et intègre des com
posants de sécurité robustes. L'importance de cette application réside dans sa capacité à fournir 
une expérience utilisateur optimale tout en permettant une gestion efficace des opérations com
merciales en ligne. Cette documentation servira de guide essentiel pour comprendre l'architecture, 
le développement, et la maintenance de cette application cruciale pour notre entreprise.   
2. Installation  
Prérequis : Avant de procéder à l'installation de notre application Django, assurez-vous de dispo
ser des éléments suivants :  
• Python : Version 3.11.5  
• Gestionnaire de paquets Python (pip) : Assurez-vous qu'il est installé et à jour.  
• Environnement virtuel : Recommandé pour isoler les dépendances du projet.  
Guide d'installation : Suivez attentivement ces étapes pour installer et configurer l'application 
sur votre environnement local :  
• Clonez le référentiel :  
git 
cd 
clone 
https://github.com/Fadddddd/Mercadonamarket.git 
votre-projet  
• Créez un environnement virtuel :  
python 
.\venv\Scripts\activate  -m 
• Activez l'environnement virtuel :  
o Sur Windows :  
o Sur Linux/MacOs :  
source venv/bin/activate  
• Installez les dépendances Python :  
• pip install -r requirements.txt  
Appliquez les migrations :  
venv 
venv  
python 
manage.py 
migrate  
python 
python 
• Créez un super utilisateur :  
manage.py 
• Lancez le serveur de développement :  
manage.py 
createsuperuser  
runserver  
• Accédez à l'application dans votre navigateur : http://localhost:8000/  
Cette séquence d’installation garantit une configuration correcte de l’application sur votre système 
local.  
3. Architecture  
• Modèles de données : Notre application repose sur une architecture de base de 
données bien définie, conçue pour stocker et gérer efficacement les informations es
sentielles. Voici le schéma de notre base de données, accompagné d'explications pour 
chaque modèle :  
• Modèle Produit (Product) :  
o Champs clés : libelle, description, price, image, category  
o Explication : Ce modèle représente les produits disponibles dans notre ca
talogue, enregistrant des détails tels que le libelle, le prix et une description 
détaillée, la catégorie auxquels ils appartiennent ainsi qu’une image.  
• Modèle Catégorie (Category) :  
o Champs clés : libelle  
o Explication : Ce modèle représente le libelle des catégories auxquelles les 
produits peuvent être associés, facilitant l'organisation et la navigation dans le 
catalogue.  
• Modèle Promotion (Product) :  
o Champs clés : product, start date, end date, discount percentage  
o Explication : Ce modèle permet d’appliquer des promotions sur les produits 
de notre application en se reposant sur une date de début et de fin ainsi que le 
pourcentage de la promotion.  
Structure du projet : Notre projet Django est organisé de manière à favoriser la lisibilité, la main
tenance et l'extensibilité. Voici une vue d'ensemble des principaux dossiers et de leurs fonctions :  
• /projectmercadona : Racine du projet Django.  
o /merchandise : Dossier principal de l'application Django.  
▪ /migrations: Contient les fichiers de migration de la base de don
nées.  
▪ /static: Emplacement des fichiers statiques tels que les feuilles de 
style, les images, etc.  
▪ /templates: Stocke les modèles HTML utilisés par l'application.  
▪ /views: Contient les fichiers de vue Django pour gérer les requêtes 
HTTP.  
o /manage.py : Script de gestion Django pour les tâches courantes.    
4. Configuration  
Paramètres Django : Dans cette section, nous allons explorer les paramètres clés présents dans 
le fichier de configuration Django (settings.py). Ces paramètres jouent un rôle crucial dans le 
comportement global de l'application. Voici une liste de certains paramètres essentiels avec leurs 
descriptions :  
• DEBUG :  
o Description : Ce paramètre contrôle le mode de débugage de l'application. 
En production, assurez-vous de le désactiver en le fixant à False pour des rai
sons de sécurité.  
• DATABASES :  
o Description : Ce paramètre spécifie les détails de la configuration de la base 
de données, tels que le moteur de base de données, le nom d'utilisateur, le mot 
de passe, etc. (informations sensibles qu’il ne faudra divulguer sous aucun pré
texte pour des raisons de sécurité)  
• STATIC_URL et STATIC_ROOT :  
o Description : Ces paramètres définissent l'URL et le répertoire racine pour 
les fichiers statiques (CSS, images, JavaScript) utilisés dans l'application.  
• MEDIA_URL et MEDIA_ROOT :  
o Description : Ces paramètres déterminent l'URL et le répertoire racine pour 
les fichiers média générés par les utilisateurs, tels que les téléchargements 
d'images.  
• INSTALLED_APPS :  
o Description : Liste des applications installées dans le projet. Ajoutez de 
nouvelles applications ici pour les intégrer à votre projet Django.  
• SECRET_KEY :  
o Description : Clé secrète utilisée pour sécuriser divers aspects de l'applica
tion, notamment les mots de passe liés à la base de données.  
Variables d'environnement : Dans le cas où votre application utilise des variables d'environne
ment, il est important de les configurer correctement. Les variables d'environnement peuvent être 
utilisées pour stocker des informations sensibles telles que les clés secrètes, les informations de 
connexion à la base de données, etc.  
Pour configurer les variables d'environnement, suivez ces étapes générales :  
• Créez un fichier .env à la racine du projet :  
SECRET_KEY=mysecretkey  
DEBUG=True  
DATABASE_URL=postgres://user:password@localhost/dbname  
• Utilisez python-decouple pour charger les variables d'environnement :  
from decouple import config  
SECRET_KEY = config('SECRET_KEY')  
DEBUG = config ('DEBUG', default=False)  
DATABASE_URL = config('DATABASE_URL')  
Assurez-vous de ne pas inclure le fichier .env dans votre référentiel Git pour éviter de divulguer 
des informations sensibles stockées dans ce fichier.  
5. Développement  
Flux de travail de développement : Notre cycle de vie de développement suit un processus bien 
défini, de la modification du code à son déploiement. Voici une vue d'ensemble des étapes clés :  
• Planification : Identifiez les fonctionnalités à développer et définissez des tâches 
spécifiques. Utilisez des outils de suivi de projet tels que Trello.  
• Tests unitaires : Écrivez des tests unitaires pour chaque fonctionnalité ou correc
tion de bug afin d'assurer la stabilité du code.  
• Déploiement : Une fois que le code a été révisé et approuvé, déployez-le sur l'en
vironnement de production.   
• Surveillance et maintenance : Surveillez les performances de l'application en pro
duction. Réagissez rapidement aux problèmes et appliquez les correctifs nécessaires. 
Documentez les changements effectués.  
En suivant ce flux de travail de développement, nous visons à assurer la qualité du code et des 
déploiements fiables. N'hésitez pas à vous référer à cette documentation pour comprendre les 
étapes spécifiques à suivre lors du développement de nouvelles fonctionnalités ou de correctifs.  
6. Fonctionnalités principales  
Description des fonctionnalités :  
• Gestion des Produits :  
o Description : Permet a l’administrateur (et aux utilisateurs que l’adminis
trateur aura autorisées) d'ajouter, modifier, supprimer et afficher des produits 
dans le catalogue.  
o Fonctionnalités : Ajout d'une nouvelle entrée de produit avec des détails 
tels que le libelle, la description, le prix et la catégorie.  
• Gestion des Catégories :  
o Description : Facilite l'organisation des produits en les associant à des ca
tégories spécifiques.  
o Fonctionnalités : Création, modification et suppression de catégories.  
• Tableau de Bord d'Administration :  
o Description : Offre un tableau de bord administratif pour la gestion centra
lisée des produits, des promotions et catégories.  
Exemples d'utilisation :  
• Ajout d'un Nouveau Produit :  
o Étapes :  
▪ Accédez à la section "Products" dans le tableau de bord en cliquant 
sur le crayon.  
▪ Cliquez sur "Add a new product".  
▪ Remplissez les détails du produit, tels que le libelle, la description, 
le prix, l’image.  
▪ Sélectionnez la catégorie appropriée.  
▪ Enregistrez le produit.  
• Gestion des Utilisateurs :  
o Étapes :  
▪ Accédez à la section "Gestion des Utilisateurs" dans le tableau de 
bord d'administration.  
▪ Créez un nouveau compte utilisateur en fournissant les informations 
requises.  
▪ Modifiez les informations du profil si nécessaire.  
7. Tests  
Guide de tests :  
Les tests jouent un rôle essentiel dans le développement d'une application fiable et robuste. Ils 
permettent de détecter les erreurs, de garantir la stabilité et de faciliter la maintenance. Voici un 
guide sur la manière d'exécuter les tests, les scénarios testés, et d'autres informations pertinentes :  
Exécution des Tests :  
• Assurez-vous d'avoir un environnement virtuel activé :  
source venv/bin/activate  
• Naviguez jusqu'au répertoire racine de votre projet Django :  
cd chemin/vers/votre/projet  
• Exécutez les tests à l'aide de la commande Django :  
python manage.py test  
Scénarios Testés :  
• Tests Unitaires :  
o Les tests unitaires sont écrits pour chaque fonction, méthode ou classe indi
viduelle afin de vérifier son comportement.  
• Tests d'Intégration :  
o Vérifient comment différentes parties de l'application interagissent les unes 
avec les autres.  
• Tests de Fonctionnalité :  
o S'assurent que les fonctionnalités principales de l'application fonctionnent 
correctement.  
Exemple d'Exécution des Tests :  
• Exécution de tous les tests :  
python manage.py test  
• Exécution des tests pour un module spécifique :  
python manage.py test nom_du_module  
• Exécution des tests avec affichage des sorties détaillées :  
python manage.py test -v 2  
Remarques supplémentaires :  
• Assurez-vous que les tests sont exécutés régulièrement, en particulier avant chaque 
déploiement en production.  
• Envisagez d'utiliser des outils tels que pytest pour des fonctionnalités supplémen
taires comme le paramétrage des tests.  
• Documentez tout test inhabituel ou complexe qui pourrait nécessiter une attention 
particulière lors de futures mises à jour ou modifications.  
8. Déploiement  
Guide de déploiement :  
Le déploiement d'une application en production est une étape critique qui nécessite une planifica
tion et une exécution soignées. Voici un guide détaillé sur la manière de déployer votre application 
Mercadona en production:  
• Configuration de l'environnement :  
o Assurez-vous que votre serveur de production dispose des mêmes dépen
dances que votre environnement local. Utilisez un environnement virtuel et ins
tallez les dépendances à l'aide du fichier requirements.txt :  
pip install -r requirements.txt  
• Configuration de la base de données :  
o Assurez-vous que la configuration de la base de données dans le fichier set
tings.py est adaptée à votre serveur de production. Appliquez les migrations 
pour créer les tables nécessaires :  
python manage.py migrate  
• Configuration des variables d'environnement :  
o Configurez les variables d'environnement nécessaires pour les paramètres 
sensibles tels que les clés secrètes, les informations de connexion à la base de 
données, etc. Utilisez un fichier .env pour garder ces informations privées.  
• Collecte des fichiers statiques et médias :  
o Collectez les fichiers statiques dans un répertoire accessible par le serveur 
web en utilisant la commande :  
python manage.py collectstatic  
• Assurez-vous que le serveur web a accès au répertoire des médias pour stocker les 
fichiers téléchargés par les utilisateurs.  
9. Maintenance  
Problèmes connus :  
• Problème : Dans le cas où certains utilisateurs signalent des erreurs lors de la con
nexion.  
o Solution temporaire : Vérifiez les journaux d'erreurs pour des informations 
détaillées. Assurez-vous que les paramètres d'authentification et de gestion des 
sessions sont configurés correctement.  
• Problème : Les images téléchargées par les utilisateurs ne s'affichent pas correcte
ment.  
o Solution temporaire : Vérifiez les autorisations sur le répertoire des médias. 
Assurez-vous que le serveur web peut accéder et servir ces fichiers.  
10. Ressources supplémentaires  
Liens utiles :  
• Documentation Django :  
o Django Documentation: La documentation officielle de Django offre des 
guides détaillés et des références pour le développement web avec Django : 
Django documentation | Django documentation | Django (djangoproject.com)  
• Tutoriels Django :  
o Django Girls Tutorial: Un tutoriel complet pour créer une application 
Django du début à la fin, adapté aux débutants : Introduction · HonKit (django
girls.org)  
• Sécurité Django :  
o Django Security: La section sécurité de la documentation Django offre des 
conseils pratiques pour sécuriser votre application : Security in Django | Django 
documentation | Django (djangoproject.com)  
• Déploiement :  
• Django Deployment: Deployment checklist | Django documentation | Django (djan
goproject.com)   
• Tests Django :  
o Django Testing Documentation: Testing in Django | Django documentation 
| Django (djangoproject.com)  
• Gestion des dépendances Python :  
o pip Documentation: pip documentation v23.3.2 (pypa.io) 
