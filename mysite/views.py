from django.contrib.auth.models import User, Group

from mysite.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render 


from django.http import HttpResponse, HttpResponseNotFound, JsonResponse

from django.views.decorators.http import require_http_methods    
from django.template import loader  
import requests
import  mysite.helpers

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions

from mysite.forms import StudentForm  



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



from .serializers import YourSerializer


class YourView(APIView):
    @permission_classes((permissions.AllowAny,))
    def get(self, request):
        yourdata= [{"likes": 10, "comments": 0}, {"likes": 4, "comments": 23}]
        results = YourSerializer(yourdata, many=True).data
        queryset = Group.objects.all()
    
        permission_classes = [permissions.IsAuthenticated]
        return Response(results)


class MyOwnView(APIView):
 
    def get(self,request):
        
        if request.method == 'GET':
            data = {'test':'test'}
            permission_classes = [permissions.IsAuthenticated]

            return Response(data)



@require_http_methods(["POST"])    
def send_json(request):
  
    #data = mysite.helpers.GetProductFromJS(request.POST.get("upc").replace("'",""))
    data = mysite.helpers.GetProductResults(request.META.get("REMOTE_ADDR"))
    return JsonResponse(data, safe=False)


@require_http_methods(["GET"])    
def getproduct(request,id):
    data = mysite.helpers.GetProductData(id,request.META.get("REMOTE_ADDR"))
    return render(request,"index-0.1.1.html",data)  





@require_http_methods(["GET","POST"])    
def index(request,asin):
    
    data = ""
    student = ""
    allUPCS = ""
    method = ""

    if request.method == 'POST':
        method = "POST"
        try:
            if request.FILES is not None: 
                student = StudentForm(request.POST, request.FILES)  
                if student.is_valid():  
                    allUPCS = mysite.helpers.handle_uploaded_file(request.FILES['file'],request.META.get("REMOTE_ADDR")) 
        except Exception as ee:
            print(ee)

    else:
        method = "GET"
        student = StudentForm()  
        session = requests.Session()
        session.auth = ("admin", "123wet123")
        data = {}
        #data = mysite.helpers.RetrieveProducts()
        data = mysite.helpers.GetProduct(asin)



    thedata = {
        'data':data,
        'form':student,
        'allUPCS':allUPCS,
        'method':method
    }


    #response = session.get('http://localhost:8000/users')
    #print(response.text)


    template = loader.get_template('index-0.1.1.html') # getting our template  
    
    return render(request,"test.html",thedata)  
    #return HttpResponse(template.render(thedata))       # rendering the template in HttpResponse  