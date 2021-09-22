import sys
path = sys.argv[1]

arr = []
with open(path, encoding="utf-8") as f:
  s = f.read()
  arr = s.split("======\n")

for i in range(len(arr)):
  with open('./CHAPTER-{}.md'.format(i+2), mode='w', encoding="utf-8") as f:
    f.write("  \n".join(arr[i].split('\n')))
  with open('./CHAPTER-{}.md'.format(i+2), encoding="utf-8") as f:
    print(f.read())
