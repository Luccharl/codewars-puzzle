aLAHLYGoals = [6,4]
zamalekGoals = [1,2]
new_diff = None
diffs = []
for num in range(len(aLAHLYGoals)):
    diff = aLAHLYGoals[num] - zamalekGoals[num]
    if new_diff is None or new_diff > diff:
        new_diff = diff
    if diff not in diffs:
        diffs.append(diff)
              
if len(diffs) > 1:
    print(diffs.index(new_diff))
else:     
    zamalekGoals.sort()
    print(zamalekGoals.index(zamalekGoals[-1]))