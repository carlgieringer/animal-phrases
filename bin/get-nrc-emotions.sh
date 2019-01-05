#!/usr/bin/env bash

script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
base_dir=${script_dir}/../

mkdir $base_dir/data
curl http://sentiment.nrc.ca/lexicons-for-research/NRC-Emotion-Lexicon.zip > $base_dir/data/NRC-Emotion-Lexicon.zip
cd $base_dir/data/
unzip NRC-Emotion-Lexicon.zip
