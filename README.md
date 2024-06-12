# COVID vCues Dataset

This is a dataset research project developed to assist Professor Ankur Chattopadhyay's COVID vCues research by creating a multi-modal dataset containing images sourced from reliable and unreliable sources on COVID-19. This dataset will be used to train multiple AI models: reliable vs unreliable images, and identify memes, ads, claims, fact-checks, or logos.

## To-Do
- [X] Scrape CoAID (Sarah)
- [X] Scrape ReCovery (Shreetika)  
- [ ] Scrape MM-Covid (Shreetika)
- [ ] Research Twarc: https://github.com/DocNow/twarc/blob/main/README.md (Sarah)  
- [ ] Consolidate CoAID, ReCovery, & MM-Covid (Sarah)
- [ ] Remove duplicate images
- [ ] Deep learning reliable vs unreliable model  
      - [X] Small test model w/ Keras and Tensorflow (200 images each) (Sarah)
      - [ ] Small test model w/ SVM (Shreetika)       
- [ ] Develop category identifying models:  
      - [ ] Memes  
      - [ ] Ads  
      - [ ] Claims  
      - [ ] Fact-checks  
      - [ ] Logos  
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
- Scrapy in 30 minutes (start here.)
  - https://www.youtube.com/watch?v=r7pMqU2kYqc
- CNN in Python: Keras  
  - https://medium.com/metakratos-studio/python-based-ai-powered-by-tensorflow-and-keras-52140b1495e3
