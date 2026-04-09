import json
from pathlib import Path

# 設定資料夾與輸出檔案
POSTS_DIR = Path("public/json/categories")
OUTPUT = Path("public/json/categories/categories.json")

def get_all_json_files(dir_path: Path):
    return [f for f in dir_path.rglob("*.json") if f.is_file()]

def generate():
    files = get_all_json_files(POSTS_DIR)

    posts = []
    tag_set = set()
    year_set = set()

    for file in files:
        with open(file, encoding="utf-8") as f:
            content = json.load(f)

        # 支援原本 TypeScript PostMeta 結構
        posts.append({
            "id": content.get("id", ""),  # 若沒有 id 可以留空
            "type": content.get("type", ""),
            "title": content.get("title", ""),
            "category": content.get("category", ""),
            "tags": content.get("tags", []),
            "year": content.get("year", 0)
        })

        # 收集所有 tag 與 year
        for tag in content.get("tags", []):
            tag_set.add(tag)
        year_set.add(content.get("year", 0))

    result = {
        "tags": sorted(tag_set),
        "years": sorted(year_set),
        "posts": posts
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print("✅ categories.json generated")

if __name__ == "__main__":
    generate()