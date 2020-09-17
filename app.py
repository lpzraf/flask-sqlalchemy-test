from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Heyooooo</h1>"


# conn = psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="",
#     host="localhost"
# )

# cur = conn.cursor()

# cur.execute("select * from users")

# rows = cur.fetchall()

# for user in rows:
#     print(f"id: {user[0]}, age: {user[1]}, name: {user[2]}")

# cur.close()
# conn.close()


if __name__ == "__main__":
    app.run()