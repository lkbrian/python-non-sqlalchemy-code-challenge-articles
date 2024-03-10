class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) and not 5 <= len(title) <= 50:
            raise Exception("the string should be more than 1 letter")
        self.title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not 5 <= len(value) <= 50:
            raise Exception("the string should be more than 1 letter")
        self._title = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) and not (len(name) > 0):
            raise Exception("invalid")
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (len(value) > 0):
            raise Exception("invalid")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles().append(article)
        return article

    def topic_areas(self):
        return (
            list(set(magazine.category for magazine in self.magazines()))
            if self.articles()
            else None
        )


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Invalid name length between 2 and 16 characters")
        self.name = name

        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Not a valid category")
        self.category = category

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 2 <= len(value) <= 16:
            raise Exception("Invalid name length between 2 and 16 characters")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()] if self.articles() else None

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            author = article.author
            if author in authors:
                authors[author] += 1
            else:
                authors[author] = 1
        
        return [author for author, count in authors.items() if count > 2 and isinstance(author, Author)]


    # @classmethod
    # def top_publisher(cls):
    #     if not cls.all:
    #         return None
    #     return max(cls.all, key=lambda magazine: len(magazine.articles()))

