
def adjust_results4_isadog(results_dic, dogfile):
   
    dognames = set()
    with open(dogfile, "r") as infile:
        for line in infile:
            name = line.strip().lower()
            if name:
                dognames.add(name)

    for key, value in results_dic.items():
        pet_label = value[0].strip().lower()
        pet_is_dog = 1 if pet_label in dognames else 0

        clf_labels = [lbl.strip().lower() for lbl in value[1].split(",")]
        clf_is_dog = 1 if any(lbl in dognames for lbl in clf_labels) else 0

        if pet_is_dog and clf_is_dog:
            value.extend((1, 1))
        elif pet_is_dog and not clf_is_dog:
            value.extend((1, 0))
        elif not pet_is_dog and clf_is_dog:
            value.extend((0, 1))
        else:
            value.extend((0, 0))
