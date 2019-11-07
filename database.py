#!/usr/bin/env python3
import psycopg2

#####################################################
##  Database Connect
#####################################################

'''
Connects to the database using the connection string
'''
def openConnection():
# connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "y19s2c9120_490490347"
    passwd = "XXSSamsung10"
    myHost = "soit-db-pro-2.ucc.usyd.edu.au"

    # Create a connection to the database
    conn = None
    try:
        # Parses the config file and connects using the connect string
        conn = psycopg2.connect(database=userid,
                                    user=userid,
                                    password=passwd,
                                    host=myHost)
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
    
    # return the connection to use
    finally:
        if conn is not None and conn.is_connected():
            conn.close()

'''
List all the user associated issues in the database for a given user 
See assignment description for how to load user associated issues based on the user id (user_id)
'''
def findUserIssues(user_id):
    # TODO - list all user associated issues from db using sql
    print(user_id)
    issue_db = [
        ['Division by zero', '1', '1', '1', 'Division by 0 doesn\'t yield error or infinity as would be expected. Instead it results in -1.', '1'],
        ['Factorial with addition anomaly', '1', '1', '1', 'No description', '2']
    ]

    issue = [{
        'title': row[0],
        'creator': row[1],
        'resolver': row[2],
        'verifier': row[3],
        'description': row[4],
        'issue_id': row[5]
    } for row in issue_db]

    return issue

'''
Find the associated issues for the user with the given userId (user_id) based on the searchString provided as the parameter, and based on the assignment description
'''
def findIssueBasedOnExpressionSearchedOnTitleAndDescription(searchString, user_id):

    # TODO - find necessary issues using sql database based on search input
    print(user_id)
    print("search string '" + searchString + "'")
    issue_db = [
        ['Division by zero', '1', '1', '1', 'Division by 0 doesn\'t yield error or infinity as would be expected. Instead it results in -1.', '1']
    ]

    issue = [{
        'title': row[0],
        'creator': row[1],
        'resolver': row[2],
        'verifier': row[3],
        'description': row[4],
        'issue_id': row[5]
    } for row in issue_db]

    return issue

#####################################################
##  Issue (new_issue, get all, get details)
#####################################################
#Add the details for a new issue to the database - details for new issue provided as parameters
# noinspection PyUnreachableCode
def addIssue(title, creator, resolver, verifier, description):
    # TODO - add an issue
    # Insert a new issue to database
    # return False if adding was unsuccessful 
    # return Ture if adding was successful
    try:
        conn = psycopg2.connect(database=userid,
                                user=userid,
                                password=passwd,
                                host=myHost)
        except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)

    # return the connection to use
    return conn
        mySql_insert_query = """INSERT INTO A3_ISSUE (title, creator, resolver, verifier, description) 
                                    VALUES (%s, %s, %s, %s, %s) """

        recordTuple = (title, creator, resolver, verifier, description)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("True")

    except mysql.connector.Error as error:
        print("False")

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertVariblesIntoTable('TV Flickers', 'TV flicking', 1, 1, 2)
insertVariblesIntoTable(3, 'MacBook Pro', 'Macbook Prop not working', 2, 1)



#Update the details of an issue having the provided issue_id with the values provided as parameters
def updateIssue(title, creator, resolver, verifier, description, issue_id):

    # TODO - update the issue using db
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE A3_issues
                    SET title = %s
                    WHERE issue_id = %s """

    data = (title, creator, resolver, verifier, description, issue_id)

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
    # return False if adding was unsuccessful 
    # return Ture if adding was successful
    return True
