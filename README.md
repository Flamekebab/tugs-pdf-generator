# A PDF tool for tUGS

This project started back in 2016 in PHP before shifting to Python and then grinding to a halt.
The reason was simple - ReportLab is a bit on the arcane side and it was too much to deal with.

Well now we're having another go!

The goal is to create a web-based tool that dynamically combines various PDFs to provide a campaign booklet for people.
Select what you want, add an introduction of your own choosing, hit the button and render it out, complete with table of contents.

Whether that's something we can actually achieve remains to be seen and might take a while but let's have a go!

As a reminder - setup a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
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

# Vague Task List

## Document list compiler

There'll be a folder of PDFs, left and right versions (so that the page number ends up in the right place). 
Each document will need some sort of data kept on it.
Something like an XML file or JSON keeping track of its title, document type, author, licence, and anything else that could be useful.
Ideally that data should be built in such a way as to allow us to add additional data without breaking anything later.

Once each document has its data there should either be a manifest that's created and cached periodically or a way to generate an equivalent each time the PDF builder runs.

## Cover page generator

A tool to take text input and generate a single page (multi?) page PDF using the right fonts, in the right layout (ideally two column).

## Table of contents generator

A tool that takes the provided PDF choices and generates a table of contents to go after the cover page.

## Document combiner

A tool that combines the chosen documents, grabs the appropriate left or right version, adds page numbers, and then combines them with the cover page and table of contents PDFs.

## GUI for finished application

A web-based front-end that will provide the end user with a list of available documents to choose from as basic functionality.
Further down the line it should provide a few forms of simple text input to provide their own cover page and title for the booklet we're going to generate.

