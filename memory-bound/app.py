from flask import Flask

app = Flask(__name__)

@app.route("/<n>", methods=['GET'])
def index(n):
  fib = [0, 1]
  for _ in range(int(n) - 1):
    fib.append(fib[-1] + fib[-2])
    
  return fib

if __name__ == '__main__':
  app.run()