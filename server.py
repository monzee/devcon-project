import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
  return flask.render_template('index.html')

@app.route('/about')
def about():
  return flask.render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
  return flask.render_template('contact.html')

@app.route('/contact', methods=['POST'])
def after_contact():
  pass

if __name__ == '__main__':
  app.run(host='0', debug=True)
