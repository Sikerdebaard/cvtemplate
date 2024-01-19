# Modern cv template

![Alt text](cv.png?raw=true "Example screenshot")

## Using the template
A minimal set of instructions to get the template working.

1. Go to `data/profile.yml` and add a new job profile. For this example datascientist is assumed. For any other position replace datascientist in this manual with the name of your choice.
    ```yml
    Data Scientist:
        meta: datascientist.yml
    ```
2. Create `datascientist.yml` inside the `data/meta/` folder. This file denotes how many years of experience you have gained with each of these skills. It is advisable to put no more than 8 skills in this list due to space limitations in the template.
    ```yml
    by-year:
      2012:
        - GIT
        - Linux

      2017:
        - Python
        - Pandas


      2019:
        - scikit-learn
        - pytorch

    manual:
      FastAPI: 2
      Flask: 2
    ```
3. Run the python script `scripts/build.py`. Its dependency requirements can be found in `requirements.txt`. Make sure there are no errors and that the `datascientist.tex` files are generated in the `generated/meta/` and `generated/vars/` folders.
4. Copy the folder `parts/mlengineer/` to `parts/datascientist/` and adjust the relevant tex files in this folder to your liking.
5. Open `cv.tex` and find this line:
    ```tex
    %jobpos
    \input{generated/vars/mlengineer}
    ```
    
    Change it to:
    ```tex
    %jobpos
    \input{generated/vars/datascientist}
    ```
6. Additionally further modifications of the files in `parts/general/` can be made. Such as a profile picture, contact details and education. 
7. Now build `cv.tex`. 


This cv template is a heavily modified version of the sidebar left template in this repository: https://github.com/jankapunkt/latexcv
