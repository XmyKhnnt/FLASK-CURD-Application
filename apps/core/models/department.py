from ...settings import DatabaseConnection


class Department:

    def __init__(self):
        self._db = DatabaseConnection()

    def _establishConnection(self):
        self._db.connect()

    def all(self):

        sql = "SELECT  dept_name, dept_name as dept  FROM department"
        self._establishConnection()
        results = self._db.execute_query(sql)
        self._db.commit_and_close()

        print(results)
        return results
