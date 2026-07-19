books = []



def add_book(name, author):
    books.append({'name': name, 'author': author})


def find_book_by_name(name):
    for book in books:
        if book['name'] == name:
            return book


def delete_book_by_name(name):
    found_book = find_book_by_name(name)
    if found_book is None:
        print('Knjiga koju trazite ne postoji.')
    else:
        books.remove(found_book)
        print('Obrisana je knjiga')
add_book('Harry Potter 1', 'J K Rowling')
add_book('Harry Potter 2', 'J K Rowling')

delete_book_by_name('Harry Potter 2')

print(books)