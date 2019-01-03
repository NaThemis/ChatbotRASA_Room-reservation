<h1 align="center"> Bookbot</h1> 
<div align="center">
  <strong>A Chatbot helping you to book rooms in your company</strong>
</div>

<div align="center">
  <!-- Subject -->
  <a href="https://nodejs.org/api/documentation.html#documentation_stability_index">
    <img src="https://img.shields.io/badge/subject-awesome-green.svg"
      alt="Subject" />
  </a>
</div>

Ici, la correction du chatbot basé sur rasa. Le principal problème que j'ai rencontré était dû à la migration.

Dans le wiki se trouve le cours/les conseils du 29 novembre 2018.

## Installation

 1. Cloner ce dépôt.
 2. Installer les requirements `pip install requirements.txt`
 3. Installer [rasa-nlu-trainer](https://github.com/RasaHQ/rasa-nlu-trainer), un outil pour aller plus vite dans la création d'examples.
 4. Entrainer le modèle avec train_init.py
 5. Entrainer le modèle avec train_online.py s'il y a besoin d'aéliorer la précision.
 6. Tester le chatbot avec dialogue_management_model.py.

En cas de galère [le tutoriel par Justina](https://vimeo.com/254777331) est très bien fait.
 
Bientôt : comment interragir avec Slack.

## Composition

Les principaux fichiers pour comprendre ce qu'il se passe sont : 

 - data/ :
   - data.json : exemples courants que je voudrais que mon chatbot apprenne
   - stories.md : anciennes conversations avec le chatbot qui aident à rendre le modèle plus précises.
 - config_spacy.json : les paramètres du modèles qui vont être utilisé : pipeline, path, data.
 - nlu.model : script qui crée le modèle d'entrainement
 - domain.yml : les scénarios de réponses, l'univers d'environnement du chatbot
 - actions.py : les opérations concrètes que l'on peut demander de faire et qui sont prévues par domain.py
 - train_init.py : script qui entraine le chatbot pour créer le modèles
 - train_online.py : script qui permet d'entrainer le modèle et mettre à jour stories.md pour améliorer le modèle.
 - models/
   - dialogue/
     Beaucoup de fichiers compliqués qui font le modèle :p 
 - dialogue_management_model.py: script qui permet de tester le chatbot
 - rasa_slack_conector.py : soon ...
 - run_app.py : soon ...

## A faire

Voir s'il y a des probèmes sur la partie Slack et les corriger.

## Un problème ? Une question ?

N'hésitez vraiment pas à [ouvrir un problème](https://github.com/antoinecomp/Chatbot_RASA_room_reservation/issues) ou à me contacter !
