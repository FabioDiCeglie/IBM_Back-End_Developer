from flask import Flask

app = Flask(__name__)

@app.route("/")
def login():

  username = request.values.get('username')
  password = request.values.get('password')

  # Prepare database connection.
  db = pymysql.connect("localhost")
  cursor = db.cursor()

  # # Execute the SQL query concatenating user-provided input.
  # sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
  # cursor.execute(sql)

  # Execute the SQL query concatenating user-provided input.
  sql = "SELECT * FROM users WHERE username = %s AND password = %s"
  cursor.execute(sql, (username, password))

  # If the query returns any matching record, consider the current user logged in.
  record = cursor.fetchone()
  if record:
    session['logged_user'] = username

  # Disconnect from server.
  db.close()


## bandit -r web_app_example.py
  
## RESULT
  
# Run started:2024-04-01 18:26:38.885910

# Test results:
# >> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
#    Severity: Medium   Confidence: Low
#    Location: web_app_example.py:16:8
#    More Info: https://bandit.readthedocs.io/en/latest/plugins/b608_hardcoded_sql_expressions.html
# 15        # Execute the SQL query concatenating user-provided input.
# 16        sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
# 17        cursor.execute(sql)

# --------------------------------------------------
  
## AFTER USING LINE 20

# Test results:
#         No issues identified.

# Code scanned:
#         Total lines of code: 14
#         Total lines skipped (#nosec): 0

# Run metrics:
#         Total issues (by severity):
#                 Undefined: 0.0
#                 Low: 0.0
#                 Medium: 0.0
#                 High: 0.0
#         Total issues (by confidence):
#                 Undefined: 0.0
#                 Low: 0.0
#                 Medium: 0.0
#                 High: 0.0
# Files skipped (0):