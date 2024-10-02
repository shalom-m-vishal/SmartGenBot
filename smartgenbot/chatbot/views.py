from django.shortcuts import render
from .models import Chat
from django.http import JsonResponse
import nltk
from nltk.tokenize import word_tokenize

# A simple knowledge base for responses
knowledge_base = {
    "hello": "Welcome to SmartGenBot,your programming assistant for mastering coding concepts and Data Structures & Alogrithms.",
    "sorting": "Sorting is the process of arranging data in a particular order.",
    "algorithms": "An algorithm is a step-by-step procedure to solve a problem.",
    "data-structures": "Data structures are used to store and organize data efficiently."
}

def chatbot(request):
    return render(request, 'index.html')

def get_response(request):
    user_input = request.GET.get('user_input', '')

    # Tokenize user input
    tokens = word_tokenize(user_input.lower())
    
    # Find a response from the knowledge base
    response = "I'm sorry, I don't understand your question."
    for word in tokens:
        if word in knowledge_base:
            response = knowledge_base[word]
            break

    # Save the chat to the database
    chat = Chat(user=request.user if request.user.is_authenticated else None, user_input=user_input, bot_response=response)
    
    # Make sure to call save() to commit the data to the database
    chat.save()

    return JsonResponse({'response': response})