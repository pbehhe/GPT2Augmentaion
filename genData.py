from transformers import pipeline, set_seed
import torchtext as tt
import numpy as np

'''
Generate data using GPT2. Take data from IMDB, separate to text and label and select all short sentences.
Feed two randomly sampled sentences to GPT2 and write only the generated text to output file
'''

N = 1000 # number of iterations, but there are multiple samples per iteration

ds_train, ds_test = tt.datasets.IMDB()

def separate(ds):
    ds_text = []
    ds_label = []
    for label,text in iter(ds):
        ds_text.append(text)
        ds_label.append(label)
    return ds_text,ds_label

ds_train_text, ds_train_label = separate(ds_train)

selectable_indices = [i for i in range(len(ds_train_text)) if len(ds_train_text[i]) < 300] # select only indices with short sentences

generator = pipeline('text-generation', model='gpt2-large',device = 0) #use gpt2-large. See https://huggingface.co/gpt2. Uses GPU. To use CPU remove the device argument
set_seed(42) # for reproduction. Since sample selection is not given a seed this is not actually reproducible

with open('data.out','a') as f:

    for i in range(N):

        indices = np.random.choice( selectable_indices ,size = 2)

        cat = ['' , 'positive movie review', 'negative movie review',] #convert the 1,2 classes to textual categories

        l = [cat[ds_train_label[i]] + ' : ' + ds_train_text[i] for i in indices]

        in_string = '\n'.join(l) + '\n'
        
        out = generator(in_string, max_length=1024, num_return_sequences=1)
        out_string = out[0]['generated_text']

        start = len(in_string)
        f.write(out_string[start:] + '\n')
        f.write('###') #marks the end of generation.
        print(i)


f.close()
