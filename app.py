#!/usr/bin/env python

import os

from flask import Flask
from flask import render_template

from database import db, Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()

    # fill DB with testing data(fixtures)
    #scifi = Genre(name="Научная фатасткиа")
    #db.session.add(scifi)
    #horror = Department(name="Ужас")
    #db.session.add(horror)

    #three_body = Book(fullname="Задача трех тел", genre=scifi)
    #db.session.add(three_body)
    #horror_book = Book(fullname="Кошмар на улице вязов", genre=horror)
    #db.session.add(horror_book)
    #dison = Book(fullname="Сфера дайсона", genre=scifi)
    #db.session.add(dison)


    fantasy = Genre(name="Фэнтези")
    scifi = Genre(name="Научная фантастика")
    drama = Genre(name="Драма")
    horror = Genre(name="Ужасы")

    db.session.add_all([fantasy, scifi, drama, horror])

    books_data = [
        {"title": "Властелин Колец",  "genre": fantasy},
        {"title": "Гарри Поттер и Философский камень", "genre": fantasy},
        {"title": "Солярис", "genre": scifi},
        {"title": "1984", "genre": drama},
        {"title": "Прощай, оружие!",  "genre": drama},
        {"title": "Игра престолов",  "genre": fantasy},
        {"title": "Темные начала", "genre": scifi},
        {"title": "Оно", "genre": horror},
        {"title": "Хоббит",  "genre": fantasy},
        {"title": "Ф451",  "genre": drama},
        {"title": "Автостопом по галактике", "genre": scifi},
        {"title": "Ночной дозор",  "genre": fantasy},
        {"title": "Дракула", "genre": horror},
        {"title": "Марсианин",  "genre": scifi},
        {"title": "Преступление и наказание", "genre": drama},
    ]

    books = [
        Book(name=data["title"], genre=data["genre"])
        for data in books_data
    ]
    db.session.add_all(books)

    db.session.commit()


@app.route("/")
def all_employees():
    books = Book.query.order_by(Book.added.desc()).limit(15).all()
    return render_template("all_books.html", books=books)


@app.route("/genre/<int:genre_id>")
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "books_by_genre.html",
        genre_name=genre.name,
        books=genre.books,
    )


if __name__ == '__main__':
    app.run()
