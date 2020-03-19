# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a controller
#compare query with matrices
import numpy as np
import pandas as pd
import nltk
from collections import Counter

def getQueryInfo(Q):
    'Calculate norm of query tokens and return length and weight vector.'
    N = 423 #number of documents in corpus
    Nta = 0 #initializes
    Ntb = 0
    w = 0
    token_list = []
    t_loop_list = []
    weights = {}
    Q_sumsquares = 0 #initialize
    results = []
    id_list = {}
    allweights = []
    for T in Q:
        token_list.append(T)
    counts = Counter(token_list) #creates dictionary of query token frequencies

    for T in Q:#for each token in query terms
        Nta = 0 #reinitialize terms counts
        Ntb = 0 #reinitialize
        if T not in t_loop_list: #ensures Nt values not calculated more than once
            for row in db(db.td_tfidf_a.stem == T).select(): #iterates through tfidf matrix 1 'a'
                id_list[row.id] = row.stem
                for value in row: #iterates through tfidf value per doc for found token
                    try:
                        a = float(row[value])
                        if a > 1:
                            continue #skips row id column
                        elif a > 0:
                            Nta = Nta + 1 #counts number of documents with token
                    except:
                        continue #skips stem column

            for row in db(db.td_tfidfB.stem == T).select(): #iterates through tfidf matrix 2 'b'
                for value in row: #iterates through tfidf value per doc for found token
                    try:
                        b = float(row[value])
                        if b > 1:
                            continue #skips row id column
                        elif b > 0:
                            Ntb = Ntb + 1 #counts number of documents with token based on if term has tfidf greater than 0
                    except:
                        continue #skips stem column
        elif T in t_loop_list:
            continue
        t_loop_list.append(T)
         #assists in preventing calculating Nt calculated twice for one term
        #K is number of times term is in query
        K = counts[T]
        #calculate weights for each token
        if (Nta + Ntb) > 0:
            w = (K * (np.log2(N/(Nta+Ntb))))
            weights[T] = w
        else:
            w = 0
            weights[T] = w
        #calculate sum of weight squares
        Q_sumsquares = Q_sumsquares + (w*w)
    #outside of T in msg loop, take square root of query sum of weight squares
    #this is the query length
    queryLength = np.sqrt(Q_sumsquares)
    L = queryLength

    for row in db().select(db.td_tfidfB.ALL): #this adds empty weights to the query vector to ensure its size matches that of the document vectors.
        for id in id_list.keys():
            if row.id == id:
                allweights.append(weights[id_list[id]])
                break
            else:
                allweights.append(0)
                break

    return L, allweights

def stem(terms):
    'Stems the input terms according to Porter Algorithm.'
    from nltk.stem import PorterStemmer
    from nltk.tokenize import sent_tokenize, word_tokenize
    ps = PorterStemmer()
    terms = word_tokenize(terms)
    stemList = []
    for t in terms:
        stemList.append(ps.stem(t))
    return stemList

