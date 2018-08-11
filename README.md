# Semantic Scholar-Search-Engine
Using SemanticScholarAPI to search published articles of the author, and create word cloud to show the frequence of some keywords appearred within the article titles.

## Dev environment setup
Python 3 is the main language used in this codebase.
We strongly encourage the use of Python [virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/):

    virtualenv venv -p /usr/bin/python3
    source venv/bin/activate

After which, you can install the required Python modules in the requirments.txt(some of them cannot be used pip straightly)
## Web Scrawling
Due to the paper information of an author can only be searched by the author ID in Senamtic Scholar website, I do the web scrawling work first to scrap author ID number according to the author name. For the situation of duplicate names, I will list all the ID that meet the input name.
## Use the Search Engine
You can run the model via

    python main.py
You will see the UI and type in the author name, like:
![image](https://github.com/RichieLee93/Semantic-Scholar-Search-Engine/blob/master/1.png)

Then click "search" button and the articles titles of the author will listed as:
![image](https://github.com/RichieLee93/Semantic-Scholar-Search-Engine/blob/master/2.png)

And also the word cloud of this author based on his paper titles will appear:
![image](https://github.com/RichieLee93/Semantic-Scholar-Search-Engine/blob/master/3.png)

For any authors who have same name, the engine will show the article and word cloud information for each of them independently as other pics in the folder show.
