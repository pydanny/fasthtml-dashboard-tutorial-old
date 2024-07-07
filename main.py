from fasthtml.fastapp import * 

app = fast_app()

@app.get("/")
def home():
  return Titled("FastHTML", P("Let's do this!"))

@app.post("/")
def home():
  return Titled("POST", P("Let's do this!"))

@app.get("/{name}/{age}")  # Specify two variable names
def namer(name: str, age: int):  # Define two arguments named after vi
  return Titled(f"Hello {name}, age {age}")

run_uv()