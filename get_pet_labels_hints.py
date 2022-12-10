from os import listdir


def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    results_dic = dict()

    for i in range(0, len(in_files), 1):
        if in_files[i][0] != ".":
            pet_label = ""
            temp = in_files[i].replace("_", " ")

            for j in range(len(temp)):
                if temp[j].isalpha() or temp[j] == " ":
                    pet_label += temp[j]
            pet_label = pet_label.strip().lower()
            results_dic[in_files[i]] = [pet_label]
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]

            else:
                print("** Warning: Duplicate files exist in directory:", in_files[i])
    return results_dic
