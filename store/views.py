from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .models import Book, Cart, CartItem
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from decimal import Decimal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context['books'] = books
        return context

class BookSearchView(ListView):
    model = Book
    template_name = 'store/home.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = Book.objects.all()
        query = self.request.GET.get('q', '')
        category = self.request.GET.get('category', '')
        
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(author__icontains=query)
            )
        
        if category:
            # Add category filtering logic here if needed
            pass
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['category'] = self.request.GET.get('category', '')
        return context

class BookListView(ListView):
    model = Book
    template_name = 'store/book_list.html'
    context_object_name = 'books'
    paginate_by = 12

    def get_queryset(self):
        queryset = Book.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(author__icontains=query)
            )
        return queryset

class BookDetailView(DetailView):
    model = Book
    template_name = 'store/book_detail.html'
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    template_name = 'store/book_form.html'
    fields = ['title', 'author', 'description', 'price', 'stock', 'cover_image']
    success_url = reverse_lazy('store:book_list')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, 'Book added successfully!')
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    template_name = 'store/book_form.html'
    fields = ['title', 'author', 'description', 'price', 'stock', 'cover_image']
    success_url = reverse_lazy('store:book_list')

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, 'Book updated successfully!')
        return super().form_valid(form)

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'store/book_confirm_delete.html'
    success_url = reverse_lazy('store:book_list')

    def test_func(self):
        return self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Book deleted successfully!')
        return super().delete(request, *args, **kwargs)

class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'store/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})
        
        # Get all books in the cart
        books = {str(book.id): book for book in Book.objects.filter(id__in=cart.keys())}
        
        # Calculate totals
        subtotal = sum(
            Decimal(str(book.price)) * Decimal(str(quantity))
            for book_id, quantity in cart.items()
            if book_id in books
        )
        tax = subtotal * Decimal('0.10')  # 10% tax
        total = subtotal + tax
        
        context.update({
            'cart_items': cart,
            'books': books,
            'subtotal': subtotal,
            'tax': tax,
            'total': total,
        })
        return context

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        cart = request.session.get('cart', {})
        
        if str(pk) in cart:
            cart[str(pk)] += 1
        else:
            cart[str(pk)] = 1
        
        request.session['cart'] = cart
        messages.success(request, f'{book.title} added to cart!')
        return redirect('store:book_detail', pk=pk)

class RemoveFromCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        if str(pk) in cart:
            del cart[str(pk)]
            request.session['cart'] = cart
            messages.success(request, 'Item removed from cart!')
        
        return redirect('store:cart_view')

class UpdateCartView(LoginRequiredMixin, View):
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart[str(pk)] = quantity
        else:
            del cart[str(pk)]
        
        request.session['cart'] = cart
        return redirect('store:cart_view')

class RegisterView(FormView):
    template_name = 'store/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('store:book_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, 'Registration successful!')
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'store:book_list'
