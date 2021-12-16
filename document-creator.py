from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# The command we'll run at the terminal is:
# uvicorn document-creator:app --reload
# jinja-test = jinja-test.py
# app = app = FastAPI
app = FastAPI()

# We're defining a templates object that we can use later
templates = Jinja2Templates(directory="templates/")

# We have a static folder for CSS and stuff
app.mount("/static", StaticFiles(directory="static"), name="static")

# If you go to the server root you get a basic message
@app.get('/')
def hello_world():
    return 'hello world'


@app.get("/documentcreator")
def documentlist(request: Request):
    # Here we're going to call the list of documents and pass that through
    documents = ["giraffe", "badger", "third thing"]
    return templates.TemplateResponse('documentcreator.html.j2', context={'request': request, 'documents': documents})

# By submitting a POST request on this page using the submit button this gets called
# The form HTML has a field called "num" which we seem to be passing into this function
# "FastAPI understands the ellipsis in Form(...) to mean that the parameter is required. 
# If the ellipsis isn't available, I think None can be used as well but it wouldn't enforce the argument requirement."
@app.post("/documentcreator")
def documentgenerate(request: Request, num: int = Form(...)):
    # We provide the template with a result variable that contains whatever num is
    # And the function knows what num is because we just passed it in (so no scoping issues)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': num})

