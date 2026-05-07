import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",             
    password="1234",
    database="keywordextraction"
)


cursor = conn.cursor()
cursor.execute("SELECT text FROM malayalam_corpus")  

rows = cursor.fetchall()

full_raw_text = "\n\n".join([row[0] for row in rows])

output_file = "malayalam_raw_corpus.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(full_raw_text)

print(f"Saved raw corpus to: {output_file}")
