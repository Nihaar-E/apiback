from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FAQ
from .serializers import FAQSerializer
from asgiref.sync import async_to_sync

@api_view(['GET', 'POST'])
def all_faqs(request):
    if request.method == "GET":
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()

        serialized_data = []
        for faq in faqs:
            question_translation = async_to_sync(faq.get_translation)(lang, 'question')
            answer_translation = async_to_sync(faq.get_translation)(lang, 'answer')
            faq_data = {
                'question': question_translation,
                'answer': answer_translation
            }
            serialized_data.append(faq_data)

        return Response(serialized_data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def specific_faq(request, pk):
    try:
        faq = FAQ.objects.get(pk=pk)
    except FAQ.DoesNotExist:
        return Response({"error": "FAQ not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        lang = request.GET.get("lang", "en")
        question_translation = async_to_sync(faq.get_translation)(lang, 'question')
        answer_translation = async_to_sync(faq.get_translation)(lang, 'answer')
        faq_data = {
            'question': question_translation,
            'answer': answer_translation
        }
        return Response(faq_data)

    elif request.method == "PUT":
        serializer = FAQSerializer(faq, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        faq.delete()
        return Response({"message": "FAQ deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
