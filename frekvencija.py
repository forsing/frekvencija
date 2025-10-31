from __future__ import absolute_import, division, print_function, unicode_literals


"""
Loto Skraceni Sistemi 
https://www.lotoss.info
ABBREVIATED LOTTO SYSTEMS
"""


import pandas as pd

"""
svih 4502 izvlacenja
30.07.1985.- 28.10.2025.
"""

df = pd.read_csv("/data/loto7_4502_k85.csv", header=None)
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



30 : 760
17 : 749
20 : 746
"""


#########################################


dfh = pd.read_csv("/data/loto7h_4502_k85.csv")


from collections import Counter

all_numbers_h = dfh[['Num1', 'Num2', 'Num3', 'Num4', 'Num5', 'Num6', 'Num7']].values.flatten()


counter_h = Counter(all_numbers_h)


top_39_h = counter_h.most_common(39)
print()
print("svih 4502 izvlacenja")
print("30.07.1985.- 28.10.2025.")
print()
for num, cnt in top_39_h:
    print(f"{num}: {cnt}")
print()
"""
svih 4502 izvlacenja
30.07.1985.- 28.10.2025.

8: 886
23: 884
26: 855



30: 760
17: 749
20: 746
"""








"""
=== Qiskit Version Table ===
Software                       Version        
---------------------------------------------
qiskit                         1.4.4          
qiskit_machine_learning        0.8.3          

=== System Information ===
Python version                 3.11.13        
OS Apple                       Darwin 
"""


