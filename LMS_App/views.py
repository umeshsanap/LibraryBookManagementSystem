from django.shortcuts import render
from LMS_App.models import Book,Register
import json
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password,make_password
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def Librarian_registration(request):
    if request.method=="POST":
        data=json.loads(request.body)
        email=data.get("email")
        if Register.objects.filter(email=email).exists():
            return JsonResponse(
                {
                    "message":"Email already Exits..!"
                }
            )
        Register.objects.create(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                email=data.get("email"),
                password=make_password(data.get("password")),
                phone_number=data.get("phone_number"),
                designation = data.get("designation"),
                role = data.get("role"),
                is_active = data.get("is_active"),
                created_at = data.get("created_at"),
                updated_at = data.get("updated_at")
                
        )
        return JsonResponse(
            {
                "Message":"Librarian resistered Successfully..!"
            }
        )
    return JsonResponse(
            {
                "error":"You choose Wrong Method"
            }
            )
    
@csrf_exempt
def Librarian_login(request):
    if request.method=="POST":
        data=json.loads(request.body)
        email=data.get("email")
        password=data.get("password")
        
        try:
            queryset=Register.objects.get(email=email)
            
            if check_password(password, queryset.password):
                return JsonResponse(
                {
                    "message":"Login successfully...!",
                    "ID":queryset.id                    
                    
                }
            )
            else:
                return JsonResponse(
                    {
                        "error":"Invalid Password"
                    }
                )
        except Register.DoesNotExist:
            return JsonResponse(
                {
                    "Error":"Data NOT Found"
                }
            )
    else:
        return JsonResponse(
            {
                "Error":"You Choose Wrong Method"
            }
        )
        
        


@csrf_exempt
def add_book(request):
    if request.method=="POST":
        data= json.loads(request.body)
        book=Book.objects.create(
            title=data.get("title"),
            author=data.get("author"),
            quantity=data.get("quantity"),
            total_copies=data.get("total_copies"),
            available_copies=data.get("available_copies"),
            price=data.get("price"),
            status=data.get("status"),
            publisher=data.get("publisher")    
        )
        return JsonResponse(
            {
                "Message":"Book Added",
                "id":book.id
            }
        )
        
    else:
        return JsonResponse(
            {
                "error":"Wrong method choosed"
            }
        )
        
        
@csrf_exempt
def update_book(request,id):
    if request.method=="PUT":
        try:
            queryset=Book.objects.get(id=id)
            data=json.loads(request.body)
            queryset.title=data.get("title")   
            queryset.author=data.get("author")
            queryset.quantity=data.get("quantity") 
            queryset.total_copies=data.get("total_copies")
            queryset.available_copies=data.get("available_copies")
            queryset.price=data.get("price")
            queryset.status=data.get("status")
            queryset.publisher=data.get("publisher") 
            
            queryset.save()
            return JsonResponse(
                {
                    "message":"Book update Successfully.."
                },
                status=200
            )   
        except Exception as e:
            return JsonResponse(
                {
                    "Error":"Data NOT Found"
                },
                status=404
            )
    else:
        return JsonResponse(
            {
                "error":"Choosed Wrong Method"
            }
        )
        
@csrf_exempt
def delete_book(request,id):
    if request.method=="DELETE":
        try:
            queryset= Book.objects.get(id=id)
            queryset.delete()
            return JsonResponse(
                {
                    "message":"Book delete successfully.."
                },
                status=200
            )
        except Exception as e:
            return JsonResponse(
                {
                    "error":"data not found"
                },
                status=404
            )
    else:
        return JsonResponse(
            {
                "error":"you choose wrong method"
            }
        )
           
            
@csrf_exempt
def search_book(request, title):
    try:
        queryset = Book.objects.get(title=title )
        return JsonResponse(
            {
                "id":queryset.id,
                "title":queryset.title,
                "author":queryset.author,
                "quantity":queryset.quantity,
                "total_copies":queryset.total_copies,
                "available_copies":queryset.available_copies,
                "price":queryset.price,
                "status":queryset.status,
                "publisher":queryset.publisher    
            },
            status = 200
        )
    except Exception as e:
        return JsonResponse(
            {
                "error":"Data not found..!"
            },
            status = 404
        )