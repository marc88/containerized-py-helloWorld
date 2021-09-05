from flask import Flask

app = Flask(__name__)


@app.route('/<name>')
def helloWorld(name):
  return("Hello "+str(name))

@app.route('/test')
def test():
  return("Tested succesfully")

if __name__=='__main__':
  app.run(host='0.0.0.0',port=5050)