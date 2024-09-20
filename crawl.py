import requests, threading, os, glob

# Remove previously generated text files if they exist
for f in glob.glob('q*.txt'):
  try:
    os.remove(f)
  except:
    pass

# Wordlist to use in crawling
f = open('path-to-wordlist', 'r').read().splitlines()

# Thread functions
def thread1():
  with open('q1.txt', 'w') as result:
    for i, val in enumerate(f):
      if i <= len(f)/4:
        r = requests.get(f'https://example.com/{val}')
        print(f'{val}: {r.status_code}')
        if r.status_code == 200 or r.status_code == 403:
          result.write(f'{r.url}: {r.status_code}\n')
  result.close()

def thread2():
  with open('q2.txt', 'w') as result:
    for i, val in enumerate(f):
      if i > len(f)/4 and i <= len(f)*2/4:
        r = requests.get(f'https://example.com/{val}')
        print(f'{val}: {r.status_code}')
        if r.status_code == 200 or r.status_code == 403:
          result.write(f'{r.url}: {r.status_code}\n')
  result.close()

def thread3():
  with open('q3.txt', 'w') as result:
    for i, val in enumerate(f):
      if i > len(f)*2/4 and i <= len(f)*3/4:
        r = requests.get(f'https://example.com/{val}')
        print(f'{val}: {r.status_code}')
        if r.status_code == 200 or r.status_code == 403:
          result.write(f'{r.url}: {r.status_code}\n')
  result.close()

def thread4():
  with open('q4.txt', 'w') as result:
    for i, val in enumerate(f):
      if i > len(f)*3/4 and i <= len(f):
        r = requests.get(f'https://example.com/{val}')
        print(f'{val}: {r.status_code}')
        if r.status_code == 200 or r.status_code == 403:
          result.write(f'{r.url}: {r.status_code}\n')
  result.close()

# Threads
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t3 = threading.Thread(target=thread3)
t4 = threading.Thread(target=thread4)

# Start threads
t1.start()
t2.start()
t3.start()
t4.start()

# Close threads on completion
t1.join()
t2.join()
t3.join()
t4.join()
