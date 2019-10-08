import pymysql

class Articles():

    def fetchArticles(self):
        # Connect to the database.

        conn = pymysql.connect(
            db='jasonsnider',
            user='root',
            passwd='password',
            host='localhost')
        c = conn.cursor()
        c.execute("SELECT * FROM articles")
        
        return c.fetchall()

    def fetchArticle(self, slug):
        # Connect to the database.

        conn = pymysql.connect(
            db='jasonsnider',
            user='root',
            passwd='password',
            host='localhost')

        c = conn.cursor()
        c.execute("SELECT * FROM articles WHERE slug = %s", (slug))
        
        return c.fetchone()
        