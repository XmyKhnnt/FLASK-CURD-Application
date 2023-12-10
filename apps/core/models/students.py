from ...settings import DatabaseConnection


class Student:

    def __init__(self):
        self._db = DatabaseConnection()

    def _establishConnection(self):
        self._db.connect()

    def getStudents(self, search_query=None):

        if search_query:
            sql = f"SELECT * FROM student WHERE  lower(name) LIKE '%{search_query}%'"
        else:
            sql = "SELECT * FROM student WHERE tot_cred = 0"

        self._establishConnection()
        results = self._db.execute_query(sql)
        self._db.commit_and_close()

        return results

    def getStudentCourses(self, student_id):

        try:
            query_param = int(student_id)
        except:
            return []

        if student_id == None:
            return []

        self._establishConnection()

        sql = """
                SELECT student.name, student.ID,course.title, course.credits, course.course_id, student.dept_name, takes.grade 
                FROM student 
                LEFT JOIN takes ON takes.ID = student.ID 
                LEFT JOIN course ON takes.course_id = course.course_id
                WHERE student.ID = '%s'

            """

        results = self._db.execute_query(sql, (query_param,))
        print(results)
        self._db.commit_and_close()

        return results

    def validateStudent(self, student_id):

        try:
            query_param = int(student_id)

        except Exception as e:
            print(e)
            return []

        if student_id == None:
            return []

        self._establishConnection()

        sql = """
                SELECT * FROM student WHERE ID = '%s'
            """

        results = self._db.execute_query(sql, (query_param,))
        self._db.commit_and_close()

        if results:
            return True

        return False\


    def insertStudent(self, student_data):
        self._establishConnection()

        data = (
            student_data['id'],
            student_data['name'],
            student_data['dept_name'],
            0
        )

        sql = """
            INSERT INTO student (ID, name, dept_name, tot_cred)
            VALUES (%s, %s, %s, %s)
        """

        self._db.execute_none_query(sql, data)
        self._db.commit_and_close()
        return True

    def studentWithFails(self, student_name=None):
        self._establishConnection()

        sql = """
            SELECT
                student.ID, 
                student.name,
                COUNT(*) AS num_failures, 
                student.dept_name, 
                student.tot_cred
            FROM
                student
                INNER JOIN
                takes
                ON 
                    student.ID = takes.ID
            WHERE
                grade IN ('F','D')
        """

        if student_name:
            sql += f" AND lower(student.name) LIKE '%{student_name}%'"

        sql += """
            GROUP BY
                student.ID,
                student.name
            HAVING
                COUNT(*) > 2
        """

        results = self._db.execute_query(sql)
        self._db.commit_and_close()

        return results
