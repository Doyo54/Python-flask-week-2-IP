class News:
    def __init__(self,content,author,img,date,url):
        self.content = content
        self.author =author
        self.img =img
        self.date =date
        self.url =url

class Source:
    def __init__(self,name,description,country,url):
        self.name =name
        self.description =description
        self.country = country
        self.url =url