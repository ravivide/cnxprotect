# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect

from CNXProtect_Utl.models import Customer
from .decorators import unauthenticated_user
# Create your views here.
from .forms import CreateUserForm
from webpage.decorators import unauthenticated_user, allowed_users#, admin_only


#@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='CNX_Internal_User')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'CNXProtect_Utl/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('indexing_data5')
        else:
            messages.info(request, 'You are not Authorized to access')
            return redirect('login')
    else:
        #messages.info(request, 'Incorrect User Name or Password')
        return render(request, 'CNXProtect_Utl/login.html')
        #return redirect('login')


# def userPage(request):
#     context = {}
#     return render(request, 'CNXProtect_Utl/index.html', context)


# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']
#
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'Uses Name already created!')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already taken!')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password1, email=email,
#                                                 first_name=first_name, last_name=last_name)
#                 user.save()
#                 messages.info(request, 'User account created!')
#                 return redirect('login')
#         else:
#             messages.info(request, 'Password not Matching')
#             return redirect('register')
#         return redirect('/')
#     else:
#         return render(request, 'CNXProtect_Utl/register.html')

#
# @unauthenticated_user
# def register(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#
#             group = Group.objects.get(name='customer')
#             user.groups.add(group)
#
#             messages.success(request, 'Account was created for ' + username)
#
#             return redirect('login')
#
#     context = {'form': form}
#     return render(request, 'accounts/register.html', context)
# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    # orders = customer.order_set.all()
    # order_count = orders.count()
    #
    # myFilter = OrderFilter(request.GET, queryset=orders)
    # orders = myFilter.qs
    #
    # context = {'customer': customer, 'orders': orders, 'order_count': order_count,
    #            'myFilter': myFilter}
    return render(request, 'CNXProtect_Utl/index.html', context)
