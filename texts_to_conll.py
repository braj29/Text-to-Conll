import spacy
import os
from utils_1 import load_text, get_paths


def text_to_conll(text,nlp, output_dir, basename, delimiter='\t', start_with_index=True,
                         overwrite_existing_conll_file=True):
    nlp_1 = spacy.load('en_core_web_sm')
    nlp = nlp_1
    doc = nlp(text)
    path = f'{output_dir}/{basename}'
    if overwrite_existing_conll_file == True:
        if os.path.isfile(path)==True:
            pass
        elif os.path.isfile(path) == False and os.path.isdir(output_dir) == False:
            os.mkdir(output_dir)
    if overwrite_existing_conll_file == False:
        if os.path.isfile(path)==True:
            pass
            print("File Exists! Set Param overwrite_existing_conll_file to true if you want to overwrite it.")
            exit()
        elif os.path.isfile(path) == False and os.path.isdir(output_dir) == False:
            os.mkdir(output_dir)

    with open(f'{output_dir}/{basename}', 'w') as outfile:
        for sent in doc.sents:
            for token in sent:
                index = str((token.i + 1) - sent.start)
                if start_with_index == True:
                    data = delimiter.join([index,
                                           token.text,
                                           token.tag_,
                                           token.lemma_,
                                           token.ent_type_,
                                           token.ent_iob_
                                           ])

                    lines = data + "\n"
                    outfile.write(lines)

                if start_with_index == False:
                    data = delimiter.join([
                        token.text,
                        token.tag_,
                        token.lemma_,
                        token.ent_type_,
                        token.ent_iob_
                    ])
                    lines = data + "\n"
                    outfile.write(lines)
            outfile.write("\n")


input_folder = '../Data/dreams'

txt_paths = get_paths(input_folder)
output_dir = f'{input_folder}/dream_conll'
print(txt_paths)
nlp = spacy.load('en_core_web_sm')
for txt_path in txt_paths:
    text = load_text(txt_path)
    basename = f'{os.path.basename(txt_path)[:-4]}.tsv'
    text_to_conll(text,nlp,output_dir,basename,
                         start_with_index = True,
                        overwrite_existing_conll_file = False)