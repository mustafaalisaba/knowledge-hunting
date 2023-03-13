from datasets import load_dataset, get_dataset_split_names, get_dataset_config_names
import pandas as pd
import stanza
from stanza.server import CoreNLPClient
import xml.etree.ElementTree as ET

# print(stanza.__file__)
# print(dir(stanza))

# stanza.install_corenlp()
# stanza.download_corenlp_models(model='english-extra', version='4.5.2')
def query_gen():
    pass

def semantic_representation(_candidates, _predC, _plus, _p, _predQ) -> list:
    """ input: candidates (list), predC, plus, p, predQ
        output: context clause (vector containing E1, E2 and PredC (lists of strings))
    """
    E1 = []
    E2 = []
    PredC = []
    
    # for i in range(0, len(_candidates)):
    #     antecedents.append(_candidates[i]) # Remove duplicate antecedents
    # print(antecedents, type(antecedents), len(antecedents))
    
    for noun1 in _candidates:
        # noun_1 = x[0]
        E1.append(noun1[0])
    print("\nE1\n", E1, len(E1), type(E1))

    for noun2 in _candidates:
        # noun_1 = x[0]
        E2.append(noun2[1])
    print("\nE2\n", E2, len(E1), type(E1))

    # I need to filter PredC from constituency parse?

    # for i in range(0, len(_candidates), 2):
    #     print(_candidates[i], type(_candidates))
        # for j in range(0, len(_candidates[i]), 2):
        #     print(j, type(j))
        #     E1.append(_candidates[j])
        # print(E1)
    # E1 = [x for x in range(len(_candidates))]
    # print(_candidates, type(_candidates))
    # print(_predC)
    # print(_plus)
    # print(_p)
    # print(_predQ)

    # for i in range(0, len(_candidates), 2):
    #     E1 = _candidates[i]
    #     E2 = _candidates[1]
    #     print(E1)
    #     for j in range(2):
    #         E1 = _candidates[i][j]
    #         print(E1)
    # E2 = _candidates[0][1]
    # for i in range(len(_candidates)):
        # print(i)
        # E1 = _candidates[0][]
        # print(E1)
        # for j in range(i):
        #     E1 = _candidates[i][j]
        #     print(E1)
    print("\nContext clause {E1, E2, PredC}")
    context = [E1, E2, PredC]
    print("\nQuery clause {P, PredQ}")
    query = [_p, _predQ]
    return context, query

def syntactic_parsing(_sentences):
    """ input: winograd sentences (list)
        output: annotations: tokens, pos, lemma, parse, depparse
    """
    text = "Chris Manning is a nice person. Chris wrote a simple sentence. He also gives oranges to people."
    with CoreNLPClient(
        annotators=['tokenize','pos','lemma','parse','depparse'],
        output_format='xml', # ['conll', 'conllu', 'json', 'serialized', 'text', 'xml', 'inlinexml']
        memory='8G',
        endpoint='http://localhost:9005', # preload=True
        be_quiet=False) as client:
        # ann = client.annotate(_sentences)
        # print(ann, type(ann))
        # ann = client.annotate(documents[1])
        # print(ann, type(ann))
        
        for s in _sentences: # for all sentences in dataset
            ann = client.annotate(s)
            # print("ANN ", ann, type(ann))
            #XML
            root = ET.fromstring(ann)
            # print(root, type(root))
            print("\n--- Accessing words, lemmas and POS ---\n")
            for token in root.iter('token'):
                for child in token:
                    print(child.tag, child.text)
            print("\n--- words, lemma and pos Finished ---\n")
            
            print("\n--- Accessing constituency parse ---\n")
            for parse in root.iter('parse'):
                print(parse.tag, parse.text, type(parse.text))
                # for child in parse:
                #     print(child.tag, child.text)
            # if child.tag == "parse": print(child.text)
            # print(ann.sentence, type(ann.sentence))
            # print("\n--- Accessing words, lemmas and POS ---\n")
            # print("{:12s}\t{:12s}\t{:6s}".format("Word", "Lemma", "POS"))
            # for i, sent in enumerate(ann.sentence):
            #     print("[Sentence {}]".format(i+1))
            #     for t in sent.token:
            #         print("{:12s}\t{:12s}\t{:6s}".format(t.word, t.lemma, t.pos))
            #         # falta guardar los tokens, lemas y poss
            #     print("--- words, lemma and pos Finished ---")

            # print("\n--- Accessing constituency parse ---\n")
            # sentence = ann.sentence[0]
            # print("Sentence 0: ", sentence, type(sentence)) # type <class 'CoreNLP_pb2.Sentence'>
            # constituency_parse = sentence.parseTree
            # print(constituency_parse, type(constituency_parse))
            # # Necesito iterar sobre los hijos de parseTree y obtener el valor VP, VBD?
            # print("\n--- Display childrens ---\n")
            # print(constituency_parse.child[0])
            # if constituency_parse.child[0].value == "VP":
            #     print(constituency_parse.child[0].value)
            # print("--- Constituency Parse Finished ---")

            #### Debe retornar las anotaciones y la capacidad para acceder a cada subitem de ellas.
    pos= 0
    contituencies=0
    dependencies=0
    
    return pos, contituencies, dependencies
            # for t in ann.sentence.token:
            #     print("{:12s}\t{:12s}\t{:6s}".format(t.word, t.lemma, t.pos))
            # print("ann Object\n", ann, type(ann))
            # print(ann.sentence, type(ann.sentence))

            # print("{:12s}\t{:12s}\t{:6s}".format("Word", "Lemma", "POS"))
            # for i, sent in enumerate(ann.sentence):
            #     print("[Sentence {}]".format(i+1))
            #     for t in sent.token:
            #         print("{:12s}\t{:12s}\t{:6s}".format(t.word, t.lemma, t.pos))
            #     print("")

            # print("--- Constituency Parse ---")
            # sentence = ann.sentence[0]
            # print("Sentence 0: ")
            # print(type(sentence)) # type <class 'CoreNLP_pb2.Sentence'>
            # constituency_parse = sentence.parseTree
            # print(constituency_parse)
            # print("--- Constituency Parse Finished ---")

            #Error: solo lo está sacando para la primera oracion de las gemelas
            # get the constituency parse of the first sentence
            # print("--- Constituency Parse ---")
            # sentence = ann.sentence[0]
            # constituency_parse = sentence.parseTree
            # print(constituency_parse)
            # print(sentence, type(sentence))
            # print(":D")
            # print("fuck----------------")
            # sentence = ann.sentence[0]
            # print(sentence, type(sentence))
        # sentence = ann.sentence[0]
        # print(sentence, type(sentence))
        # sentence = ann.sentence[0]
        # constituency_parse = sentence.parseTree
        # print(constituency_parse)
    # Accessing annotations
    # print("{:12s}\t{:12s}\t{:6s}".format("Word", "Lemma", "POS"))
    # for i, sent in enumerate(ann.sentence):
    #     print("[Sentence {}]".format(i+1))
    #     for t in sent.token:
    #         print("{:12s}\t{:12s}\t{:6s}".format(t.word, t.lemma, t.pos))
    #     print("")

    # nlp = stanza.Pipeline(lang="en", processors='tokenize,pos,lemma,constituency,depparse', use_gpu=True, pos_batch_size=3000)
    # in_docs = [stanza.Document([], text=d) for d in _documents]
    # print(in_docs, type(in_docs))
    # out_docs = nlp(in_docs) # Call the neural pipeline on this list of documents
    # print(out_docs)

    # print(out_docs.entities)
    # print(text, type(text))
    # nlp = stanza.Pipeline('en', processors='tokenize,pos', use_gpu=True, pos_batch_size=3000) # Build the pipeline, specify part-of-speech processor's batch size
    # doc = nlp("Barack Obama was born in Hawaii.") # Run the pipeline on the input text
    # print(doc)
    

