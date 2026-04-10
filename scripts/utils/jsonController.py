import json


class JsonController:
    def jsonWriter(self, path, data):
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    
    def jsonReader(self, path):
        with open(path, 'r', encoding="utf-8") as f:
            return json.load(f)
        
    def jsonViewer(self, data):
        print(json.dumps(data, indent=4, ensure_ascii=False))