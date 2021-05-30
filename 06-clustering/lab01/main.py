import numpy as np
from numpy.lib.function_base import append

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
# print(docs.keys())

def calculate_center(group, docs):
    center = []
    for k in group:
        if len(center) == 0:
            center.append(docs[k])
        else:
            center += docs[k]
    center = center / np.float64(len(group))
    return center

# center = calculate_center([1,2,3], docs)
# print(center)

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

# dTable = calculate_distance_table(docs)

def calculate_distance_from_2_groups(group1, group2, dTable, docs=None, method=0):
    # single link : min distance
    if method == 0:
        dist = 1.7976931348623157e+308
        for k1 in group1:
            for k2 in group2:
                if k1 < k2:
                    s = str(k1) + '-' + str(k2)
                else:
                    s = str(k2) + '-' + str(k1)
                if dist > dTable[s]:
                    dist = dTable[s]
        return dist

    # complete link : min distance
    if method == 1:
        dist = -1.7976931348623157e+308
        for k1 in group1:
            for k2 in group2:
                if k1 < k2:
                    s = str(k1) + '-' + str(k2)
                else:
                    s = str(k2) + '-' + str(k1)
                if dist < dTable[s]:
                    dist = dTable[s]
        return dist

    # dist average
    if method == 2:
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

    # group average
    if method == 3:
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
        if len(group1) > 1:
            l = len(group1)
            for i in range(0, l):
                for j in range(i+1, l):
                    if group1[i] < group1[j]:
                        s = str(group1[i]) + '-' + str(group1[j])
                    else:
                        s = str(group1[j]) + '-' + str(group1[i])
                    sum += dTable[s]
                    num += 1
        if len(group2) > 1:
            l = len(group2)
            for i in range(0, l):
                for j in range(i+1, l):
                    if group2[i] < group2[j]:
                        s = str(group2[i]) + '-' + str(group2[j])
                    else:
                        s = str(group2[j]) + '-' + str(group2[i])
                    sum += dTable[s]
                    num += 1
        return sum/num

    # dist centroid : calculate distance of 2 centers
    if method == 4:
        center1 = calculate_center(group1, docs)
        center2 = calculate_center(group2, docs)
        return np.linalg.norm(center1 - center2)


# dist = calculate_distance_from_2_groups([1,2,3], [4,5,6], dTable)
# print(dist)


def grouping(docs, method=0):
    group = []
    for k in sorted(docs.keys()):
        group.append([k])
    print(group)

    distance_table = calculate_distance_table(docs)
    num = len(docs)
    for _ in range(1, num):
        min_dist = 1.7976931348623157e+308
        kmin = ''
        group_length = len(group)
        for i in range(0, group_length):
            for j in range(i+1, group_length):
                dist = calculate_distance_from_2_groups(group[i], group[j], distance_table, docs, method)
                if min_dist > dist:
                    kmin = str(i) + '-' + str(j)
                    min_dist = dist
        # print(kmin, min_dist)
        ss = kmin.split('-')
        i = int(ss[0])
        j = int(ss[1])
        # print(i, j)
        gi = group[i]
        gj = group[j]
        group.remove(gi)
        group.remove(gj)
        gi.extend(gj)
        group.append(gi)
        print(group, ':', min_dist)

print("---------- Single link ----------")
grouping(docs, 0)

print("---------- Complete link ----------")
grouping(docs, 1)

print("---------- Dist Average ----------")
grouping(docs, 2)

print("---------- Group Average ----------")
grouping(docs, 3)

print("---------- Dist Centroid ----------")
grouping(docs, 4)