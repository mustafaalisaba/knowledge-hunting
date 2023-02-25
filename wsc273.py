from datasets import load_dataset, get_dataset_split_names, get_dataset_config_names
import stanza
from stanza.server import CoreNLPClient

# stanza.install_corenlp()
def semantic_rep_schema():
    return

if __name__ == '__main__':
    dataset = load_dataset("winograd_wsc", "wsc285", split="test") # configurations: wsc273, wsc285
    # print("Dataset ", dataset, type(dataset))
    text = dataset["text"] #next(iter(dataset))["text"]
    print("Text", text, type(text))
    # text = "Chris Manning is a nice person. Chris wrote a simple sentence. He also gives oranges to people."
    with CoreNLPClient(
        annotators=['tokenize', 'pos', 'parse', 'depparse'],
        timeout=30000,
        endpoint="http://localhost:9009",
        classpath=None,
        memory='6G') as client:
        for i in text:
            ann = client.annotate(i) # annotations
            print(ann)
    # print(ann)
    
    # for i in dataset:
    #     print(i)

    # print(dataset)

# print(get_dataset_split_names("winograd_wsc", "wsc285")) # wsc is only for test

# ds_builder = load_dataset_builder("winograd_wsc", "wsc285")

# print(ds_builder.info.description)

# print("Dataset Features")
# print(ds_builder.info.features)