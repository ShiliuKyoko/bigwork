from Tadmin.models import Article
from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ArticleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=1)
    class Meta:
        model = Article
        fields = '__all__'

@api_view(['GET','POST'])
def a_article_list(request):
    if request.method == 'GET':
        article_1 = Article.objects.order_by('-id') #order_by('-id')
        serializer =ArticleSerializer(article_1,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        body = {
            'body': serializer.errors,
            'msg': '40001'
        }
        return Response(body, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE','GET','POST'])
def a_article_info(request,id):
    article = Article.objects.get(id=id)
    if request.method == 'GET':
        # article_1 = Article.objects.order_by('-id') #order_by('-id')
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        body = {
            'body': serializer.errors,
            'msg': '40001'
        }
        return Response(body, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response({'msg': 'A-OK'}, status=status.HTTP_201_CREATED)
