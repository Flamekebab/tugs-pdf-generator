# A PDF tool for tUGS

This project started back in 2016 in PHP before shifting to Python and then grinding to a halt.
The reason was simple - ReportLab is a bit on the arcane side and it was too much to deal with.

Well now we're having another go!

The goal is to create a web-based tool that dynamically combines various PDFs to provide a campaign booklet for people.
Select what you want, add an introduction of your own choosing, hit the button and render it out, complete with table of contents.

Whether that's something we can actually achieve remains to be seen and might take a while but let's have a go!

As a reminder - setup a virtual environment:

```
python3 -m venv .
source bin/activate
```

Then install the requirements:

```
pip install -r requirements.txt
```

Additional reminder - to create an updated requirements.txt:

```
pip freeze > requirements.txt 
```

Useful reference sources:

- [ReportLab User Guide](https://www.reportlab.com/docs/reportlab-userguide.pdf)  
- [ReportLab Reference](https://www.reportlab.com/docs/reportlab-reference.pdf)