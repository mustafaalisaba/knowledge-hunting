from datasets import load_dataset, get_dataset_split_names, get_dataset_config_names
import stanza
from stanza.server import CoreNLPClient

# print(stanza.__file__)
# print(dir(stanza))

# stanza.install_corenlp()
# stanza.download_corenlp_models(model='english-extra', version='4.5.2')

def semantic_rep_schema(_candidates, _predC, _plus, _p, _predQ):
    """ input: candidates (list), predC, plus, p, predQ
        output: 
    """
    print(_candidates, type(_candidates))
    print(_predC)
    print(_plus)
    print(_p)
    print(_predQ)
    # for i in range(0, len(_candidates), 2):
    #     E1 = _candidates[i]
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
    return

def syntactic_parsing(_sentences):
    """ input: winograd sentences (list)
        output: annotations: tokens, pos, lemma, parse, depparse
    """
    # with CoreNLPClient(
    #     annotators=['tokenize','pos','lemma','parse','depparse'],
    #     memory='8G',
    #     endpoint='http://localhost:9005',
    #     be_quiet=False) as client:
    #     # ann = client.annotate(documents[1])
    #     # print(ann, type(ann))
    #     for sent in _sentences:
    #         ann = client.annotate(sent)
    #         print(ann.sentence, type(ann.sentence))
    #         print("{:12s}\t{:12s}\t{:6s}".format("Word", "Lemma", "POS"))
    #         for i, sent in enumerate(ann.sentence):
    #             print("[Sentence {}]".format(i+1))
    #             for t in sent.token:
    #                 print("{:12s}\t{:12s}\t{:6s}".format(t.word, t.lemma, t.pos))
    #             print("")
    #         print("--- Constituency Parse ---")
    #         sentence = ann.sentence[0]
    #         print("Sentence 0: ")
    #         print(type(sentence)) # type <class 'CoreNLP_pb2.Sentence'>
    #         constituency_parse = sentence.parseTree
    #         print(constituency_parse)
    #         print("--- Constituency Parse Finished ---")
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
    return

def main() -> int:
    dataset = load_dataset("winograd_wsc", "wsc285", split="test") # configurations: wsc273, wsc285
    sentences = dataset["text"] # documents = ["The city councilmen...", "The .." ...] list of strings
    candidates = dataset["options"]
    # print(can, type(can))
    # for i in range(len(can)):
    #     candidates = dataset["options"][i]
    #     print(candidates, type(candidates))
    # print(can, type(can))
    # print(sentences, type(sentences))
    # syntactic_parsing(sentences) # connection to CoreNLP and annotations
    semantic_rep_schema(candidates,0,0,0,0)
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