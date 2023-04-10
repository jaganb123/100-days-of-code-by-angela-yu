from bs4 import BeautifulSoup
import requests, json

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
bestMovie100 = response.text

soup = BeautifulSoup(bestMovie100, "html.parser")

# with open("100_best_movies.html", "w") as file:
#     file.write(soup.prettify())

# def search_movie_name(tag):
#     return tag.has

def format_movie_name(name):
    # print(name)
    list1 = name.split()
    # print(list1)
    print(list1[1:])
    movie_name = " ".join(list1[1:])
    movie_name.join(" ")
    movie_rank = int(list1[0].split(")")[0])
    movie_rank_str = list1[0]
    return movie_rank, movie_rank_str, movie_name


tags = soup.find("script", id="__NEXT_DATA__").string
json_doc = json.loads(tags)
for obj in json_doc["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"]:        
    if obj["content"]["title"] == "100 Greatest Movies 2022":
        # print(obj['content'].keys())
        movie_list = []
        for movie_name in obj["content"]["images"]:
            # print(movie_name)
            movie_list.append(format_movie_name(movie_name['titleText']))


def sort_func(e):
    return e[0]
movie_list.sort(reverse=False, key=sort_func)
movie_string = "\n".join([f"{name[1]} {name[2]}" for name in movie_list])


with open("movie_list.txt", "w") as file:
    file.write(movie_string)






# tag = [ tag for tag in soup.select("h3.jsx-4245974604")]
# print(tag)