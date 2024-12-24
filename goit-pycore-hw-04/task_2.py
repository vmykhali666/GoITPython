def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        cats = []
        for line in lines:
            cat_id, name, age = line.strip().split(',')
            cats.append({"id": cat_id, "name": name, "age": age})
        return cats
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

cats_info = get_cats_info("./cats_file.txt")
print(cats_info)