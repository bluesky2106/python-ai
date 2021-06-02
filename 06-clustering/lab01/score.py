import numpy as np

def calculate_distance_table(docs):
    distances = dict()
    keys = sorted(docs.keys())
    n = len(keys)
    for i, k1 in enumerate(keys):
        for j in range(i+1, n):
            k2 = keys[j]
            s = str(k1) + '-' + str(k2)
            distances[s] = np.linalg.norm(docs[k1] - docs[k2])
    return distances

def calculate_average_distance_from_2_groups(group1, group2, dTable):
    sum = 0.0
    num = 0
    for k1 in group1:
        for k2 in group2:
            if k1 < k2:
                s = str(k1) + '-' + str(k2)
            else:
                s = str(k2) + '-' + str(k1)
            sum += dTable[s]
            num += 1
    return sum/num

def enter_group():
    s = input('Enter the first group : ')
    l = []
    if type(s) == tuple:
        l = [int(i) for i in s]
    elif type(s) == int:
        l = [s]
    return l

def init_documents():
    documents = dict()
    documents[1] = np.array([2.25349666421154, 1.28771237954945, 0.15200309344505, 0.514573172829758, 0], dtype=np.float64)
    documents[2] = np.array([1.28771237954945, 0.965784284662087, 0.6080123737802, 2.57286586414879, 0], dtype=np.float64)
    documents[3] = np.array([0, 0, 0.9120185606703, 4.11658538263807, 0], dtype=np.float64)
    documents[4] = np.array([0.965784284662087, 0.965784284662087, 0.45600928033515, 1.54371951848927, 3], dtype=np.float64)
    documents[5] = np.array([0.321928094887362, 0.643856189774725, 1.67203402789555, 0, 0], dtype=np.float64)
    documents[6] = np.array([0.321928094887362, 0, 0, 3.60201220980831, 3], dtype=np.float64)
    documents[7] = np.array([0, 2.5754247590989, 0.3040061868901, 0, 4], dtype=np.float64)
    documents[8] = np.array([1.60964047443681, 0.965784284662087, 0.15200309344505, 0, 7], dtype=np.float64)
    documents[9] = np.array([0.965784284662087, 0.321928094887362, 0.15200309344505, 0, 5], dtype=np.float64)
    documents[10] = np.array([0.321928094887362, 1.28771237954945, 0.45600928033515, 1.54371951848927, 0], dtype=np.float64)
    return documents

docs = init_documents()
# print(docs)
distance_table = calculate_distance_table(docs)

group1 = enter_group()
group2 = enter_group()
group3 = enter_group()
# print(group1)
# print(group2)
# print(group3)

evaluation = dict()

if len(group1) == 1:
    evaluation[group1[0]] = 0
else:
    for idx, doc in enumerate(group1):
        evaluation[doc] = []
        remain = group1[:]
        del remain[idx]
        internal_distance = calculate_average_distance_from_2_groups([doc], remain, distance_table)
        external_distance1 = calculate_average_distance_from_2_groups([doc], group2, distance_table)
        external_distance2 = calculate_average_distance_from_2_groups([doc], group3, distance_table)
        external_distance = min(external_distance1, external_distance2)
        s = (external_distance - internal_distance) / max(internal_distance, external_distance)
        evaluation[doc] = s

if len(group2) == 1:
    evaluation[group2[0]] = 0
else:
    for idx, doc in enumerate(group2):
        evaluation[doc] = []
        remain = group2[:]
        del remain[idx]
        internal_distance = calculate_average_distance_from_2_groups([doc], remain, distance_table)
        external_distance1 = calculate_average_distance_from_2_groups([doc], group1, distance_table)
        external_distance2 = calculate_average_distance_from_2_groups([doc], group3, distance_table)
        external_distance = min(external_distance1, external_distance2)
        s = (external_distance - internal_distance) / max(internal_distance, external_distance)
        evaluation[doc] = s

if len(group3) == 1:
    evaluation[group3[0]] = 0
else:
    for idx, doc in enumerate(group3):
        evaluation[doc] = []
        remain = group3[:]
        del remain[idx]
        internal_distance = calculate_average_distance_from_2_groups([doc], remain, distance_table)
        external_distance1 = calculate_average_distance_from_2_groups([doc], group1, distance_table)
        external_distance2 = calculate_average_distance_from_2_groups([doc], group2, distance_table)
        external_distance = min(external_distance1, external_distance2)
        s = (external_distance - internal_distance) / max(internal_distance, external_distance)
        evaluation[doc] = s

print(evaluation)
print(sum(evaluation.values())/len(evaluation))