#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
    author1 = Author("John Doe")
    magazine1 = Magazine("Tech Mag", "Technology")
    ipdb.set_trace()
    article1 = author1.add_article(magazine1, "Python Programming")
    print(author1.name)
    print(author1.articles())
    print(author1.magazines())
