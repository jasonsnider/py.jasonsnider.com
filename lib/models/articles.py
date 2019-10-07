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