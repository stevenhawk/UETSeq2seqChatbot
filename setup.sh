#!/usr/bin/env bash

# create and own the directories to store results locally
save_dir='/var/lib/tf_seq2seq_chatbot_help_viet/'
sudo mkdir -p $save_dir'/data/'
sudo mkdir -p $save_dir'/nn_models/'
sudo mkdir -p $save_dir'/results/'
sudo chown -R "$USER" $save_dir

# copy train and test data with proper naming
data_dir='tf_seq2seq_chatbot/data/train'
cp $data_dir'/my-data.txt' $save_dir'/data/chat.in'
cp $data_dir'/my-data.txt' $save_dir'/data/chat_test.in'
