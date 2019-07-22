import json
from nltk.tokenize import sent_tokenize, word_tokenize

word = "ate"

# create <WORD>-word.jsgf file
word_file = "wordfiles/" + word + "-word.jsgf"
with open(word_file, 'w') as outfile:
    json.dump("#JSGF V1.0;", outfile);
    outfile.write('\n');
    json.dump("grammar word;", outfile);
    outfile.write('\n');
    json.dump("public <wholeutt> = sil " + word + " [ sil ];", outfile);

# create <WORD>-align.jsgf file
words_dict = "wordFiles/words.dict"
tokens = []
file = open(words_dict,'r')
lines = file.readlines()
for line in lines:
    if (line.startswith(word) == True):
        tokens = word_tokenize(line)
file.close()
align_file = "wordfiles/" + word + "-align.jsgf"
with open(align_file, 'w') as outfile:
    json.dump("#JSGF V1.0;", outfile);
    outfile.write('\n');
    json.dump("grammar word;", outfile);
    outfile.write('\n');
    token_list = ""
    for token in tokens[1:]:
        token_list += token.lower()
        token_list += " "
    json.dump("public <" + word + "> = sil " + token_list + "[ sil ];", outfile);

# create <WORD>-neighbors.jsgf files
neighbors_file = "wordfiles/" + word + "-neighbors.jsgf"
tokens = []
file = open(align_file,'r')
lines = file.readlines()
with open(neighbors_file, 'w') as outfile:
    for line in lines:
        json.dump(line,outfile);
        outfile.write('\n');
file.close()
neighbors = ["<aa> = aa | ah | er | ao;",
"<ae> = ae | eh | er | ah;",
"<ah> = ah | ae | er | aa;",
"<ao> = ao | aa | er | uh;",
"<aw> = aw | aa | uh | ow;",
"<ay> = ay | aa | iy | oy | ey;",
"<b> = b | p | d;",
"<ch> = ch | sh | jh | t;",
"<dh> = dh | th | z | v;",
"<d> = d | t | jh | g | b;",
"<eh> = eh | ih | er | ae;",
"<er> = er | eh | ah | ao;",
"<ey> = ey | eh | iy | ay;",
"<f> = f | hh | th | v;",
"<g> = g | k | d;",
"<hh> = hh | th | f | p | t | k;",
"<ih> = ih | iy | eh;",
"<iy> = iy | ih;",
"<jh> = jh | ch | zh | d;",
"<k> = k | g | t | hh;",
"<l> = l | r | w;",
"<m> = m | n;",
"<ng> = ng | n;",
"<n> = n | m | ng;",
"<ow> = ow | ao | uh | aw;",
"<oy> = oy | ao | iy | ay;",
"<p> = p | t | b | hh;",
"<r> = r | y | l;",
"<ss> = sh | s | z | th;",
"<sh> = sh | s | zh | ch;",
"<t> = t | ch | k | d | p | hh;",
"<th> = th | s | dh | f | hh;",
"<uh> = uh | ao | uw | uw;",
"<uw> = uw | uh | uw;",
"<v> = v | f | dh;",
"<w> = w | l | y;",
"<y> = y | w | r;",
"<z> = z | s | dh | z;",
"<zh> = zh | sh | z | jh;"]
for line in neighbors:
    json.dump(line,outfile);
