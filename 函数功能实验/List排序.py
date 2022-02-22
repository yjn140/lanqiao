def list_sort_string():
    list = ["delphi", "Delphi", "python", "Python", "c++", "C++", "c", "C", "golang", "Golang"]
    list.sort()  # 按字典顺序升序排列
    print("升序:", list)

    list.sort(reverse=True)  # 按降序排列
    print("降序:", list)
