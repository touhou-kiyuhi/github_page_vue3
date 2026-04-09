import sys, os, datetime
sys.path.append(os.getcwd())
from tools.settings.jsonSettings_abstract import JsonSettings
from tools.jsonClasses.jsonFileManager_abstract import JsonFileManager
from tools.ytCrawler.ytCrawler_abstract import YTCrawler


class CategoriesContentBuilder(JsonSettings):
    def __init__(self, parentPath, folder, fileName, jsonTitle, description, data):
        super().__init__()
        # Path 
        self.jsonFileManager = JsonFileManager(parentPath, folder, fileName)

        self.jsonTitle = jsonTitle
        self.description = description
        self.data = data

    # 更新 
    def update(self, data, index=None):
        if data == {}:
            # HTML 路徑
            pageLink = "/pages/" + '/'.join(self.jsonFileManager.filePath.split('/')[2:])[:-5] + ".html"
            print(self.jsonFileManager.filePath, pageLink)
            # 標籤
            tags = self.jsonFileManager.folderPath.split('/')[3:]
            # 該資料
            data = {
                "title": self.jsonTitle,
                "description": self.description,
                "data": self.data,
                "page": pageLink,
                "tags": tags,
                "year": datetime.datetime.now().year
            }
        else:
            
            if self.data[0]["title"] not in [data["data"][i]["title"] for i in range(len(data["data"]))]:
                data["data"].append(self.data[0])
            else:
                print("the json already exists")
        self.jsonController.jsonWriter(self.jsonFileManager.filePath, data)

    def builder(self, index=None):
        self.jsonFileManager.check()
        data = self.jsonController.jsonReader(self.jsonFileManager.filePath)
        self.update(data, index)


def main(
        category, directory, parentPathList, folder, fileName,
        jsonTitle, description, data
    ):
    parentPath = ""
    for p in [category, directory] + parentPathList:
        if p == "":
            break
        parentPath = os.path.join(parentPath, p)
    CCB = CategoriesContentBuilder(parentPath, folder, fileName, jsonTitle, description, data)
    CCB.builder()

    data = CCB.jsonController.jsonReader(CCB.jsonFileManager.filePath)
    CCB.jsonController.jsonViewer(data)


if __name__ == "__main__":
    category = "coding"
    directory = "dataStructure"
    parentPathList = [
        "linkedList"
    ]
    folder = "singleLinkedList"
    fileName = "singleLinkedList"

    jsonTitle = "資料結構：Single Linked List"
    description = "紀錄 資料結構 🐾 的地方 🐾🐾"
    data = [
        {
            "title": "Learn single linked list in Ruby",
            "description": {
                "node": {
                    "theme": "Class: `ListNode`",
                    "description": "Represents a single node in a singly linked list."
                },
                "dataStructure": {
                    "theme": "Class: `SingleLinkedList`",
                    "description": "Implements a singly linked list with common list operations.",
                    "methods": [
                        {
                            "method": "`append_node(data)`",
                            "description": "Adds a new node containing `data` to the end of the linked list."
                        },
                        {
                            "method": "`insert_node(data, index)`",
                            "description": "Inserts a new node with `data` at the specified `index`. Raises `IndexError` if the index is invalid."
                        },
                        {
                            "method": "`get_node_by_index(index)`",
                            "description": "Returns the node at the specified index. Raises `IndexError` if the index is out of range."
                        },
                        {
                            "method": "`find_node(data)`",
                            "description": "Searches for the first node containing `data` and returns its index. Returns `nil` if not found."
                        },
                        {
                            "method": "`update_node(data, index)`",
                            "description": "Updates the value of the node at the specified index. Raises `IndexError` if the index is invalid."
                        },
                        {
                            "method": "`delete_node(index)`",
                            "description": "Deletes the node at the specified index. Raises `IndexError` if the index is out of range."
                        },
                        {
                            "method": "`reverse_linked_list()`",
                            "description": "Reverses the entire linked list in place. Raises `ArgumentError` if the list is empty."
                        },
                        {
                            "method": "`clear()`",
                            "description": "Removes all nodes from the linked list."
                        },
                        {
                            "method": "`length()` / `size()`",
                            "description": "Returns the number of nodes in the linked list."
                        },
                        {
                            "method": "`[](index)`",
                            "description": "Returns the value of the node at the specified `index`. Supports negative indices."
                        },
                        {
                            "method": "`[]=(index, data)`",
                            "description": "Updates the value of the node at the specified `index` using array-style assignment."
                        },
                        {
                            "method": "`each()`",
                            "description": "Iterates through each node in the linked list and yields its value. Enables `Enumerable` methods."
                        },
                        {
                            "method": "`to_s()`",
                            "description": "Returns a string representation of the linked list (e.g., `\"A -> B -> C -> None\"` or `\"This linked list is empty\"`)."
                        }
                    ]
                }
            },
            "codePath": "/programSource/dataStructure/linkedList/singleLinkedList/singleLinkedList.rb"
        }
    ]
    main(
        category, directory, parentPathList, folder, fileName,
        jsonTitle, description, data
    )
