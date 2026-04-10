import os, datetime
from typing import List
from scripts.utils.jsonController import JsonController
from scripts.utils.ytCrawler import YTCrawler


class JsonBuilder():
    def __init__(self, root: List[str], tags: List[str], file_name: str) -> None:
        # Path 
        self.folder_path = self.setFolderPath(root, tags)
        self.file_name = file_name
        self.full_path = self.setFullPath()
        # Json Controller
        self.jsonController = JsonController()
        # tags 
        self.tags = tags

    def setFolderPath(self, root: List[str], tags: List[str]) -> str:
        folder_path = ""
        for f in root + tags:
            folder_path = os.path.join(folder_path, f)
        return folder_path
    
    def setFullPath(self) -> str:
        full_path = os.path.join(self.folder_path, self.file_name)
        return f"{full_path}.json"
    
    # 更新 
    def update(self, json_data, title, description, url, video_insert_index=None) -> None:
        # video crawler: title, id
        yt_crawler = YTCrawler(url)
        yt_crawler.crawler()
        # get video_label, video_id
        video_label = ' '.join(yt_crawler.ytTitle.split()[1:])
        video_id =  yt_crawler.ytVideoId
        print()
        if json_data == {}:
            json_data = {
                "title": title,
                "description": description,
                "videos": [
                    {
                        "label": video_label,
                        "id": video_id
                    }
                ], 
                "tags": self.tags, 
                "years": [
                    datetime.datetime.now().year
                ]
            }
            self.jsonController.jsonWriter(self.full_path, json_data)
        else:
            # video 
            new_video = {
                "label": video_label,
                "id": video_id
            }
            if new_video not in json_data["videos"]:
                if video_insert_index == None and video_insert_index > len(json_data["videos"]):
                    json_data["videos"].append(new_video)
                else:
                    json_data["videos"].insert(video_insert_index, new_video)
                # year
                new_year = datetime.datetime.now().year
                if new_year not in json_data["years"]:
                    json_data["years"].append(new_year)
                self.jsonController.jsonWriter(self.full_path, json_data)
            else:
                print(f"the video exists. pass {self.full_path}")

    def check(self) -> None:
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        if not os.path.exists(self.full_path):
            self.jsonController.jsonWriter(self.full_path, {})

    def builder(self, title, description, url, video_insert_index) -> None:
        self.check()
        data = self.jsonController.jsonReader(self.full_path)
        self.update(data, title, description, url, video_insert_index)


def main(
        tags: List[str], file_name: str, 
        title: str, description: str, url: str, video_insert_index: int
    ) -> None:
    # folder path 
    root = ["public", "json", "categories"]
    full_path = ""
    for p in root + tags:
        full_path = os.path.join(full_path, p)
    print(full_path)

    JB = JsonBuilder(root, tags, file_name)
    JB.builder(title, description, url, video_insert_index)

    data = JB.jsonController.jsonReader(JB.full_path)
    JB.jsonController.jsonViewer(data)


if __name__ == "__main__":
    # parent folders + file name
    tags = [
        "game", "theBattleCats", "catFruit"
    ]
    file_name = "manicCat"

    # json 
    title = "大狂亂貓咪"
    description = "紀錄 貓咪大戰爭 🐾 的地方 🐾🐾"
    url = "https://youtu.be/WSLufl_qA6I?si=q6H0Upl2hWpZ5gg5"
    video_insert_index = 3

    main(tags, file_name, title, description, url, video_insert_index)
