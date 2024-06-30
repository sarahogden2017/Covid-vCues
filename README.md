# COVID vCues Dataset

This is a dataset research project developed to assist Professor Ankur Chattopadhyay's COVID vCues research by creating a multi-modal dataset containing images sourced from reliable and unreliable sources on COVID-19. This dataset will be used to train multiple AI models: reliable vs unreliable images, and identify memes, ads, claims, fact-checks, or logos.

## To-Do
- [X] Scrape CoAID (Sarah)
- [X] Scrape ReCovery (Shreetika)  
- [X] Scrape MM-Covid (Shreetika)
- [ ] Scrape tweets with Twikit  
- [X] Consolidate CoAID, ReCovery, & MM-Covid (Sarah)
- [X] Remove duplicate images
- [ ] Deep learning reliable vs unreliable model  
      - [X] Small test model w/ Keras and Tensorflow (200 images each) (Sarah)  
      - [X] Keras neural network using all images - Model is overfit? (Sarah)  
      - [X] Small test model w/ SVM (also tried with random images on Google) (Shreetika)
- [ ] Clean dataset  
      1.  Remove duplicates w/ existing script  
      2.  Figure out how to remove pixilated images  
      3.  Use OpenCV to identify people and manually del profile pictures  
      4.  Remove favicon and icon type images by sorting images by size  
      5.  Randomly select same amount of remaining images from each category  
- [ ] Redo model training with cleaned dataset
- [ ] Develop category identifying models:
      Method 1  
      - [ ] Memes  
      - [ ] Ads  
      - [ ] Claims  
      - [ ] Fact-checks  
      - [ ] Logos
      Method 2
      - [ ] Infographics/Diagrams  
      - [ ] Photographs  
      - [ ] Illustrations  
      - [ ] Memes  
      - [ ] Advertisements  
      - [ ] Misc/Logos  
      - Image naming convention idea: (un)reliable.subcategory.####.jpg/png  
- [ ] Analysis of dataset breakdown

## Sources

The dataset based on **CoAID: COVID-19 Healthcare Misinformation Dataset**, ReCovery, and MM-Covid.

**Citations:**  
@misc {  
  cui2020coaid,  
  title={CoAID: COVID-19 Healthcare Misinformation Dataset},  
  author={Limeng Cui and Dongwon Lee},  
  year={2020},  
  eprint={2006.00885},  
  archivePrefix={arXiv},  
  primaryClass={cs.SI}  
}  
https://github.com/apurvamulay/ReCOVery/tree/master  
https://github.com/bigheiniu/MM-COVID/blob/main/README.md  

## Usage

This dataset is still underdevelopment and not yet ready for use.

## Authors
Sarah Ogden  
Shreetika Poudel  

## Helpful Tutorials
- Scrapy in 30 minutes (start here.): https://www.youtube.com/watch?v=r7pMqU2kYqc
- CNN in Python: https://medium.com/metakratos-studio/python-based-ai-powered-by-tensorflow-and-keras-52140b1495e3  
- Twikit Example: https://github.com/d60/twikit/blob/main/examples/download_tweet_media.py  
- Remove duplicate images: https://pyimagesearch.com/2020/04/20/detect-and-remove-duplicate-images-from-a-dataset-for-deep-learning/     
- SVM model for image classification: https://medium.com/analytics-vidhya/image-classification-using-machine-learning-support-vector-machine-svm-dc7a0ec92e01   
- Fastdup: https://medium.com/visual-layer/fastdup-a-powerful-tool-to-manage-clean-curate-visual-data-at-scale-on-your-cpu-for-free-12e850946ead  
