# import statements
import mysql.connector
from mysql.connector import Error
from pyresparser import ResumeParser
import boto3
from botocore.client import Config
from collections import defaultdict
import nltk
import random

nltk.download('stopwords')

# connects to s3, get all the resumes, if resume not already downloaded - download resume, get resume to download location
# insert the location into the tbl_resume table
def downloadResumeFromS3(res, connection, cursor):
    resume_links = []

    for item in res:
        resume_links.append(item[0])

    s3 = boto3.resource('s3',
                        aws_access_key_id="",
                        aws_secret_access_key="")

    for bucket in s3.buckets.all():
        if bucket.name == "bucketofresume":
            bucket_ob = bucket

    s3_client = boto3.client('s3',
                             aws_access_key_id="",
                             aws_secret_access_key="")

    for bucket_object in bucket_ob.objects.all():
        str_path = bucket_object.key
        if str_path not in resume_links:
            s3_client.download_file(
                Bucket="bucketofresume", Key=bucket_object.key, Filename=f"app/static/{bucket_object.key}"
            )

            res = (bucket_object.key)

            sql = """INSERT INTO tbl_resume_link (Resume_link, Loaded_flag) VALUES (%s, %s);"""

            record = (res, False)
            cursor.execute(sql, record)

            connection.commit()

            print(cursor.rowcount, "record(s) affected")


