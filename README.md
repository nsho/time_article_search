# Time Article Search (Work In Progress)
Web2py application that searches a known corpus of text documents. 

The search application is currently hosted at: https://nshort1234.pythonanywhere.com/search/default/time_search

The project makes use of the model-view-controller framework advocated by web2py. 

Web2py enables one to run python based web applications that allow a developer to manipulate a database, process data between and project a frontend interface largely with python code. 

Note: Many files included come out of the box with web2py and provide an admin interface for editing code and troubleshooting bugs. The files unique to this project are detailed below.

## Dataset
The Time Magazine dataset includes 423 text documents that were originally published as magazine articles.

The corpus dataset used can be downloaded at the following link: 
http://ir.dcs.gla.ac.uk/resources/test_collections/time/

The time.all folder was exported and manipulated locally with python and excel. The resultant files became datasets in the projects various databases.

The data for each of these can also be inspected in the databases folder.


## Model -- db.py
The model includes the file db.py. The end of this file includes code that defines the four sqlite databases utilized by this project. 

#### Corpus
The corpus table includes the full text from the corpus documents. These can also be referenced by date and docID fields.

#### Queries
The queries table enables the capture of user searches for processing and logging. The current project no longer utilizes this method and now processes queries without interacting with the database layer.

#### td_tfidf_a
This is and the next are two tables that serve the same purpose. They are partitioned as the data was too large for a single table.

These tables include a term-document tf-idf matrix with preprocessed tfidf values for all corpus terms. These values were derived locally with python and then inserted into the database.

#### td_idfB
This is the second of the two tables.
Also includes a term-document tf-idf matrix with preprocessed tfidf values for all corpus terms. 

These two tables are ultimately concatenated during processing in the controller file.

## Views
The View folder contains many files not relevant to the project. The two that are relevant include layout.html and time_search.html.

#### Layout.html
One of two view files utilized is layout.html which provides the main layout definition for the site. Much comes out of the box and is commented out for this project.

#### time_search.html
This is primary view file that is unique to this project. This defines the application URL and also how the results display on the page.

## Controller - default.py
The sole controller file utilized for this project is default.py.

This includes python code for the following:

#### Porter's Stemming algorithm: see stem() function

#### Query Processing: see getQueryInfo() function
This takes the stemmed query and returns the query norm and vector weights.

#### The Time Search time_search() function
This is primary function and calls the previous two.

time_search main tasks:
1) Defines the search form for the view to display. 
2) Accepts and processes the query.
3) call PS to get stems for query.
4) calls getQueryInfo() to obtain query norm/length and weights.
5) Selects td_tdidf databases and attempts to apply a cosine similarity comparison between the query and each document vector.

   #KNOWN ISSUE: results are consistently 0 due to dot product multiplying to equal zero. The dot product sums to zero, even when known terms included in the corpus are searched. This indicates to me that the non-empty weights in the vectors are not in alignment and that the vector indexes are discrepant.


    #To Do: add to cos_sim to dict of docs and cos similarity scores
    #To Do: function that sorts and retrieves list of top five scores
            ##these scores are returned in a table with fields: score, date, docID and link with preview text
    #To Do: #allow user to click the link and read the specified document

    #To Do: processing efficiencies:
        #1) reduce size of query/doc vectors by removing mutually empty values
        #2) create document tfidf dynamically rather than via precalculated table upload

    #To Do: Miscellaneous extra features that need to be added:
        #1)	Radio buttons on home page to enable user to select options such as weighting scheme.
        #2)	Relevance feedback table that compares with that in the dataset files.

