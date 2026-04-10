import sys, os, requests, re
sys.path.append(os.getcwd())


class YTCrawlerSettings:
    def __init__(self) -> None:
        # Define the headers to mimic a real browser request
        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

class YTCrawler(YTCrawlerSettings):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url
        # "videoPrimaryInfoRenderer": {
        #     "title": {
        #         "runs": [
        #             {
        #                 "text": "20250711 絕·鐵子的部屋 進擊的鐵屑 極難"
        #             }
        #         ]
        #     }
        # }
        # ...
        # "videoId": ""
        self.regularExpressionRule = r'"videoPrimaryInfoRenderer":{.*?"title":\{"runs":\[\{"text":"(.*?)"\}\]\}.*?"videoId":"(.*?)"'
        self.ytTitle = ""
        self.ytVideoId = ""

    def crawler(self) -> None:
        response = requests.get(self.url, headers=self.HEADERS)
        if response.status_code == 200:
            match = re.search(self.regularExpressionRule, response.text)
            try:
                if match:
                    self.ytTitle = match.group(1)
                    self.ytVideoId = match.group(2)
                else:
                    print("No title found in the JSON response.")
            except Exception as e:
                 print(f"An error occurred while extracting the title: {e}")
        else:
            print(f"Request failed with status code: {response.status_code}")
        print(f"result: \n{self.ytTitle}\n{self.ytVideoId}")


if __name__ == "__main__":
    url = "https://youtu.be/RHtMGP2f7uE?si=d8WLLtitsF8VIKIb"
    YTC = YTCrawler(url)
    YTC.crawler()