from flask import Flask, request, redirect, session, url_for, render_template
from newsapi import NewsApiClient
import datetime
import re

app = Flask(__name__)
class News:
    def __init__(self, key):
        self.key = key
        self.newsapi = NewsApiClient(api_key=self.key)

    def get_news_list(self, search, lan="en"):
        news = self.newsapi.get_everything(q=search,
                                        from_param= datetime.date.today() - datetime.timedelta(days=1),
                                        to= datetime.date.today(),
                                        language= lan ,
                                        sort_by='relevancy')

        news_list = []

        for news in news["articles"]:
            if news["title"] == "[Removed]":
                pass
            else:
                news_list.append({"title" : news["title"],
                                "content" : News.remove_chars_marker(news["content"]),
                                "url" : news["url"]})
        return news_list

    @staticmethod
    def remove_html_tags(text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    @staticmethod
    def remove_chars_marker(text):
        pattern = r"\[\+\d+ chars\]"
        cleaned_text = re.sub(pattern, '', text)
        cleaned_text = News.remove_html_tags(cleaned_text)
        return cleaned_text




@app.route("/", methods = ["GET", "POST"])
def index():

    key = AddKeyHere #Add Key Here(NewsApi Key)
    news = News(key)

    if request.method == "POST":
        try:

            if not request.form.get("search").strip():
                return redirect("/")

            if request.form.get("language"):
                list = news.get_news_list(request.form.get("search"), request.form.get("language"))
                return render_template("index.html", news_list = list)
            else:
                list = news.get_news_list(request.form.get("search"))
                return render_template("index.html", news_list = list)
        except:
            return "something went wrong"





    else:
        try:
            return render_template("index.html")
        except:
            return "something went wrong"





