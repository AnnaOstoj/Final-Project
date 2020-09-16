from blog import models, db

"""
def add_book(book_form):
    new_title = book_form.data["title"]
    title = models.Title(title = new_title)
    db.session.add(title)

    new_author_input = book_form.data["author"]
    new_author_list = new_author_input.split(sep=",")
    
    for i in new_author_list:
        author = models.Author.query.filter_by(author=i).first()
        if author is None:
            author = models.Author(author = i)
            db.session.add(author)
            db.session.commit()
        title.authors.append(author)
        db.session.commit()


def borrow_book(book_title):
    book = models.Title.query.filter_by(title=book_title).first()
    borrowed = models.Borrowed(book = book)
    db.session.add(borrowed)
    db.session.commit()

def delete_book(book_title):
    book = models.Title.query.filter_by(title=book_title).first()
    borrowed = models.Borrowed.query.filter_by(book_id=book.title_id).first()
    
    if borrowed is not None:
        db.session.delete(borrowed)
    db.session.delete(book)
    db.session.commit()
"""
def load():
    posts_list = []
    
    for entry in models.Entry.query.all():
        temp_post = {}
        temp_post["title"] = entry.title
        temp_post["body"] = entry.body
        temp_post["pub_date"] = entry.pub_date
        temp_post["is_published"] = entry.is_published
        temp_post["id"] = entry.id
        posts_list.append(temp_post)
 
    return posts_list