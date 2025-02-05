import flask 

from controlers.eleves_controler import eleves_bp

app = flask.Flask(__name__)

#! Ici on déclare les controlers
#! ce sont eux qui vont interpréter ce que l'utilisateur a demandé, et qui vont renvoyer une réponse en conséquence.
app.register_blueprint(eleves_bp, url_prefix='/eleves')

@app.route('/', methods=['GET'])
def liste_eleves():
    # Traitement du template et transmission du HTML généré au client
    return flask.render_template('accueil.jinja')


