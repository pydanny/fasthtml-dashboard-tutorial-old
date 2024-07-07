# Quickstart

Eager to get started? This page gives a good introduction to FastHTML. 

## Installation

```bash
pip install python-fasthtml
```

## A Minimal Application

A minimal FastHTML application looks something like this:

``` python title="main.py" linenums="1"
from fasthtml.fastapp import * 

app = fast_app()

@app.get("/")
def home():
  return Titled("FastHTML", P("Let's do this!"))

run_uv()
```

What does that code do?

1. First we imported the FastHTML namespace on line 1. This is a carefully specified set of functions designed to optimize development. 

2. Next on line 3 we instantiate the FastHTML app with the `fast_app()` utility function. This provides a number of really useful defaults that we'll take advantage of later in the tutorial. 

3. Then on line 5 we use the `app.get()` decorator to tell FastTML what URL should trigger our view function if visited with an HTTP GET. By HTTP GET we mean "go to that location in our browser"

4. Line 6 is where we define our function name.

5. On line 7 we return several functions that describe all the HTML required to write a properly formed web page.

6. Finally, on line 9 the `run_uv()` utility configures and runs FastHTML using a library called `uvicorn`.


Run the code above by entering this command in the terminal:

```bash
python main.py
```

The terminal should send out some text that looks like this:

```
INFO:     Uvicorn running on http://0.0.0.0:5001 (Press CTRL+C to quit)
INFO:     Started reloader process [58058] using WatchFiles
INFO:     Started server process [58060]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

Confirm FastHTML is running by opening your web browser to this linl: [127.0.0.1:5001](http://127.0.0.1:5001). You should see something like the image below:

TODO add image

We did it! Now that we've got the program running, let's view the source of the HTML page. It should look something like this:

```html
<!doctype html>

<html>
  <head>
    <title>FastHTML</title>
    <script src="https://unpkg.com/htmx.org@next/dist/htmx.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/gnat/surreal/surreal.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/gnat/css-scope-inline/script.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css">
    <style>:root { --pico-font-size: 100%; }</style>
  </head>
  <body>
<main class="container">
  <h1>FastHTML</h1>
  <p>Let&#x27;s do this!!!</p>
</main>
  </body>
</html>
```

## Routing

Friendly URLs are intuitive and helpful to users, and easier to maintain for coders. Users are more likely to use your project if they can remember URLs without much effort. Fortunately, FastHTML uses the Python community's common pattern for specifying URLs.

!!! note "Pay attention to the highlighted lines"

    Try clicking the `+` icons for more information


``` python title="main.py" hl_lines="5 9"
from fasthtml.fastapp import * 

app = fast_app()

@app.get("/")  # (1)!
def home():
  return Titled("FastHTML", P("Let's do this!"))

@app.get("/hello")  # (2)!
def hello():
  return Titled("Hello, world!")

run_uv()
```

1. The "/" URL is the home of a project. This would be accessed at [127.0.0.1:5001](http://127.0.0.1:5001).
2. "/hello" URL will be found by the project if the user visits [127.0.0.1:5001/hello](http://127.0.0.1:5001/hello).

You can do more! Read on to learn what we can do to make parts of the URL dynamic.

## Variable in URLs

You can add variable sections to a URL by marking sections with `{variable_name}`. Your function then receives the `{variable_name}` as a keyword argument, but only if it is the correct type. Here's an example:

``` python title="main.py" hl_lines="9-11" linenums="1"
from fasthtml.fastapp import * 

app = fast_app()

@app.get("/")
def home():
  return Titled("FastHTML", P("Let's do this!"))

@app.get("/{name}/{age}")
def namer(name: str, age: int):
  return Titled(f"Hello {name.title()}, age {age}")

run_uv()
```

Try it out by going to this address: [127.0.0.1:5001/uma/5](http://127.0.0.1:5001/uma/5). You should get a page that says "Hello Uma, age 5".

### What's happening?

- On line 9 we specify two variable names, `name` and `age`
- On line 10 we define two function arguments named identically to the variables. You will note that we specify the Python types to be passed. 
- On line 11, we use these functions in our project.

### What happens if we enter incorrect data?

The [127.0.0.1:5001/uma/5](http://127.0.0.1:5001/uma/5) URL works because `5` is an integer. If we enter something that is not, such as [127.0.0.1:5001/uma/five](http://127.0.0.1:5001/uma/five), then FastHTML will return an error instead of a web page.

!!! note "FastHTML URL routing supports more complex types"

    The two examples we provide here use Python's built-in `str` and `int` types, but you can use your own types, including more complex ones such as those defined by libraries like `attrs`, `pydantic`, and even `sqlmodel`. 

## HTTP Methods

Most commonly URL routes for web apps are defined as HTTP GET methods. However, form submissions often are sent as HTTP POST. When dealing with more dynamic web page designs, also known as Single Page Apps (SPA for short), the need can arise for other methods such as HTTP PUT and HTTP DELETE. The way FastHTML handles this is by changing the decorator.

```python title="main.py" hl_lines="5-7 9-11" linenums="1"
from fasthtml.fastapp import * 

app = fast_app()

@app.get("/")
def home():
  return Titled("HTTP GET", P("Handle GET"))

@app.post("/")
def home():
  return Titled("HTTP POST", P("Handle POST"))

run_uv()
```

If you look at the hightlighted code, you'll see that the two view functions are named identically. The routing decorators allow for method overloading, something that isn't common in Python. This is really useful when building forms, as both the view (GET) and action (POST) views can be named the same for easy discovery. 

