from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .models import Book, Cart, CartItem
from django.db.models import Q

# Create your views here.

@login_required(login_url='login')
def home(request):
    # Check if there are any books, if not create sample books
    if Book.objects.count() == 0:
        print("No books found, creating sample books...")
        # Create sample books
        sample_books = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'price': 12.99,
                'description': 'A story of the fabulously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan.',
                'stock': 10
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'price': 14.99,
                'description': 'The story of racial injustice and the loss of innocence in the American South.',
                'stock': 15
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'price': 11.99,
                'description': 'A dystopian social science fiction novel and cautionary tale.',
                'stock': 8
            },
            {
                'title': 'Pride and Prejudice',
                'author': 'Jane Austen',
                'price': 10.99,
                'description': 'A romantic novel of manners.',
                'stock': 12
            },
            {
                'title': 'The Hobbit',
                'author': 'J.R.R. Tolkien',
                'price': 15.99,
                'description': 'The adventure of Bilbo Baggins, a hobbit who embarks on a quest.',
                'stock': 20
            },
            {
                'title': 'The Catcher in the Rye',
                'author': 'J.D. Salinger',
                'price': 13.99,
                'description': 'The story of teenage alienation and loss of innocence.',
                'stock': 7
            },
            {
                'title': 'The Lord of the Rings',
                'author': 'J.R.R. Tolkien',
                'price': 24.99,
                'description': 'An epic high-fantasy novel.',
                'stock': 15
            },
            {
                'title': 'Brave New World',
                'author': 'Aldous Huxley',
                'price': 11.99,
                'description': 'A dystopian social science fiction novel.',
                'stock': 9
            },
            {
                'title': 'Crime and Punishment',
                'author': 'Fyodor Dostoevsky',
                'price': 14.99,
                'description': 'A psychological novel about crime and redemption.',
                'stock': 11
            },
            {
                'title': 'The Brothers Karamazov',
                'author': 'Fyodor Dostoevsky',
                'price': 16.99,
                'description': 'A philosophical novel about faith, doubt, and morality.',
                'stock': 8
            },
            {
                'title': 'War and Peace',
                'author': 'Leo Tolstoy',
                'price': 19.99,
                'description': 'A historical novel about the Napoleonic Wars.',
                'stock': 6
            },
            {
                'title': 'Anna Karenina',
                'author': 'Leo Tolstoy',
                'price': 15.99,
                'description': 'A tragic love story set in Russian high society.',
                'stock': 10
            },
            {
                'title': 'The Odyssey',
                'author': 'Homer',
                'price': 12.99,
                'description': 'An ancient Greek epic poem.',
                'stock': 5
            },
            {
                'title': 'The Iliad',
                'author': 'Homer',
                'price': 12.99,
                'description': 'An ancient Greek epic poem about the Trojan War.',
                'stock': 5
            },
            {
                'title': 'Don Quixote',
                'author': 'Miguel de Cervantes',
                'price': 14.99,
                'description': 'A Spanish novel about a man who believes he is a knight.',
                'stock': 7
            },
            {
                'title': 'Moby-Dick',
                'author': 'Herman Melville',
                'price': 13.99,
                'description': 'A novel about the voyage of the whaling ship Pequod.',
                'stock': 8
            },
            {
                'title': 'The Divine Comedy',
                'author': 'Dante Alighieri',
                'price': 15.99,
                'description': 'An epic poem describing the journey through Hell, Purgatory, and Paradise.',
                'stock': 6
            },
            {
                'title': 'The Canterbury Tales',
                'author': 'Geoffrey Chaucer',
                'price': 12.99,
                'description': 'A collection of stories told by pilgrims on their way to Canterbury.',
                'stock': 4
            },
            {
                'title': 'Les Misérables',
                'author': 'Victor Hugo',
                'price': 16.99,
                'description': 'A French historical novel about justice, redemption, and revolution.',
                'stock': 9
            },
            {
                'title': 'The Count of Monte Cristo',
                'author': 'Alexandre Dumas',
                'price': 14.99,
                'description': 'A tale of revenge and redemption.',
                'stock': 10
            },
            {
                'title': 'The Picture of Dorian Gray',
                'author': 'Oscar Wilde',
                'price': 11.99,
                'description': 'A philosophical novel about beauty, youth, and morality.',
                'stock': 7
            },
            {
                'title': 'Wuthering Heights',
                'author': 'Emily Brontë',
                'price': 12.99,
                'description': 'A story of love and revenge on the Yorkshire moors.',
                'stock': 8
            },
            {
                'title': 'Jane Eyre',
                'author': 'Charlotte Brontë',
                'price': 12.99,
                'description': 'A novel about a young woman\'s journey to independence.',
                'stock': 9
            },
            {
                'title': 'Frankenstein',
                'author': 'Mary Shelley',
                'price': 11.99,
                'description': 'A Gothic novel about the creation of life and its consequences.',
                'stock': 6
            },
            {
                'title': 'Dracula',
                'author': 'Bram Stoker',
                'price': 12.99,
                'description': 'An epistolary novel about the vampire Count Dracula.',
                'stock': 7
            }
        ]
        
        for book_data in sample_books:
            try:
                book = Book.objects.create(**book_data)
                print(f"Created book: {book.title}")
            except Exception as e:
                print(f"Error creating book: {e}")
    
    books = Book.objects.all()
    print(f"Total books in database: {books.count()}")
    return render(request, 'store/home.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'store/book_detail.html', {'book': book})

def search_books(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    
    books = Book.objects.all()
    
    if query:
        books = books.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query)
        )
    
    if category:
        # Add category filtering logic here if needed
        pass
    
    return render(request, 'store/home.html', {
        'books': books,
        'query': query,
        'category': category
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(
            session_key=request.session.session_key,
            user=None
        )
    return cart

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart = get_or_create_cart(request)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book,
        defaults={'quantity': 1}
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

@login_required
def cart(request):
    cart = get_or_create_cart(request)
    cart_items = cart.cartitem_set.all()
    total = cart.get_total()
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')
