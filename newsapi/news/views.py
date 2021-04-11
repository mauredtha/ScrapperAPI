import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from bs4 import BeautifulSoup as BSoup
from news.models import Headline

from rest_framework import generics, filters
from rest_framework import status
from rest_framework.response import Response

from .serializers import HeadlineSerializer

# Create your views here.
def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://lite.cnn.com"

    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find('ul').find_all('li')
    for article in News:
        main = article.find_all('a')[0]
        link = main['href']
        title = main.text
        try:
            new_headline = Headline()
            new_headline.title = title
            new_headline.url = url + link
            new_headline.save()
            return HttpResponse("Success Scrapping Data")
        except e as Exception:
            return HttpResponse(f"Failed {e}")
    #return redirect("../")

def custom404(request, exception=None):
    return Response({"message": "The resource was not found", "status":status.HTTP_404_NOT_FOUND})

class CreateView(generics.ListCreateAPIView):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer
    def perform_create(self, serializer):
        try:
            serializer.save()
            custom_data = {
                "statusCode": status.HTTP_201_CREATED,
                'data': serializer.data,  # this is the default result you are getting today
                "successMessages": "Success Add Data",
                "errorMessage": "",
            }
            return Response(custom_data) 
        except Exception as e:
            return Response({"statusCode":status.HTTP_409_CONFLICT, "data":serializer.errors, "successMessage": "", "errorMessage": "Terjadi Kesalahan" })

class ListHeadlineView(generics.ListAPIView):
    #queryset = Headline.objects.all() # used for returning objects from this view
    serializer_class = HeadlineSerializer
    def get_queryset(self):
        queryset = Headline.objects.all()
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(title__contains=search)
        return queryset
    
    def list(self, request, *args, **kwargs):
        try :
            if HeadlineSerializer(self.get_queryset(),many=True).data :
                custom_data = {
                    "statusCode": status.HTTP_200_OK,
                    'data': HeadlineSerializer(self.get_queryset(),many=True).data,
                    "successMessage": "Success Load Data",
                    "errorMessage": "",
                }
                return Response(custom_data)
            return Response({"statusCode":status.HTTP_204_NO_CONTENT, "data":"", "successMessage": "", "errorMessage": "No Content" })
        except e as Exception:
            return Response({"statusCode":status.HTTP_404_NOT_FOUND, "data":"", "successMessage": "", "errorMessage": "The resource was not found"})

class HeadlineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer

    def retrieve(self, request, pk=None):
        try :
            queryset = Headline.objects.all()
            cpu = get_object_or_404(queryset, pk=pk)
            serializer = HeadlineSerializer(cpu)
            return Response({"statusCode":status.HTTP_200_OK, "data":serializer.data, "successMessage": "Success", "errorMessage": "" })
        except Exception:    
            return Response({"statusCode":status.HTTP_204_NO_CONTENT, "data":"", "successMessage": "", "errorMessage": "No Content" })

    def list(self, request, *args, **kwargs):
        try :
            if HeadlineSerializer(self.get_queryset(),many=True).data :
                custom_data = {
                    "statusCode": status.HTTP_200_OK,
                    'data': HeadlineSerializer(self.get_queryset(),many=True).data,
                    "successMessages": "Success",
                    "errorMessage": "",
                }
                return Response(custom_data)
            return Response({"statusCode":status.HTTP_400_BAD_REQUEST, "data":"", "successMessage": "", "errorMessage": "Terjadi Kesalahan" })
        except e as Exception:
            return Response({"statusCode":status.HTTP_404_NOT_FOUND, "data":"", "successMessage": "", "errorMessage": "The resource was not found" })

    def update(self, request, *args, **kwargs):
        try :
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            custom_data = {
                "statusCode": status.HTTP_200_OK,
                'data': serializer.data,  # this is the default result you are getting today
                "successMessages": "Success Updated Data",
                "errorMessage": "",
            }
            return Response(custom_data) 
        except Exception as e:
            return Response({"statusCode":status.HTTP_409_CONFLICT, "data":serializer.errors, "successMessage": "", "errorMessage": "Terjadi Kesalahan" })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"statusCode":status.HTTP_200_OK, "data":"", "successMessage": "Success Delete Data", "errorMessage": "" })


        