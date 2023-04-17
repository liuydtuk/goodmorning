from pygooglenews import GoogleNews

class MyNews(GoogleNews):
    
    def __init__(self, lang='en'):
        super().__init__(lang)
        
    def get_news_by_top(self, topic='business'):
        try:
            news = self.topic_headlines(topic)
            return self._format_news(news)
        except Exception as e:
            print(e)
            return ""
        
    def _format_news(self, news):
        html_news = "<h2>Today's business headlines:</h2>"
        
        for item in news['entries']:
            
            html_news += "<p>"
            
            html_news += "<strong>" + item["title"] + "</strong><br>"
            html_news += "Published on: " + item["published"] + "<br>"
            html_news += item["link"]
            
            html_news += "</p><hr>"

        return html_news
            





