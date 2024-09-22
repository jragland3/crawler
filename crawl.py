import requests, threading, os

# Remove previously generated text files if they exist
try:
  os.remove('urls.txt')
except:
  pass

# Wordlist to use in crawling
f = open('path-to-wordlist', 'r').read().splitlines()

with open('urls.txt', 'w') as result:
  # Thread functions
  def thread1():
    for i, val in enumerate(f):
      if i <= len(f)/4:
        r = requests.get(f'https://example.com/{val}')
        print(f'{val}: {r.status_code}')
        if r.status_code != 404:
          result.write(f'{r.url}: {r.status_code}\n')

  def thread2():
    for i, val in enumerate(f):
      if i > len(f)/4 and i <= len(f)*2/4:
        r = requests.get(f'https://example.com/{val}')
        print(f'{val}: {r.status_code}')
        if r.status_code != 404:
          result.write(f'{r.url}: {r.status_code}\n')

  def thread3():
    for i, val in enumerate(f):
      if i > len(f)*2/4 and i <= len(f)*3/4:
        r = requests.get(f'https://example.com/{val}')
        print(f'{val}: {r.status_code}')
        if r.status_code != 404:
          result.write(f'{r.url}: {r.status_code}\n')

  def thread4():
    for i, val in enumerate(f):
      if i > len(f)*3/4 and i <= len(f):
        r = requests.get(f'https://example.com/{val}')
        print(f'{val}: {r.status_code}')
        if r.status_code != 404:
          result.write(f'{r.url}: {r.status_code}\n')

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

result.close()
