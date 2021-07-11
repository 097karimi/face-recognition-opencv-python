# Face detection and recognition using opencv and python

This is a console based application which uses opencv and python in order to detect human face and finally recognize it.

This app works in three steps :
  
**First step :**
- Detecting human face and extract human faces from the image and finally save these images in directory called "/data/images_db"
    
**Second step :**
 - On the second step we are using an algorithm called LBPH (Local Binary Patterns Histograms) which will extract human face features and save these features in a yml file.
 - remember in this step, we actually extract the features of our specific user which we are intended to recognize.
    
**Third step :**
 - Now everything is ready to recognize our user face, in this step we detect the user face and compare it to our previous data which we callected in previous steps.

# Installation

1. **requirments**
  - pip3 install -r requirments.txt
2. **How to run ???**
  - Type **python3 main.py** on the terminal in right directory.
  - Turn your webcam on and press number **1** then press **Enter**
  - Press **2**
  - Press **3** and enjoy :)

