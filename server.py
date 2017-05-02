import socket
import sys

import os
import sys
import socket

import tensorflow as tf

from tf_seq2seq_chatbot.configs.config import FLAGS
from tf_seq2seq_chatbot.lib import data_utils
from tf_seq2seq_chatbot.lib.seq2seq_model_utils import create_model, get_predicted_sentence
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
try:
    s.bind((HOST, PORT))
except socket.error:
    #print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print ('Socket bind complete')
 
s.listen(10)
print ('Socket now listening')
 
#now keep talking with the client

with tf.Session() as sess:
    # Create model and load parameters.
    model = create_model(sess, forward_only=True)
    model.batch_size = 1  # We decode one sentence at a time.

    # Load vocabularies.
    vocab_path = os.path.join(FLAGS.data_dir, "vocab%d.in" % FLAGS.vocab_size)
    vocab, rev_vocab = data_utils.initialize_vocabulary(vocab_path)
     #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
	
    while 1:
        data,address = conn.recvfrom(1024)
       # reply = 'OK...' + data
        if not data: 
           continue
        sentence=data.decode("utf-8", "ignore")
        print(sentence)
        predicted_sentence = get_predicted_sentence(sentence, vocab, rev_vocab, model, sess)
        print(predicted_sentence)
        conn.sendall(predicted_sentence.encode("utf-8"))
conn.close()
s.close()
