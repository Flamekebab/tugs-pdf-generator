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

# Intended end result

The user visits a web page with a form (HTML). The form provides a list of available documents, split by category, with checkboxes for each one.
Additionally there's an option title and body text box for the document's front page. Similarly the option for a table of contents page.
Once the options are selected the server assembles a PDF and offers it for download.

# Components

## Document list compiler

There'll be a folder of PDFs, left and right versions (so that the page number ends up in the right place). 
Each document will need some sort of data kept on it for portability. This can be auto-generated for PDFs that have meta data but we cannot rely on that existing and so some way of manually inputting it seems like a good idea.

Either we have a manifest file for each PDF or we have a single central index. Ideally I want to avoid databases for the sake of ease of portability.

The code should check the timestamp on the central index and only recreate it if it's older than (time). No need to rescan a load of files every time the page loads.

JSON is probably the easiest way to handle this - each object keeping track of its title, document type, author, licence, page count, and anything else that could be useful.
The code that scans the data should be built in such a way as to allow us to add additional data without breaking anything later. Define some sensible defaults if the relevant data isn't found.

## Cover page generator/Table of contents generator

ReportLab to generate the two columns of text, the text flowing between the two. The title font is Ridgeline, the body text is Source Sans Pro. Both have suitable licences and are in the repo.

The page always starts on the right - i.e. the page number is in the bottom right corner. The page number should be in Ridgeline.
Let's limit it to a single page. If you've got more to say than that then create your own fork as it's enough of an edge case that it's overkill to build for. We'll figure out a character count that it maxes out at and implement that in the HTML form.

Once that's done create the ToC.

Take the input from the HTML form and check the page count in the manifest. Based on whether a cover page is included or not calculate on which page each document will start. Grab the title of each from the manifest and create the relevant text data.

Render it out in two columns using the code from the cover page generator. The page number could be either left or right, depending on whether a cover page is included or not.

## Document combiner

We now have between 0 and 2 PDFs to which we'll be using ReportLab to add page numbers to, then PyPDF2 to combine.

How to do this I'm less sure of as I'm not yet familiar enough with the tools (beyond knowing that this is something they can do).


## GUI for finished application

A web-based front-end that will provide the end user with a list of available documents to choose from as basic functionality.

This may end up being both complicated and simple. Complicated in that it'll probably be easiest to do it using a framework like Flask, simple in that what we'll be asking of it isn't too complicated.


# Questions to be answered:

- Is it better to add text on top of blank PDFs for the cover page/ToC or to render from scratch?
- Which framework makes the most sense for the GUI?