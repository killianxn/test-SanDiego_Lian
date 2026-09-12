import os
import shutil

imageCount = 0
documentCount = 0
videosCount = 0
othersCount = 0

path_list = []

folder = ["Image", "Document", "Videos", "Others"]

user_path = input("Type a path: ")

if os.path.exists(user_path) is True:
    path_list.append(os.listdir(user_path))
    for list in path_list:
        print(list)

    for i in folder:
        if not os.path.exists(i):
            os.mkdir(os.path.join(user_path, i))

            for file in path_list:
                if os.path.isdir(file) is True:
                    continue
                if file.endswith(".jpg", ".jpeg", ".png", ".gif"):
                    shutil.move(file, i[0])
                    print("hi")
                elif file.endswith(".pdf", ".docx", ".txt", ".pptx"):
                    pass
                elif file.endswith(".mp4", ".mov", ".avi"):
                    pass
                else:
                    pass


        else:
            continue

    # if not os.path.exists(user_path):
    #     print("hi")
    #     # os.path.join(base_dir, "Images")

else:
    print("Path does not exist")

