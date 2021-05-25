import math

def count_letter(word, char):
  count = 0
  for c in word:
    if c == char:
      count += 1
  return count

def SatisfyRequirement(word):
  if count_letter(word, 'A') < 3 or count_letter(word, 'B') < 3:
    return False
  if abs(count_letter(word, 'A') - count_letter(word, 'B')) > 2:
    return False

  return True

doc1 = 'AABAAABBBAACD'
doc2 = 'ACDAAABBBCCCDDD'
doc3 = 'CCDDDCDDDDDCCC'
doc4 = 'ABCDEABCDEABCDE'
doc5 = 'ABCCCCCCCCCCBC'
doc6 = 'DEADEADDDDDE'
doc7 = 'BEBBBBEEECBBBC'
doc8 = 'ABCAAAABBE'
doc9 = 'AEEEEABCEEA'
doc10 = 'ABCBCBCBCDDD'

actual_labels = dict()
actual_labels['doc1'] = True
actual_labels['doc2'] = True
actual_labels['doc3'] = True
actual_labels['doc4'] = True
actual_labels['doc5'] = True
actual_labels['doc6'] = True
actual_labels['doc7'] = True
actual_labels['doc8'] = True
actual_labels['doc9'] = True
actual_labels['doc10'] = True

if not SatisfyRequirement(doc1):
  actual_labels['doc1'] = False
if not SatisfyRequirement(doc2):
  actual_labels['doc2'] = False
if not SatisfyRequirement(doc3):
  actual_labels['doc3'] = False
if not SatisfyRequirement(doc4):
  actual_labels['doc4'] = False
if not SatisfyRequirement(doc5):
  actual_labels['doc5'] = False
if not SatisfyRequirement(doc6):
  actual_labels['doc6'] = False
if not SatisfyRequirement(doc7):
  actual_labels['doc7'] = False
if not SatisfyRequirement(doc8):
  actual_labels['doc8'] = False
if not SatisfyRequirement(doc9):
  actual_labels['doc9'] = False
if not SatisfyRequirement(doc10):
  actual_labels['doc10'] = False

print(actual_labels)

predict_labels = dict()
predict_labels['doc1'] = True
predict_labels['doc2'] = False
predict_labels['doc3'] = False
predict_labels['doc4'] = False
predict_labels['doc5'] = True
predict_labels['doc6'] = False
predict_labels['doc7'] = False
predict_labels['doc8'] = True
predict_labels['doc9'] = False
predict_labels['doc10'] = False

print(predict_labels)


def true_positivve(actual, predict):
    cnt = 0.0
    for doc in actual:
        if actual[doc] == True and predict[doc] == True:
            cnt += 1
    return cnt

def true_negative(actual, predict):
    cnt = 0.0
    for doc in actual:
        if actual[doc] == False and predict[doc] == False:
            cnt += 1
    return cnt

def false_positive(actual, predict):
    cnt = 0.0
    for doc in actual:
        if actual[doc] == False and predict[doc] == True:
            cnt += 1
    return cnt

def false_negative(actual, predict):
    cnt = 0.0
    for doc in actual:
        if actual[doc] == True and predict[doc] == False:
            cnt += 1
    return cnt

def recal(actual, predict):
    tp = true_positivve(actual, predict)
    fn = false_negative(actual, predict)
    return tp / (tp + fn)

def precision(actual, predict):
    tp = true_positivve(actual, predict)
    fp = false_positive(actual, predict)
    return tp / (tp + fp)

def fmeasure(actual, predict):
    r = recal(actual, predict)
    p = precision(actual, predict)
    return  (2 * r * p) / (r + p)

print("true_positivve:", true_positivve(actual_labels, predict_labels))
print("true_negative:", true_negative(actual_labels, predict_labels))
print("false_positive:", false_positive(actual_labels, predict_labels))
print("false_negative:", false_negative(actual_labels, predict_labels))
print("recal:", recal(actual_labels, predict_labels))
print("precision:", precision(actual_labels, predict_labels))
print("fmeasure:", fmeasure(actual_labels, predict_labels))