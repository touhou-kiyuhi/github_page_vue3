import os, datetime, re
from typing import List, Dict, Any
from scripts.utils.jsonController import JsonController


class PortfolioJsonManager:
    def __init__(self, root: List[str], folders: List[str]):
        # Path 
        self.folder_path = self.setFolderPath(root, folders)
        self.file_name = folders[-1] + "Portfolio"
        self.full_path = self.setFullPath()
        # Json Controller
        self.jsonController = JsonController()
        self.folders = folders

    def setFolderPath(self, root: List[str], folders: List[str]) -> str:
        folder_path = ""
        for f in root + folders:
            folder_path = os.path.join(folder_path, f)
        return folder_path
    
    def setFullPath(self) -> str:
        full_path = os.path.join(self.folder_path, self.file_name)
        return f"{full_path}.json"
    
    # 所有在 current_root 下的 .json
    def traversal(self):
        for dirpath, dirnames, filenames in os.walk(self.folder_path):
            for filename in filenames:
                # 篩選
                if filename.endswith(".json") and filename[-14:-5] != "Portfolio":
                    # Portfolio Json
                    json_data = self.jsonController.jsonReader(self.full_path)
                    # Currebt Post Json
                    post_json_path = os.path.join(dirpath, filename)
                    print(post_json_path)
                    post_json_data = self.jsonController.jsonReader(post_json_path)
                    self.update(json_data, post_json_data, filename)

    def split_camel(self, text):
        return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

    # 更新
    def update(self, json_data: Dict[str, Any], post_json_data: Dict[str, Any], filename):
        new_post = {
            "id": filename[:-5], 
            "name": post_json_data["title"], 
            "tags": post_json_data["tags"], 
            "years": post_json_data["years"]
        }
        tagList = []
        for tag in post_json_data["tags"]:
            tagList.append(
                {
                    "id": tag, 
                    "name": self.split_camel(tag)
                }
            )
        if json_data == {}:
            json_data = {
                "tagList": tagList,
                "yearList": post_json_data["years"],
                "postList": [
                    new_post
                ]
            }
            self.jsonController.jsonWriter(self.full_path, json_data)
        else:
            if new_post not in json_data["postList"]:
                json_data["postList"].append(new_post)
                # 檢查重複元素
                for tag in post_json_data["tags"]:
                    tag_dict = {
                        "id": tag, 
                        "name": self.split_camel(tag)
                    }
                    if tag_dict not in json_data["tagList"]:
                        json_data["tagList"].append(tag_dict)
                # year
                new_year = datetime.datetime.now().year
                if new_year not in json_data["yearList"]:
                    json_data["yearList"].append(new_year)
                self.jsonController.jsonWriter(self.full_path, json_data)
            else:
                print(f"the post exists. pass {new_post["id"]}")

    def check(self) -> None:
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        if not os.path.exists(self.full_path):
            self.jsonController.jsonWriter(self.full_path, {})

    def builder(self):
        self.check()
        self.traversal()

        data = self.jsonController.jsonReader(self.full_path)
        self.jsonController.jsonViewer(data)


def main():
    # file path 
    root = ["public", "json", "categories"]
    folders = [
        "game", "theBattleCats"
    ]
    PJM = PortfolioJsonManager(root, folders)
    PJM.builder()


if __name__ == "__main__":
    main()
