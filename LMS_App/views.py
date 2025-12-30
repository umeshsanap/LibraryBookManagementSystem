from django.shortcuts import render
from LMS_App.models import Book
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def add_book(request):
    if request.method=="POST":
        data= json.loads(request.body)
        book=Book.objects.create(
            title=data.get("title"),
            author=data.get("author"),
            quantity=data.get("quantity")
            
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
            queryset=Book.objects.get(id==id)
            data=json.loads(request.body)
            queryset.title=data.get("title")   
            queryset.author=data.get("author")
            queryset.quantity=data.get("quantity")  
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
                "quantity":queryset.quantity
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