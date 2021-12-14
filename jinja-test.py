from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# The command we'll run at the terminal is:
# uvicorn jinja-test:app --reload
# jinja-test = jinja-test.py
# app = app = FastAPI
app = FastAPI()

# We're defining a templates object that we can use later
templates = Jinja2Templates(directory="templates/")

# We have a static folder for CSS and stuff
app.mount("/static", StaticFiles(directory="static"), name="static")

# If you go to the server root you get a basic message
@app.get('/')
def read_form():
    return 'hello world'

# Head over to 127.0.0.1/form and you'll GET the form below.
# I *think* request: Request passes that it's a GET type request
# Then again I'm still getting the hang of decorators so I could be wrong.
# Anyway it passes the result variable to the HTML template so when the user 
# opens it what they see initially is "Result: Type a number"
@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# By submitting a POST request on this page using the submit button this gets called
# The form HTML has a field called "num" which we seem to be passing into this function
# "FastAPI understands the ellipsis in Form(...) to mean that the parameter is required. 
# If the ellipsis isn't available, I think None can be used as well but it wouldn't enforce the argument requirement."
@app.post("/form")
def form_post(request: Request, num: int = Form(...)):
    # We provide the template with a result variable that contains whatever num is
    # And the function knows what num is because we just passed it in (so no scoping issues)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': num})

