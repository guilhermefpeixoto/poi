from flask import Flask

app = Flask(__name__)

@app.route("/<n>", methods=['GET'])
def index(n):
  numbers = []
  
  for i in range(2, int(n)):
    is_prime = True
    for j in range(2, i):
      if i % j == 0:
        is_prime = False
        break
      
    if is_prime:
      numbers.append(i)
    
  return numbers

if __name__ == '__main__':
  app.run()