class DBConnect:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='db_recruitment',
                                                      user='root',
                                                      password='')
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)
                return self.connection

        except Error as e:
            print("Error while connecting to MySQL", e)

    def close(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")

    def get_cursor(self):
        return self.cursor

    def get_connection(self):
        return self.connection


# Parse resume - get data from resume
def parseResume(res, connection, cursor):
    for x in res:
        path = r'%s' % x[0]
        if x[1] == False:
            data = ResumeParser(f"app/static/{path}").get_extracted_data()
            insertParsedResumeData(x[0], data, connection, cursor)


# insert parsed resume data into tbl_candidates sql table
def insertParsedResumeData(resume_link, data, connection, cursor):
    # insert data from resume as record into sql table
    sql = """INSERT INTO tbl_candidate_resume (Candidate_Name, Contact_Email, Contact_phone, Work_Experience, Skill_Set, Education) VALUES (%s, %s, %s, %s,%s, %s);"""

    record = (data['name'], data['email'], data['mobile_number'], data['total_experience'], str(data['skills']),
              str(data['degree']))
    cursor.execute(sql, record)

    connection.commit()

    print(cursor.rowcount, "record(s) affected")

    sql = "UPDATE tbl_resume_link SET Loaded_flag = 1, Candidate_Name = %s WHERE Resume_link = %s"
    record = (data['name'],resume_link,)
    cursor.execute(sql, record)

    connection.commit()


# Insert new job roles into database
def insertOpenJobRole(connection ,cursor, role_name, work_experience, skillset, description):
    sql = """INSERT INTO tbl_open_roles (Role_name, Work_Experience, Skill_Set, Open_flag, role_description) VALUES (%s, %s, %s, %s, %s);"""

    record = (role_name, work_experience, str(skillset), 1 , str(description))
    print(record)
    cursor.execute(sql, record)
    connection.commit()

    print(cursor.rowcount, "record(s) affected")


# get all the links for resume
def getResumeLink(cursor):
    cursor.execute("SELECT Resume_link, Loaded_flag FROM tbl_resume_link")

    result = cursor.fetchall()

    return result

def getResumeLinkForCandidate(cursor, candidate_name):
    query = "SELECT Resume_link FROM tbl_resume_link where Candidate_name = %s"
    val = [candidate_name]
    cursor.execute(query, val)

    result = cursor.fetchall()

    result = result[0]
    print(type(result))

    return result[0]

# get relevant candidates
def shortlistCandidates(skillset, sql_exp, connection, cursor, role_name):
    res = defaultdict(int)
    for item in skillset:
        query = "SELECT * FROM tbl_candidate_resume WHERE skill_Set REGEXP (%s)"
        cursor.execute(query, (item.strip(),))

        result = cursor.fetchall()
        years = sql_exp

        for item_ in result:
            if years <= item_[4]:
                res[item_] += 1

    for key in res:
        print(role_name)
        print(key[0])
        print(res[key])

        query = "SELECT * FROM tbl_shortlisted_candidates WHERE role_name = %s and Candidate_ID = %s"
        values = [role_name, key[0]]
        cursor.execute(query, values)

        result = cursor.fetchall()

        if not result:
            sql = "INSERT INTO tbl_shortlisted_candidates (Role_name, candidate_ID, candidate_score) VALUES (%s, %s, %s)"
            val = (role_name, int(key[0]), res[key])
            cursor.execute(sql, val)

            connection.commit()
            print(cursor.rowcount, "record inserted.")


def getShortlistedCandidates(rolename, cursor):
    query = """SELECT ID, Role_name, Candidate_Name, Contact_Email, Contact_phone, Work_Experience, Skill_set, Education, candidate_score  FROM tbl_candidate_resume cr INNER JOIN tbl_shortlisted_candidates sc ON sc.candidate_ID = cr.ID WHERE sc.Role_name = %s ORDER BY candidate_score DESC"""
    role_name = [rolename]
    cursor.execute(query, role_name)

    result = cursor.fetchall()
    return result


# get all the candidates
def getAllCandidates(cursor):
    query = """SELECT ID, Candidate_Name, Contact_Email, Contact_phone, Work_Experience, Skill_set, Education FROM tbl_candidate_resume"""
    cursor.execute(query)

    result = cursor.fetchall()

    return result


# get all employees of the company
def getAllEmployees(cursor):
    query = "SELECT * FROM tbl_employees"
    cursor.execute(query)

    result = cursor.fetchall()
    return result


# get all employees of the company
def getOpenRoles(cursor):
    query = "SELECT * FROM tbl_open_roles where Open_flag=1"
    cursor.execute(query)

    result = cursor.fetchall()
    return result


def closeJobRole(cursor, connection, role_name):
    sql = "UPDATE tbl_open_roles SET Open_flag = 0 WHERE Role_name = %s"
    record = (role_name,)
    cursor.execute(sql, record)

    connection.commit()

# get relevant employees for a role(for interview)
def getInterviewers(skillset, sql_exp, cursor):
    res = defaultdict(int)
    for item in skillset:

        query = "SELECT ID, Employee_Name, Email, Current_Role, Work_Experience, Skill_set, Education FROM tbl_employees WHERE skill_Set REGEXP (%s)"
        cursor.execute(query, (item.strip(),))

        result = cursor.fetchall()
        years = sql_exp

        for item_ in result:
            if years <= item_[4]:
                res[item_] += 1

    print(res)
    return res

def getRoleRequirements(cursor, role_name):
    sql = """select Skill_set from tbl_open_roles where Role_name = %s"""
    sql_exp = """select Work_Experience from tbl_open_roles where Role_name = %s"""
    record = [role_name]

    cursor.execute(sql, record)
    result = cursor.fetchall()
    print(result)
    str_result = str(result)
    str_result = str_result.replace("\'", "")
    str_result = str_result.replace("(", "")
    str_result = str_result.replace(")'", "")
    str_result = str_result.replace("[", "")
    str_result = str_result.replace("]'", "")
    skillset = []
    skillset = str_result.split(",")
    skillset = skillset[0:len(skillset) - 1]

    print(skillset)

    cursor.execute(sql_exp, record)
    res = cursor.fetchall()
    for val in res:
        sql_exp = val[0]
    print(sql_exp)

    return skillset, sql_exp


# first function to be called to get relevant candidates and employees for a role
def getRelevantCandidates(connection, cursor, role_name):
    skillset, sql_exp = getRoleRequirements(cursor, role_name)
    print("Candidates:")
    shortlistCandidates(skillset, sql_exp, connection, cursor, role_name)
    return getShortlistedCandidates(role_name, cursor)


def getRelevantInterviewers(cursor, role_name):
    skillset, sql_exp = getRoleRequirements(cursor, role_name)
    print("Interviewers:")
    # get employees relevant to a role
    return getInterviewers(skillset, sql_exp, cursor)

def getMostRelevantInterviewer(cursor, role_name):
    interviewerScoreMap = getRelevantInterviewers(cursor=cursor, role_name=role_name)
    
    if interviewerScoreMap:
        print("Random: ", random.choice(list(interviewerScoreMap.items()))[0])
        return random.choice(list(interviewerScoreMap.items()))[0]

    # max_score = max(interviewerScoreMap.values())
    # for interviewer in interviewerScoreMap:
    #     if interviewerScoreMap[interviewer] == max_score:
    #         return interviewer

    # Default (CEO!)
    return (999, "John", "john@company.com", "CEO", 25, "Everything", "MBA")


def submitFeedback(cursor, connection, c_name, c_feedback, role_name):
    sql = "INSERT INTO tbl_feedback (Candidate_Name, Feedback, Role_name) VALUES (%s, %s, %s)"
    val = (c_name, c_feedback, role_name)
    cursor.execute(sql, val)

    connection.commit()
    print(cursor.rowcount, "record inserted.")

def getAllFeedback(cursor):
    query = "SELECT * FROM tbl_feedback"
    cursor.execute(query)

    result = cursor.fetchall()
    return result

def main():
    db = DBConnect()
    connection = db.connect()
    cursor = db.get_cursor()

    resume_links = getResumeLink(cursor)
    downloadResumeFromS3(resume_links, connection, cursor)

    resume_links = getResumeLink(cursor)
    parseResume(resume_links, connection, cursor)

    # Get all candidates
    print("All candidates: ")
    candidates = getAllCandidates(cursor)
    print(candidates)

    # get all employees
    print("All Employees: ")
    employees = getAllEmployees(cursor)
    print(employees)

    # get candidates relevant to an open role
    relevant_candidates = getRelevantCandidates(connection, cursor, "Support Engineer")
    print(relevant_candidates)

    # get relevant interviewerScoreMap for the open role
    relevant_interviewerScoreMap = getRelevantInterviewers(cursor, "Support Engineer")
    print(relevant_interviewerScoreMap)

    # Submit feedback for a candidate
    c_name = "Dhanasree Rajamani"
    c_feedback = "Good"
    submitFeedback(cursor, connection, c_name, c_feedback, "Software Engineer")
    print("Feedback submitted")


if __name__ == "__main__":
    main()