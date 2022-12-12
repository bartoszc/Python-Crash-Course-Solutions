# FIRST STAR
# with open('Chapter 9\\input.txt', 'r') as f:
#     # ✅ get list of all lines
#     lines = f.read()

# for i in range(len(lines)):
#     nl = list(lines[i:i+4])
#     if len(set(nl)) == 4:
#         print(lines.index(''.join(nl)) + len(nl))
#         break

# SECOND STAR
with open('Chapter 9\\input.txt', 'r') as f:
    # ✅ get list of all lines
    lines = f.read()

for i in range(len(lines)):
    nl = list(lines[i:i+14])
    if len(set(nl)) == 14:
        print(lines.index(''.join(nl)) + len(nl))
        break
