#!/usr/bin/env python3
# coding: utf-8
#卒論　　tweetの感情分析

from mlask import MLAsk

emotion_dict = {}

emotion_analyzer = MLAsk()
infile = open("all.csv", "r")
for line in infile:
  data_list = line.replace("\n", "").split(",")
  #print(data_list[3])
  result = emotion_analyzer.analyze(data_list[2])
  #if result["emotion"] != "None":
  if "representative" in result:
    print("all:", result)
    print("representative:", result["representative"], result["text"])
    print("representative:", result["representative"])
    if result["representative"][0] not in emotion_dict:
      emotion_dict[ result["representative"][0] ] = 1
    else:
      emotion_dict[ result["representative"][0] ] += 1
print(emotion_dict)
