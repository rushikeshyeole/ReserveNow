from django.shortcuts import render
from .models import Customer_Table, Customer_Contact_Details, Thali_items

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about.html')

def rooms(request):
    return render(request, 'rooms.html')

def wlc(request):
    return render(request, 'welcome.html')

def COr(request):
    return render(request, "customer.html")

def restaurant(request):
    return render(request, 'restaurant.html')

def Cus_or(request):
    C_n = request.POST['C_name']
    C_t = request.POST['C_time']
    # C_d = "date"
    C_p = request.POST['C_people']

    C_obj = Customer_Table(Cus_name = C_n, Cus_time = C_t, Cus_people = C_p)
    C_obj.save()    

    return render(request, "index.html", {'msg':'Table booked'})


def Cus_Contact_Us(request):
    name = request.POST.get('ccname')
    email = request.POST.get('ccemail')
    msg = request.POST.get('ccmsg')

    C_C_obj = Customer_Contact_Details(Name = name, Email = email, Message = msg)
    C_C_obj.save()

    return render(request, "contact.html", {'msg':'Your Details are Submit'})

def Show_Cus_data(request):
    Obj_Cus_Data = Customer_Table.objects.all()
    return render(request, "Owner.html", {'Obj_Cus_Data':Obj_Cus_Data})


def thali_items_save(request):
    rice = request.POST.get('T_rice')
    G_b = request.POST.get('T_G_Bhaji')
    S_b = request.POST.get('T_S_Bhaji')
    sweet = request.POST.get('T_sweet')

    T_T_Obj = Thali_items(Rice = rice, G_bhaji = G_b, S_bhaji = S_b, Sweet = sweet) 
    T_T_Obj.save()
   
   
    return render(request, "Thali-items.html", {'msg':'Items are added'})

def thali_items_show_owner(request):
    T_O_Items = Thali_items.objects.all()
    return render(request, "Thali-items.html", {'T_O_Items' : T_O_Items})

def thali_items_show(request):
    T_Items = Thali_items.objects.all()
    return render(request, "restaurant.html",  {'T_Items':T_Items})

def thali_items_delete(request):
    T_D_Items = Thali_items.objects.all()
    T_D_Items.delete()
    
    return render(request, 'Thali-items.html')


def Owner(request):
    return render(request, "Owner.html")

def thali_Items(request):
    return render(request, 'Thali-items.html')


def box_co_ch(request):
    return render(request, 'box-color-change.html')
