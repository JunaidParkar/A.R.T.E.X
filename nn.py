import json
import string
from Zubia.Brain.NeuralNetwork.Model import appFinder

appFinder()

file_path = "./AppsList.json"

# def appTokenizer(name: str):
#     token = name.lower().split(" ")
#     return token

# def wordsFilter(apps_list: list, query_app: list):
#     comm = []
#     for index, each_app in enumerate(apps_list):
#         wrd = []
#         for word in query_app:
#             if word.lower() in each_app:
#                 wrd.append(word)
#         comm.append(wrd)
#     return comm

# def wordPercentageCalculator(tokenised_query: list, filtered_query: list):
#     query_length = len(tokenised_query)
#     percentile_list = []
#     for list in filtered_query:
#         list_length = len(list)
#         percentage = (list_length / query_length) * 100
#         percentile_list.append(percentage)
#     if all(num == 0 for num in percentile_list):
#         return [-1]
#     return percentile_list

# def getAppName(name: str):
#     with open(file_path, 'r') as f:
#         apps = json.load(f)
#         tokenised_apps = []
#         tokenised_query = appTokenizer(name)
#         for app in apps:
#             tokenised_apps.append(appTokenizer(app))
#         filtered_word = wordsFilter(tokenised_apps, tokenised_query)
#         percentile = wordPercentageCalculator(tokenised_query, filtered_word)
#         if len(percentile) == 1 and percentile[0] == -1:
#             return False
#         else:
#             maxIndex = percentile.index(max(percentile))
#             return apps[maxIndex]

# while True:
#     nme = input("Enter >> ")
#     try:
#         app_name = getAppName(str(nme))
#         inValid = False
#         for char in nme:
#             if char not in string.ascii_letters and char != " ":
#                 inValid = True
#                 print(char)
#         if inValid:
#             print("Enter query properly...")
#         else:
#             if app_name is False:
#                 print("Your app is not installed...")
#             else:
#                 print(f"opening {app_name}")
#     except:
#         print("Enter query properly...")