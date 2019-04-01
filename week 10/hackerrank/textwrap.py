import textwrap

def wrap(string, max_width):
  string=textwrap.wrap(string,max_width)
  res=""
  for i in range(len(string)):
    res+=string[i]+"\n"
  return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)