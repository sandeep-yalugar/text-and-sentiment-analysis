import json
import os



def make_set(fpath):
  s = set()
  with open(fpath,'r') as fp:
    content = fp.read()
  words = content.split('\n')
  for i in words:
    s.add(i.lower())
  s.discard('')
  return s

def make_set2(fpath):
    ss = set()
    with open(fpath,'r') as f:
     content2 = f.read()
    word_raw = content2.split('\n')
    for ii in word_raw:
      if '|' in ii:
        ss.add(ii.split('|')[0].rstrip().lower())
      else:
        ss.add(ii.lower())
    ss.discard('')
    return ss


def make_stop_word_json():
    folder = './StopWords'
    flis = os.listdir(folder)
    ss = set()
    for file_name in flis:
        path_name = folder + '/' + file_name
        s = make_set2(path_name)
        ss = ss|s


    with open('stop_words.json','w') as jp:
        json.dump(list(ss),jp)

pos = make_set('./MasterDictionary/positive-words.txt')
neg = make_set('./MasterDictionary/negative-words.txt')
with open('positive.json','w') as jp:
    json.dump(list(pos),jp)
with open('negative.json','w') as jp2:
    json.dump(list(neg),jp2)
print('task completed')


