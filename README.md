# GPT2Augmentaion
An experiment in augmenting IMDB dataset with GPT2
Read Deep_proj.pdf for more information

Uses libraries:
<BR> torch 1.13.1 
<BR> torchtext 0.14.1
<BR> transformers 4.21.0
<BR> scikit-learn 1.2.0
<BR> pandas 1.4.3
<BR> numpy 1.23.1

Run "genData.py" to generate additional samples using GPT2. <BR>
The samples are stored in "data.out". <BR>
The code assumes you have a GPU available in cuda:0, but there are instructions within on modifying it to run on CPU. <BR>
This code takes a while to run. <BR>
<BR>
Run "cleanData.py" to clean the samples in "data.out" into a usable format. <BR>
The samples will be written to "clean_data.out". <BR>
<BR>
Run the notebook to train a transformer on the reduced/augmented IMDB dataset. <BR>
The first cell contains some parameters that can control the execution. <BR>
ADD_DATA - If True, will take the samples from "clean_data.out". <BR>
FORCE_BALANCE - If True, will duplicate samples to balance the number of positive and negative review.s <BR>
select_len - This is the maximum length of samples in the reduced dataset. 300 is the parameter used in "genData.py". <BR>
cut_off_len - Due to limited memory all sequences are truncated to this length. This includes the test_set. <BR>
