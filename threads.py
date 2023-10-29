from threads_interface import ThreadsInterface

scraper = ThreadsInterface()
id=''
user_id = scraper.retrieve_user_id(id)
id=''
user_id = scraper.retrieve_user_id(id)
user_data = scraper.retrieve_user_threads(user_id)
threads=user_data['data']['mediaData']['threads']
captions=[]
for thread in threads:
    captions.append(thread['thread_items'][0]['post']['caption']['text'])
with open('threads_data.txt','+wt') as f:
    for caption in captions:
        f.write(caption+"\n")