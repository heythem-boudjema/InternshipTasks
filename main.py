import pyodbc
import json
def EuroToDollar(Price):
 return float(Price)*1.2
connection = pyodbc.connect("Driver={SQL Server};" + "Server=localhost;"+ "Database=Itransition_Task3.5;"+"Trusted_connection=True;")

with open("books.json", "r", encoding="utf-8") as file:
    data = json.load(file)

    for book in data:
        year = book["year"]

        if book["price"][0] == "€":
            price = EuroToDollar(float(book["price"][1:]))
        else:
            price = book["price"][1:]

        try:
            connection.execute("""
                INSERT INTO JsonBooks
                (ID, title, author, genre, publisher, PubYear, price)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                str(book["id"]),
                book["title"],
                book["author"],
                book["genre"],
                book["publisher"],
                book["year"],
                price
            )

        except pyodbc.Error as e:
            print(e)

    connection.commit()

    

