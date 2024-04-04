Quick summary of what I've done: 
- Downloaded FaceScrub dataset and split into train, val, test and deployment datasets
- Preprocessed them all by retrieving faces from images and aligning them
- Used DeepFace model for face recognition. I tried to fine-tune it using train dataset using also some data augmentation techniques
- Evaluation on test dataset however shows that something went wrong. I tried to debug it but run out of ideas
- Created code for creating face database by getting a mean of embeddings of all images of a person
- Created databases for test and deployment sets which I serialized and added to this repository
- Created a function for adding a person to dataset by simply passing path to his/her images directory

Model: https://drive.google.com/file/d/1i3ZXjlcoaFdvdGWVU_VkPAuOmkYhL0qJ/view?usp=sharing
Dataset: https://drive.google.com/file/d/1rxT2pMvSno5jSA60FAAcrumnL-rLlCIZ/view?usp=sharing
Dataset aligned (preprocessed): https://drive.google.com/file/d/16h9nYmmVo7_8wnQ_jUqBccfGvZSRHJ7i/view?usp=sharing