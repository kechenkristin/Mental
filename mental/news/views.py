from django.shortcuts import HttpResponse, render


# Create your views here.
def news_board(request):
    url = "https://advanced-emotions-detection-advemotions.p.rapidapi.com/getemotionsnon"

    querystring = {
        "text": "The problem here was almost the opposite of the one I had faced on 37th Street – there were too many cafes. I hardly knew where to start, so I sought guidance from my friend Jaime, who lived a couple of blocks away and who explained that the doughnuts I loved at Delectica came from a place called the Donut Plant and that it distributed its doughnuts to quite a few places, one of which was on the corner of Third and A, opposite Two Boots, the Cajun pizza place that I had been completely obsessed by and utterly dependent on when I lived in New York in the late 80s. They did have the doughnuts at this place on the corner of Third and A but the coffee came in a mug and wasn't so nice. It was too frothy and rather bland. In every other respect this was a perfect neighbourhood: it was full of cool people, there were tonnes of cheap places to eat, and the St Mark's Bookshop was only a five-minute walk away . . . One morning, as I gobbled my doughnut and slurped my coffee, thinking to myself, \"What a fantastic doughnut, what an amazing coffee,\" I realised that I had not just thought this but was actually saying aloud, \"What a fantastic doughnut! What a totally fantastic experience!\", and that this was attracting the attention of the other customers, one of whom turned to me and said, \"You like the doughnuts\""}

    headers = {
        "X-RapidAPI-Key": "5632d5510fmsh11f48e26de7c88dp1a2719jsn6c6c56277791",
        "X-RapidAPI-Host": "advanced-emotions-detection-advemotions.p.rapidapi.com"
    }

    import requests
    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    data = response.json()
    context = {
        'emotions': data
    }

    print(data)

    return render(request, 'news/news_board.html', context)
