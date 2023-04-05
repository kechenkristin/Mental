from django.shortcuts import HttpResponse, render


# Create your views here.
def news_board(request):
    import requests

    url = "https://motivational-quotes-quotable-api.p.rapidapi.com/motivational_quotes"

    headers = {
        "X-RapidAPI-Key": "5632d5510fmsh11f48e26de7c88dp1a2719jsn6c6c56277791",
        "X-RapidAPI-Host": "motivational-quotes-quotable-api.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    print(response.json())
    data = response.json()

    new_data_list = []

    for key, value in data.items():
            new_data_list.append(value)

    context = {
        'text':new_data_list
    }

    return render(request, 'news/news_board.html', context)
