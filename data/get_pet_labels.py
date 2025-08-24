
from os import listdir


def get_pet_labels(image_dir):
    
    in_files = listdir(image_dir)
    
    results_dic = dict()
   
    
    for idx in range(0, len(in_files), 1):
       
       if in_files[idx][0] != ".":
           filename = in_files[idx]
           pet_label = ""

           parts = filename.lower().split("_")
           pet_label = " ".join([p for p in parts if p.isalpha()]).strip()

          
           if filename not in results_dic:
              results_dic[filename] = [pet_label]
           else:
               print("** Warning: Duplicate files exist in directory:", filename)
 
    return results_dic
