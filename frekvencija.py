from __future__ import absolute_import, division, print_function, unicode_literals

# https://github.com/you22fy/loto6_prediction/blob/main/frequency/note.ipynb

import pandas as pd


import pandas as pd

df = pd.read_csv("/Users/milan/Desktop/GHQ/data/loto7_4502_k85.csv", header=None)
print()
print(df.head())
print()
"""
    0   1   2   3   4   5   6
0   5  14  15  17  28  30  34
1   2   3  13  18  19  23  37
2  13  17  18  20  21  26  39
3  17  20  23  26  35  36  38
4   3   4   8  11  29  32  37
"""

print()
print(df.tail())
print()
"""
      0   1   2   3   4   5   6
4495  7  11  16  18  29  31  36
4496  4   5   6  15  23  26  36
4497  4  13  14  19  27  35  37
4498  1   7  13  18  25  30  34
4499  1   5   6   7  11  24  37
"""



counter = {k:0 for k in range(1,40)}

for i in range(len(df)):
    for item in list(df.iloc[i]):
        counter[item] += 1
print()
for k, v in counter.items():
    print(f'{k} : {v}')
print()
"""
1 : 762
2 : 800
3 : 805
4 : 791
5 : 801
6 : 790
7 : 821
8 : 886
9 : 818
10 : 824
11 : 831
12 : 796
13 : 801
14 : 776
15 : 784
16 : 808
17 : 749
18 : 796
19 : 786
20 : 746
21 : 805
22 : 831
23 : 884
24 : 811
25 : 824
26 : 855
27 : 764
28 : 800
29 : 820
30 : 760
31 : 804
32 : 839
33 : 829
34 : 842
35 : 817
36 : 766
37 : 837
38 : 816
39 : 825
"""

import matplotlib.pyplot as plt

x = counter.keys()
y = counter.values()

plt.bar(x, y, width=0.75)
plt.show()
# >>>

sorted_counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
print()
for k, v in sorted_counter.items():
    print(f'{k} : {v}')
print()
"""
8 : 886
23 : 884
26 : 855
34 : 842
32 : 839
37 : 837
11 : 831
22 : 831
33 : 829
39 : 825
10 : 824
25 : 824
7 : 821
29 : 820
9 : 818
35 : 817
38 : 816
24 : 811
16 : 808
3 : 805
21 : 805
31 : 804
5 : 801
13 : 801
2 : 800
28 : 800
12 : 796
18 : 796
4 : 791
6 : 790
19 : 786
15 : 784
14 : 776
36 : 766
27 : 764
1 : 762
30 : 760
17 : 749
20 : 746
"""


#########################################


dfh = pd.read_csv("/Users/milan/Desktop/GHQ/data/loto7h_4502_k85.csv")


from collections import Counter

all_numbers_h = dfh[['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', 'Num7']].values.flatten()


counter_h = Counter(all_numbers_h)


top_39_h = counter_h.most_common(39)
print()
print("4502 izvlacenja")
print("30.07.1985.- 28.10.2025.")
print()
for num, cnt in top_39_h:
    print(f"{num}: {cnt}")
print()
"""
4502 izvlacenja
30.07.1985.- 28.10.2025.

    8: 886
    23: 884
    26: 855
    34: 842
        32: 839
    37: 837
        11: 833
        22: 831
        33: 830
39: 825
    10: 824
    25: 824
        7: 821
        29: 820
35: 819
9: 818
        38: 817
    24: 811
    16: 808
3: 806
    21: 806
31: 804
        5: 801
        2: 801
13: 801
28: 800
        12: 797
18: 796
4: 792
6: 791
        19: 787
15: 784
    14: 776
36: 766
    27: 764
1: 763
        30: 760
    17: 749
        20: 746
"""

