def read_sales_file(file_path):
    try:
        with open(file_path, "r", encoding="latin-1") as file:
            lines = file.readlines()
        return lines
    except Exception as e:
        print("Error reading file:", e)
        return []