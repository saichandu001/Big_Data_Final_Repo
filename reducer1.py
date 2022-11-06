#!/usr/bin/env python3
import sys

average_rate = []
global_dict = dict()

for line in sys.stdin:
    details = line.rstrip('\n').split("\t")
    test_year, campus_id, subject, prof, demog, num, den = details[0], details[1], details[2], details[3], details[4], details[5] ,details[6]

    if campus_id in global_dict.keys():
        
        if test_year not in global_dict[campus_id].keys():
            global_dict[campus_id][test_year] = dict()

        if subject not in global_dict[campus_id][test_year].keys():
            global_dict[campus_id][test_year][subject] = list()
        
        global_dict[campus_id][test_year][subject].append( int(num)/int(den))
    else:
        global_dict[campus_id] = dict()

# print(global_dict)

counter_greater = []
counter = 0
counter_lesser = []

agg_dict = dict()

for i in global_dict.keys():
    if i not in agg_dict.keys():
        agg_dict[i] = dict()
    for j in global_dict[i].keys():
        if j not in agg_dict[i].keys():
            summation = []
            length = []
            for k in global_dict[i][j].keys():
                summation.append(sum(global_dict[i][j][k]))
                length.append(len( global_dict[i][j][k]))       
            agg_dict[i][j] = sum(summation)/sum(length)


for i in agg_dict.keys():
    if len(agg_dict[i].keys()) > 1 :
        max_key = max( agg_dict[i].keys())
        min_key = min( agg_dict[i].keys())

        if agg_dict[i][max_key] >  agg_dict[i][min_key]:
            counter_greater.append(i)
        else:
            counter_lesser.append(i)
    else:
        for j in agg_dict[i].keys():
            if agg_dict[i][j]> 0.5:
                counter_greater.append(i)
            else:
                counter_lesser.append(i)

print( "Number of campuses where Success rate is greater from previous", len(counter_greater))
print("Number of campuses where Success rate is lesser from previous", len(counter_lesser))