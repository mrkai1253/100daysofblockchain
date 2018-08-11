import datetime
import hashlib
import json 
from flask import Flask, jsonify



class BlockChain:
    def __init__(self):
        self.chain = []  #initialising the chain
        #Creating the genisis block
        self.create_block(proof = 1 , prev_hash = '0')

        #function to create block
    def create_block(self,proof,prev_hash):
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : datetime.datetime.now(),
            
        }
        
