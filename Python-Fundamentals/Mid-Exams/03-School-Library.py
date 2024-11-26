#School Library

books = input().split('&')

cmd = input()

while cmd != "Done":
    cmdSplit = cmd.split('|')
    cmdSplit = [i.strip() for i in cmdSplit if i.strip()]
    action = cmdSplit[0]

    if action == "Add Book":
        book = cmdSplit[1]
        if book not in books:
            books.insert(0, book)
    if action == "Take Book":
        book = cmdSplit[1]
        if book in books:
            books.remove(book)
    if action == "Swap Books":
        book1 = cmdSplit[1]
        book2 = cmdSplit[2]
        if book1 in books and book2 in books:
            index1 = books.index(book1)
            index2 = books.index(book2)
            books[index1] = book2
            books[index2] = book1
    if action == "Insert Book":
        book = cmdSplit[1]
        if book not in books:
            books.append(book)
    if action == "Check Book":
        index = int(cmdSplit[1])
        if 0 <= index <= (len(books) - 1):
            print (f"{books[index]}")
    cmd = input()

print (f"{', '.join(books)}")