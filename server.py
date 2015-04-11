import flask
import time

app = flask.Flask(__name__)
app.secret_key = 'super_secret'

MESSAGES = []

@app.route('/')
def home():
  return flask.render_template('index.html')

@app.route('/about')
def about():
  return flask.render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
  flash = flask.get_flashed_messages()
  if len(flash) > 0:
    messages = flash
  else:
    messages = None
  return flask.render_template('contact.html', messages=messages)

@app.route('/contact', methods=['POST'])
def after_contact():
  timestamp = time.strftime('%y-%b-%d %I:%M%p', time.localtime())
  name = flask.request.form.get('name')
  message = flask.request.form.get('message')
  MESSAGES.append((timestamp, name, message))
  flask.flash('Thank you for dropping by!')
  return flask.redirect(flask.url_for('contact'))

@app.route('/messages')
def messages():
  return flask.render_template('messages.html', xs=MESSAGES)

if __name__ == '__main__':
  app.run(host='0', debug=True)
