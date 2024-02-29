class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.add_new_article(self)
       
        
    @classmethod
    def add_new_article(cls, new_instance):
        cls.all.append(new_instance)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not hasattr(self, "_title"):
            if type(new_title) == str:
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    raise ValueError("Title must be between 5 and 50 characters")
            else:
                raise TypeError("Name must be a string")  

    
        
class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if hasattr(self, "_name"):
            raise AttributeError("Name should be a string.")
        else:
            if isinstance(new_name, str):
                if len(new_name) > 0:
                    self._name = new_name
                else:
                    raise ValueError("Name cannot be zero characters")
            else:
                raise TypeError("Name must be a string")




    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})


    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str):
            new_article = Article(self, magazine, title)
            new_article.author = self
            return new_article
        else:
            raise ValueError("Invalid arguments for creating an article")
        
    def topic_areas(self):
        article_categories = [article.magazine.category for article in self.articles()]
        return list(set(article_categories)) if article_categories else None


class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._contributors = set()
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = name
         
        
    @property
    def category(self):
        return self._category

    @category.setter 
    def category(self, new_category):
        if isinstance(new_category, str):
            if 0 < len(new_category):
                self._category = new_category
            else:
                raise ValueError("Category must have characters")
        else:
            raise TypeError("Category must be a string")


    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        unique_authors = set()
        for article in self.articles():
            unique_authors.add(article.author)
        unique_author_list = list(unique_authors)
        if all(isinstance(author, Author)for author in unique_author_list):
            return unique_author_list
        else:
            return None

    def article_titles(self):
        magazine_articles = [article.title for article in self.articles()]
        if magazine_articles:
            return magazine_articles
        else:
            return None

    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            author = article.author
            if author in author_article_count:
                author_article_count[author] += 1
            else:
                author_article_count[author] = 1

        contributing_authors = [author for author, count in author_article_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

