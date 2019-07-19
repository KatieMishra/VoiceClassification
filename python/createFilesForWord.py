import json

word = "test"
json_file = "wordfiles/" + word + "-word.jsgf"
with open(json_file, 'w') as outfile:
    json.dump("#JSGF V1.0;", outfile);
    outfile.write('\n');
    json.dump("grammar word;", outfile);
    outfile.write('\n');
    json.dump("public <wholeutt> = sil " + word + " [ sil ];", outfile);
    outfile.write('\n');

words_dict = "wordFiles/words.dict"
with open(json_file, 'r') as outfile:
    
