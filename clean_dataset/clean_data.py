import fastdup
from IPython.display import HTML


if __name__ == "__main__":
    fastdup.create_duplicates_gallery(similarity_file="reports/similarity.csv", 
                                      save_path="reports", 
                                      num_images=5)

    HTML('scene_classification/report/train/similarity.html')