def time_search():
    'Main search function'
    form = SQLFORM.factory(
        Field('Query', requires=IS_NOT_EMPTY()),
        submit_button='Search')
    if form.process().accepted:
        response.flash = 'form accepted'
        session.Query = form.vars.Query
    elif form.errors:
        response.flash = 'form has errors'

    stemmed_query = stem(session.Query) #runs stemming function on submitted search query terms

    msg = stemmed_query #transfers query to msg variable to display from View file
    #results = SQLTABLE(db().select(db.corpus.ALL))
    q_length, q_weights = getQueryInfo(msg)

    #get each doc vector

    #dba = db.executesql('SELECT td_tfidf_a.doc17,	td_tfidf_a.doc18,	td_tfidf_a.doc19,	td_tfidf_a.doc20,	td_tfidf_a.doc21,	td_tfidf_a.doc23,	td_tfidf_a.doc24,	td_tfidf_a.doc25,	td_tfidf_a.doc26,	td_tfidf_a.doc27,	td_tfidf_a.doc28,	td_tfidf_a.doc29,	td_tfidf_a.doc30,	td_tfidf_a.doc31,	td_tfidf_a.doc32,	td_tfidf_a.doc33,	td_tfidf_a.doc34,	td_tfidf_a.doc35,	td_tfidf_a.doc36,	td_tfidf_a.doc40,	td_tfidf_a.doc42,	td_tfidf_a.doc43,	td_tfidf_a.doc45,	td_tfidf_a.doc47,	td_tfidf_a.doc48,	td_tfidf_a.doc49,	td_tfidf_a.doc50,	td_tfidf_a.doc51,	td_tfidf_a.doc52,	td_tfidf_a.doc53,	td_tfidf_a.doc54,	td_tfidf_a.doc55,	td_tfidf_a.doc57,	td_tfidf_a.doc58,	td_tfidf_a.doc59,	td_tfidf_a.doc60,	td_tfidf_a.doc61,	td_tfidf_a.doc62,	td_tfidf_a.doc63,	td_tfidf_a.doc64,	td_tfidf_a.doc65,	td_tfidf_a.doc66,	td_tfidf_a.doc67,	td_tfidf_a.doc68,	td_tfidf_a.doc69,	td_tfidf_a.doc70,	td_tfidf_a.doc71,	td_tfidf_a.doc72,	td_tfidf_a.doc81,	td_tfidf_a.doc82,	td_tfidf_a.doc83,	td_tfidf_a.doc84,	td_tfidf_a.doc85,	td_tfidf_a.doc86,	td_tfidf_a.doc87,	td_tfidf_a.doc88,	td_tfidf_a.doc90,	td_tfidf_a.doc91,	td_tfidf_a.doc92,	td_tfidf_a.doc93,	td_tfidf_a.doc94,	td_tfidf_a.doc95,	td_tfidf_a.doc96,	td_tfidf_a.doc97,	td_tfidf_a.doc98,	td_tfidf_a.doc99,	td_tfidf_a.doc100,	td_tfidf_a.doc101,	td_tfidf_a.doc102,	td_tfidf_a.doc104,	td_tfidf_a.doc105,	td_tfidf_a.doc106,	td_tfidf_a.doc107,	td_tfidf_a.doc108,	td_tfidf_a.doc109,	td_tfidf_a.doc110,	td_tfidf_a.doc111,	td_tfidf_a.doc112,	td_tfidf_a.doc113,	td_tfidf_a.doc115,	td_tfidf_a.doc116,	td_tfidf_a.doc117,	td_tfidf_a.doc118,	td_tfidf_a.doc119,	td_tfidf_a.doc120,	td_tfidf_a.doc121,	td_tfidf_a.doc122,	td_tfidf_a.doc123,	td_tfidf_a.doc126,	td_tfidf_a.doc128,	td_tfidf_a.doc129,	td_tfidf_a.doc130,	td_tfidf_a.doc131,	td_tfidf_a.doc133,	td_tfidf_a.doc134,	td_tfidf_a.doc135,	td_tfidf_a.doc136,	td_tfidf_a.doc137,	td_tfidf_a.doc138,	td_tfidf_a.doc140,	td_tfidf_a.doc143,	td_tfidf_a.doc144,	td_tfidf_a.doc145,	td_tfidf_a.doc146,	td_tfidf_a.doc147,	td_tfidf_a.doc148,	td_tfidf_a.doc149,	td_tfidf_a.doc150,	td_tfidf_a.doc151,	td_tfidf_a.doc152,	td_tfidf_a.doc153,	td_tfidf_a.doc154,	td_tfidf_a.doc155,	td_tfidf_a.doc156,	td_tfidf_a.doc157,	td_tfidf_a.doc158,	td_tfidf_a.doc159,	td_tfidf_a.doc160,	td_tfidf_a.doc161,	td_tfidf_a.doc162,	td_tfidf_a.doc163,	td_tfidf_a.doc170,	td_tfidf_a.doc171,	td_tfidf_a.doc172,	td_tfidf_a.doc173,	td_tfidf_a.doc174,	td_tfidf_a.doc175,	td_tfidf_a.doc176,	td_tfidf_a.doc177,	td_tfidf_a.doc178,	td_tfidf_a.doc179,	td_tfidf_a.doc180,	td_tfidf_a.doc181,	td_tfidf_a.doc182,	td_tfidf_a.doc183,	td_tfidf_a.doc184,	td_tfidf_a.doc185,	td_tfidf_a.doc186,	td_tfidf_a.doc187,	td_tfidf_a.doc188,	td_tfidf_a.doc189,	td_tfidf_a.doc190,	td_tfidf_a.doc191,	td_tfidf_a.doc192,	td_tfidf_a.doc193,	td_tfidf_a.doc194,	td_tfidf_a.doc195,	td_tfidf_a.doc196,	td_tfidf_a.doc197,	td_tfidf_a.doc198,	td_tfidf_a.doc199,	td_tfidf_a.doc200,	td_tfidf_a.doc201,	td_tfidf_a.doc202,	td_tfidf_a.doc203,	td_tfidf_a.doc204,	td_tfidf_a.doc213,	td_tfidf_a.doc214,	td_tfidf_a.doc215,	td_tfidf_a.doc217,	td_tfidf_a.doc218,	td_tfidf_a.doc219,	td_tfidf_a.doc220,	td_tfidf_a.doc221,	td_tfidf_a.doc222,	td_tfidf_a.doc223,	td_tfidf_a.doc224,	td_tfidf_a.doc225,	td_tfidf_a.doc226,	td_tfidf_a.doc227,	td_tfidf_a.doc228,	td_tfidf_a.doc229,	td_tfidf_a.doc230,	td_tfidf_a.doc231,	td_tfidf_a.doc232,	td_tfidf_a.doc234,	td_tfidf_a.doc235,	td_tfidf_a.doc236,	td_tfidf_a.doc237,	td_tfidf_a.doc238,	td_tfidf_a.doc239,	td_tfidf_a.doc240,	td_tfidf_a.doc241,	td_tfidf_a.doc242,	td_tfidf_a.doc243,	td_tfidf_a.doc244,	td_tfidf_a.doc245,	td_tfidf_a.doc246,	td_tfidf_a.doc247,	td_tfidf_a.doc248,	td_tfidf_a.doc249,	td_tfidf_a.doc250,	td_tfidf_a.doc251,	td_tfidf_a.doc252,	td_tfidf_a.doc253,	td_tfidf_a.doc254,	td_tfidf_a.doc255,	td_tfidf_a.doc256,	td_tfidf_a.doc257,	td_tfidf_a.doc258,	td_tfidf_a.doc259,	td_tfidf_a.doc260,	td_tfidf_a.doc261 FROM td_tfidf_a;')
    dba = db.executesql('SELECT td_tfidf_a.doc17,	td_tfidf_a.doc21,	td_tfidf_a.doc29 FROM td_tfidf_a;')
    #dbb = db.executesql('SELECT * FROM td_tfidfB;')
    dfa = pd.DataFrame(dba)
    #dfb = pd.DataFrame(dbb)
    #df = pd.concat([dfa,dfb], axis=1)

    #To Do: undo above commenting out. Currently only selects three documents for testing efficiency. Need to select all docs and concatenate each table.

    df = dfa.astype('float')
    #get length of each document vector
    results = []
    loop = 0
    #results = dfa
    for col in df:
        if loop == 0:
            loop = loop + 1 #increment loop
            continue
        else:
            loop = loop + 1 #increment loop
            d_sumsquares = 0
            #if not a tfidf value such as table id or stem, go to next column
            for w in df[col]: #loop to sum the weight squares
                d_sumsquares = d_sumsquares + w*w

            doc_weights = df[col]
            doc_length = np.sqrt(d_sumsquares)
            #compute cosine similarity
            cos_sim = np.dot(q_weights,doc_weights)/(q_length*doc_length)
            results.append(cos_sim)

    #KNOWN ISSUE: results are consistently 0 due to doc product multiplying to equal zero.

    #To Do: add to cos_sim to dict of docs and cos similarity scores
    #To Do: function that sorts and retrieves list of top five scores
            ##these scores are returned in a table with fields: score, date, docID and link with preview text
    #To Do: #allow user to click the link and read the specified document

    #To Do: processing efficiencies:
        #1) reduce size of query/doc vectors by removing mutually empty values
        #2) create document tfidf dynamically rather than via precalculated table upload

    #To Do: add radio buttons on home page to enable user to select options such as weighting scheme

    return dict(form=form, msg=msg, results=results)





# ---- example index page ----
# this comes packaged by default with web2py

'''

def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki()

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
'''
