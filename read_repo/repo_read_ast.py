import os, ast, json, re

def parse_python_file(file_path):
    classes, functions = [], []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read(), filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                classes.append(node.name)
            elif isinstance(node, ast.FunctionDef):
                func_info = {
                    "name": node.name,
                    "args": [arg.arg for arg in node.args.args],
                    "is_async": isinstance(node, ast.AsyncFunctionDef)
                }
                functions.append(func_info)
    except SyntaxError as e:
        return {"error": f"Syntax error in {file_path}: {e}"}
    return {"classes": classes, "functions": functions}

def parse_sql_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sql = file.read() 
        tables =  re.findall(r'CREATE TABLE (\w+)', sql, re.IGNORECASE)
        procedures = re.findall(r"CREATE\s+PROCEDURE\s+(\w+)", sql, re.IGNORECASE)

        return {"tables": tables, "procedures": procedures}
    except Exception as e:
        return {"error": f"Error reading {file_path}: {e}"} 
    
def scan_repo(repo_path):
    repo_map = {}
    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file.endswith(".py"):
                repo_map[file_path] = parse_python_file(file_path)
            elif file.endswith(".sql"):
                repo_map[file_path] = parse_sql_file(file_path)
    return repo_map

if __name__ == "__main__":
    repo_path = r"D:\STPython\demo_repo"  # lưu ý thêm r để tránh lỗi escape
    repo_structure = scan_repo(repo_path)
    print(json.dumps(repo_structure, indent=4, ensure_ascii=False))
