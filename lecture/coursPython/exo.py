fruits=["pomme","pain","pomme","orange","pomme",
"pain"]
f={}
for c in fruits:
    f[c] = f.get(c, 0) + 1
for i in reversed(sorted(f.keys())):
    print(i,f.get(i))