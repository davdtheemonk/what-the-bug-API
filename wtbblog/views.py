from rest_framework import generics,permissions
from .models import Post
from .serializers import PostSerializer,ModulesSerializer
from django.http import JsonResponse
from .models import Post,modules
from django.shortcuts import render
from braces import views
from django.views.generic import View

class PostList(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all()
    serializer_class = PostSerializer

class ModuleList(generics.ListCreateAPIView):
	queryset = modules.objects.all()
	serializer_class = ModulesSerializer

class ModulePost(generics.RetrieveUpdateDestroyAPIView):
	queryset = modules.objects.all()
	permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
	serializer_class = ModulesSerializer

def home(request):
	return render(request, 'home/home.html')



def get_Data(request,pk):
	results = []
	try:
		if request.method == 'GET':
			query_id=int(pk)
			post = Post.objects.get(pk=pk)
			val ={'id':post.pk,'title':post.title,'date':post.date,'location':post.location,'timetoread':post.timetoread
			,'image_url':post.image,'post':post.post}
			results.append(val)
			return JsonResponse(results, content_type='application/json',
			safe=False)
		else:
			val = {'error': "Request not allowed.See documentation"}
			results.append(val)
			return JsonResponse(results,content_type='application/json',safe=False)
	except Exception as e:
		val = {'error':'An error occured fetching data'}
		results.append(val)
		JsonResponse(results,content_type='application/json',safe=False)
		raise e

def getDataJson(request):
	results = []

	try:
		queryset = Post.objects.filter().values()
		return JsonResponse({"models_to_return": list(queryset)})		
	except Exception as e:
		raise e