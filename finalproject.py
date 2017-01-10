# Devin Cheong
# devin@bu.edu
#
# final project
#
# Partner: Matt Yang  
# Partner e-mail: ymcmatt@bu.edu
#
import math

def clean_text(txt):
    """takes a string of text txt as a parameter and
    returns a list containing the words in txt after it has been “cleaned”.
    """
##    file = open(txt, 'r')
##    text = file.read()
##    file.close()

    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('!', '')
    txt = txt.replace('?', '')
    txt = txt.replace(':', '')
    txt = txt.replace(';', '')
    txt = txt.replace('"', '')
    txt = txt.replace("'", '')

    txt = txt.lower()
    txt = txt.split(' ')
    return txt


def stem(s):
        """takes a string s and returns the stem of s
        """
        if s == '':
            return ''
        if s[-3:] == 'ing':
            if len(s) > 5 and s[-4] == s[-5]:
                s= s[:-4]
            else:
                s= s[:-3]           
        if s[-1] == 'e':
            s= s[:-1]
        if s[-1] == 'y':
            s= s[:-1] + 'i'
        if s[-3:] == 'ies':
            s= s[:-2]
        if s[-2:] == 'er':
            

            s= s[:-2]
        if s[-2:] == 'ed':
            s= s[:-2]
        if s[-3:] == 'ied':
            s= s[:-3] + 'y'
        if s[-3:] == 'est':
            s= s[:-3]
        if s[-4:] == 'iest':
            s= s[:-4] + 'y'
        if s[-3:] == 'ers':
            s= s[:-3]

        return s


##def sentencelen(s):
##    """calculates the length of a sentence, returns its length
##    """
##    x = s.split(' ')
##    return len(x)
    

def convos(s):
    """counts quotation marks
    """
    i = 0
    for x in s:
        if x == '"':
            i += 1

    return i // 2
        

def compare_dictionaries(d1, d2):
    """ compares 2 dics
    """
    i = 0
    for w in d1:
        i += d1[w]
    total = i
    if total == 0:
        total = 1

    
    log_sim_score = 0
    for q in d2:
        if q in d1:
            log_sim_score += d2[q] * math.log((d1[q])/total, 10)
        else:
            log_sim_score += (math.log(0.5/total, 10)) * d2[q]

    return log_sim_score
            
        

            
    
class TextModel:
    """class for a text model
    """

    def __init__(self, model_name):
        """ initialiser for the class
        """
        self.name = model_name
        self.words = {} 
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.my_dic = {}       # my own parameters for a dictionary


    def __repr__(self):
        """ new repr
        """
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of conversations: ' + str(self.my_dic)
        return s


    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
           to all of the dictionaries in this text model.
        """

        # Add code to clean the text and split it into a list of words.
        # *Hint:* Call one of your other methods!
        word_list = clean_text(s)
##        if s[-1] == '.':
##            dirty = s.split('.')       # what if there is only one sentence?
##        if s[-1] == '?':
##            dirty = s.split('?')
##        if s[-1] == '!':
##            dirty = s.split('!')
##        #dirty.remove('')
##        finaldirty = dirty

        # Template for updating the words dictionary.
   
        for word in word_list:          
            if word not in self.words:
                self.words[word] = 1
            else:
                self.words[word] += 1


        for word in word_list:
            if len(word) not in self.word_lengths:
                self.word_lengths[len(word)] = 1
            else:
                self.word_lengths[len(word)] += 1


        for word in word_list:
            if stem(word) not in self.stems:    
                self.stems[stem(word)] = 1
            else:
                self.stems[stem(word)] += 1
                
        p = s.split(' ')
        
        sentence_len = 1
        for sentence in p:
            if '.' in sentence or '?' in sentence or '!' in sentence or '."' in sentence:
                if sentence_len not in self.sentence_lengths:  # fix this 
                    self.sentence_lengths[sentence_len] = 1
                else:
                    self.sentence_lengths[sentence_len] += 1
            else:
                sentence_len += 1


        for word in p:
            
            if '"' in word:
                if '"' not in self.my_dic:
                    self.my_dic['"'] = 1
                else:
                    self.my_dic['"'] += 1
                    
    
            # Update self.words to reflect w
            # either add a new key-value pair for w
            # or update the existing key-value pair.

        # Add code to update other feature dictionaries.

    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the model.
        """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        list = f.read()
        self.add_string(list)


### BEGINNING OF PART 2


    def save_model(self):
        """saves the TextModel object self by
        writing its various feature dictionaries to files.
        """
        d = self.words
        e = self.word_lengths
        f = open(str(self.name) + '_' + 'words', 'w')      # works only if we enter string words
        g = open(str(self.name) + '_' + 'word_lengths', 'w')  
        f.write(str(d))
        g.write(str(e))
        f.close()
        g.close()


    def read_model(self):
        """reads the stored dictionaries for the called TextModel object from their
        files and assigns them to the attributes of the called TextModel.
        """
        f = open(str(self.name) + '_' + 'words', 'r')   # doesnt work for model2: memory location????
        g = open(str(self.name) + '_' + 'word_lengths', 'r')  #when read and print, it prints empty dictionary
        d_str = f.read()
        e_str = g.read()

        d = dict(eval(d_str))
        e = dict(eval(e_str))
        self.words = d
        self.word_lengths = e


        f.close()
        g.close()


    def similarity_scores(self, other):
        """returns a list of log similarity scores measuring similarity
            between self and other
        """
        word_score = []
        word_score += [compare_dictionaries(other.words, self.words)]  #10
        word_score += [compare_dictionaries(other.word_lengths, self.word_lengths)]   #10
        word_score += [compare_dictionaries(other.stems, self.stems)]   #10
        word_score += [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]   #50
        word_score += [compare_dictionaries(other.my_dic, self.my_dic)]    #20

        return word_score


    def classify(self, source1, source2):
        """compares self to two other source text model objects
            determining which of the two textmodels is more likely the source
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)

        print('scores for ' + source1.name + ': ' + str(scores1))
        print('scores for ' + source2.name + ': ' + str(scores2))

        weighted_sum1 = 10*scores1[0] + 10*scores1[1] + 10*scores1[2] + 50*scores1[3] + 20*scores1[4]
        weighted_sum2 = 10*scores2[0] + 10*scores2[1] + 10*scores2[2] + 50*scores2[3] + 20*scores1[4]

        if weighted_sum1 >= weighted_sum2:
            print(self.name + ' is more likely to have come from ' + str(source1.name))
        else:
            print(self.name + ' is more likely to have come from ' + str(source2.name))
            



def test():
    """ test ur functions of source 1 and 2 to teh mystery text """
    source1 = TextModel('source1')
    source1.add_string('"It is interesting that she is interested."')

    source2 = TextModel('source2')
    source2.add_string('"I am very, very excited about this!"')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)



        
              


    
        





    


    


        

    
        


    
        





    
