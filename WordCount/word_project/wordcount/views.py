from django.shortcuts import render

def home(request):
    return render(request,'wordcount/home.html')

def about(request): 
    return render(request, 'wordcount/about.html')

def result(request):
    text = request.GET['fulltext']
    words=text.split()
    space_word={}
    for word in words:
        if word in space_word:
            # 있던단어가 또 있으면 1증가 시켜라
            space_word[word]+=1
        else:
        # 새로운 단어면 1 증가
            space_word[word]=1   

    return render(request, 'wordcount/result.html', {'all_text' : text,'len_words':len(words),'word_dictionary':space_word.items()})