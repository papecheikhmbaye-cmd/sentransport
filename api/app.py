import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Charger les donnees depuis le fichier JSON
with open("lignes_ddd.json", "r") as f:
    lignes = json.load(f)


@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>", "/arrets", "/stats", "/lignes/recherche?q="]
    })


@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)


@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next(
        (l for l in lignes if l["id"] == ligne_id),
        None
    )

    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvee"}), 404

    return jsonify(ligne)


@app.route("/arrets")
def get_arrets():
    arrets = set()

    for ligne in lignes:
        for arret in ligne["listeArrets"]:
            arrets.add(arret)

    return jsonify(list(arrets))


@app.route("/stats")
def get_stats():
    total_lignes = len(lignes)

    total_arrets = 0
    ligne_max_arrets = None
    max_arrets = 0

    for ligne in lignes:
        nb_arrets = len(ligne["listeArrets"])
        total_arrets += nb_arrets

        if nb_arrets > max_arrets:
            max_arrets = nb_arrets
            ligne_max_arrets = ligne["numero"]

    return jsonify({
        "total_lignes": total_lignes,
        "total_arrets": total_arrets,
        "ligne_max_arrets": ligne_max_arrets
    })


@app.route("/lignes/recherche")
def rechercher_lignes():
    q = request.args.get("q", "").lower()

    if not q:
        return jsonify({"erreur": "Parametre q manquant"}), 400

    resultats = [
        ligne for ligne in lignes
        if q in ligne["depart"].lower() or q in ligne["arrivee"].lower()
    ]

    return jsonify(resultats)


if __name__ == "__main__":
    app.run(debug=True, port=5000)