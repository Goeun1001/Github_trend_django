from rest_framework.decorators import api_view
from rest_framework.response import Response
from Repository.models import Repository
from Language.models import Language
from Topic.models import Topic
import requests


# id = models.AutoField(primary_key=True)
# url = models.CharField(max_length=100)
# name = models.CharField(max_length=50)
# desc = models.CharField(max_length=200)
# star = models.IntegerField()
# language = models.ForeignKey(Language, on_delete=models.CASCADE)


@api_view(['GET'])
def getJson(request):
    since = 309500 # change the number what you want.
    for i in range(1, 10000):
        since += 500
        getRepositoryURL = 'https://api.github.com/repositories?since='
        current_token: str = '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'
        first_token = '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' # 고은
        second_token = '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' # 정민
        third_token = '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' # 종은
        final_token = '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' # 태희
        headers = {'Authorization': 'token ' + current_token,
                   'Accept': 'application/vnd.github.mercy-preview+json'}

        repository = requests.get(getRepositoryURL + str(since), headers=headers, )
        json = repository.json()

        if type(json) is not list:
            print(json)
            if current_token == first_token:
                current_token = second_token
                repository = requests.get(getRepositoryURL + str(since), headers=headers, )
                json = repository.json()
            elif current_token == second_token:
                current_token = third_token
                repository = requests.get(getRepositoryURL + str(since), headers=headers, )
                json = repository.json()
            elif current_token == third_token:
                current_token = final_token
                repository = requests.get(getRepositoryURL + str(since), headers=headers, )
                json = repository.json()
            elif current_token == final_token:
                current_token = first_token
                repository = requests.get(getRepositoryURL + str(since), headers=headers, )
                json = repository.json()

        for n in json:
            print(n["id"])
            user = requests.get(n["url"], headers=headers)
            userJson = user.json()
            if userJson.get("language"):
                print(userJson["language"])
                print(userJson["created_at"])
                try:
                    lang = Language.objects.get(language=userJson["language"])
                    lang.count = lang.count + 1
                    lang.save()
                except Language.DoesNotExist:
                    Language.objects.create(language=userJson["language"], count=1)

                try:
                    repo = Repository.objects.get(url=userJson["url"])
                except Repository.DoesNotExist:
                    Repository.objects.create(url=userJson["url"],
                                              name=userJson["name"],
                                              desc=userJson["description"],
                                              star=-userJson["stargazers_count"],
                                              language=Language.objects.get(language=userJson["language"]),
                                              created_at=userJson["created_at"])

            topics = requests.get(n["url"] + "/topics", headers=headers)
            topicJson = topics.json()

            if topicJson.get("names"):
                print(topicJson["names"])
                for i in topicJson["names"]:
                    print(i)
                    try:
                        top = Topic.objects.get(name=i)
                        top.count = top.count + 1
                        top.save()
                    except Topic.DoesNotExist:
                        if userJson["language"]:
                            Topic.objects.create(name=i, count=1,
                                                 language=Language.objects.get(language=userJson["language"]))
                        else:
                            continue

    return Response({"success": "1"})


@api_view(['GET'])
def getYear(request):
    return Response({"years": [2008, 2009]})
