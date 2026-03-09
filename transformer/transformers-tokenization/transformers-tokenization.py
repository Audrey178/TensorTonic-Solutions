import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        # YOUR CODE HERE
        self.word_to_id = {
            "<PAD>": 0,
            "<UNK>": 1,
            "<BOS>": 2,
            "<EOS>": 3,
        }

        for word, id in self.word_to_id.items():
            self.id_to_word[id]=word

        for text in texts:
            for word in text.split(" "): 
                if word in self.word_to_id:
                    continue 
                id = len(self.word_to_id)
                self.word_to_id[word] = id
                self.id_to_word[id] = word
        self.vocab_size = len(self.word_to_id)
                
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        # YOUR CODE HERE
        encode_list = []
        # encode_list.append(self.bos_token)
        for word in text.split(" "):
            encode_list.append(self.word_to_id.get(word, self.word_to_id[self.unk_token]))
        # encode_list.append(self.eos_token)
        return encode_list
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        # YOUR CODE HERE
        texts = []
        for id in ids:
            texts.append(self.id_to_word[id])
        return " ".join(texts)
        
