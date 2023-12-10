from ...settings import DatabaseConnection


class Course:

    def __init__(self):
        self._db = DatabaseConnection()

    def _establishConnection(self):
        self._db.connect()

    def all(self, keyword=None):

        if keyword:
            sql = "SELECT * FROM course WHERE title LIKE %s"
            params = (f"%{keyword}%",)
        else:
            sql = "SELECT * FROM course"
            params = None

        self._establishConnection()
        results = self._db.execute_query(sql, params)
        self._db.commit_and_close()

        print(results)
        return results
