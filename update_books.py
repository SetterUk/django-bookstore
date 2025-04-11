from store.models import Book

# New book titles
new_titles = [
    "The Midnight Library",
    "Atomic Habits",
    "The Silent Patient",
    "Educated",
    "Where the Crawdads Sing"
]

# Update each book with a new title
for i, book in enumerate(Book.objects.all()):
    if i < len(new_titles):
        book.title = new_titles[i]
        book.save()
        print(f"Updated book {book.id} to: {book.title}") 