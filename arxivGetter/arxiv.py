#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:54:10 2019

@author: andrewblance
"""

import feedparser
from flask import Flask, request, jsonify
app = Flask(__name__)

#export FLASK_APP=arxiv.py
#flask run
# curl localhost:5000/arxiv --form "query=hep-ph"

@app.route('/')
def hello_world():
    return 'Hello, World!'

def parser(query):
    # pull info from arXiv
    url = 'http://export.arxiv.org/api/query?search_query=all:' + query + '&start=0&max_results=2&sortBy=lastUpdatedDate&sortOrder=descending'
    result = feedparser.parse(url)
    return result

@app.route('/arxiv', methods=['POST', 'GET'])    
def jsoner():
    if request.method == 'POST':
        print('info received')
        query = request.form['query']
        
        result = parser(query)
        
        paper_info = []
        authors = []
        contains = []
        
        # if the query has results, parse the results
        if len(result.feed) != 0:
            for x in result.entries:
                print(x.title)
                contains.append(x.title)
                
                tmpAuthor = []
                if len(x.authors) > 3:
                    tmpAuthor.append(str(x.authors[0].name) + ', et al')
                else:
                    for y in x.authors:
                        tmpAuthor.append(y.name)
                authors.append(tmpAuthor)
            
                paper_info.append(
                        dict(title = x.title ,
                             authors = tmpAuthor,
                             abstract = x.summary
                           )     
                        )
         
        # create dictionary about query and results               
        data = dict(query = query,
                    contains = contains,
                    paper_info = paper_info)
        
        return jsonify(data)
    
    else:
        return "oops"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    

        
    