def main() -> int:
    dataset = load_dataset("winograd_wsc", "wsc285", split="test") # configurations: wsc273, wsc285
    print("Dataset\n", dataset, len(dataset), type(dataset))
    sentences = dataset["text"][:2] # documents = ["The city councilmen...", "The .." ...] list of strings
    print("\nSentences\n", sentences, len(sentences), type(sentences))
    candidates = dataset["options"][:2]
    print("\nCandidate options\n", candidates, len(candidates), type(candidates))
    # print(can, type(can))
    # for i in range(len(can)):
    #     candidates = dataset["options"][i]
    #     print(candidates, type(candidates))
    # print(can, type(can))
    # print(sentences, type(sentences))
    parts_of_speech, constituents, dependencies = syntactic_parsing(sentences) # connection to CoreNLP and annotations
    
    # context_clause, query_clause = semantic_representation(candidates,0,0,0,0)
    
    # print(context_clause, type(context_clause))
    # print(query_clause, type(query_clause))
    # print(len(context_clause[0]))
    # sentence = ann.sentence[0]
    # print(sentence, type(sentence))
    # preprocessing_stage(documents)
    # dataset = load_dataset("winograd_wsc", "wsc285", split="test") # configurations: wsc273, wsc285
    # with CoreNLPClient(
    #     annotators=['tokenize', 'pos', 'parse', 'depparse'],
    #     memory='8G',
    #     endpoint='http://localhost:9005',
    #     be_quiet=True) as client:
    #     # text = "Albert Einstein was a German-born theoretical physicist."
    #     text = dataset["text"]
    #     print(text, type(text))
    #     for sent in text:
    #         document = client.annotate(sent)
    #         print(document, type(document))
    #     sentence = document.sentence[0]
    #     print(sentence)
    #     # get the constituency parse of the first sentence
    #     constituency_parse = sentence.parseTree
    #     print(constituency_parse)
    return 0

if __name__ == '__main__':
    main()
    # print("{:12s}\t{:12s}\t{:6s}\t{}".format("Word", "Lemma", "POS", "NER"))

    # for i, sent in enumerate(document.sentence):
    #     print("[Sentence {}]".format(i+1))
    #     for t in sent.token:
    #         print("{:12s}\t{:12s}\t{:6s}\t{}".format(t.word, t.lemma, t.pos, t.ner))
    #     print("")

    # print("Dataset ", dataset, type(dataset))
    # text = dataset["text"] #next(iter(dataset))["text"]
    # print("Text", text, type(text))
    # # text = "Chris Manning is a nice person. Chris wrote a simple sentence. He also gives oranges to people."
    # with CoreNLPClient(
    #     annotators=['tokenize', 'pos', 'parse', 'depparse'],
    #     timeout=30000,
    #     endpoint="http://localhost:9009",
    #     classpath=None,
    #     memory='6G') as client:
    #     for i in text:
    #         ann = client.annotate(i) # annotations
    #         print(ann)
    # print(ann)
    
    # for i in dataset:
    #     print(i)

    # print(dataset)

# print(get_dataset_split_names("winograd_wsc", "wsc285")) # wsc is only for test

# ds_builder = load_dataset_builder("winograd_wsc", "wsc285")

# print(ds_builder.info.description)

# print("Dataset Features")
# print(ds_builder.info.features)