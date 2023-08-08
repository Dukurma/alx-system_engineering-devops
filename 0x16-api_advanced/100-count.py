!/usr/bin/python3
""" reddit api"""
import requests
import json

def count_words(subreddit, word_list, after=None):
    if after is None:
        count = {word: 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, params={'after': after}, headers={'user-agent': 'YourUserAgent'})

    if response.status_code == 200:
        data = response.json()
        
        for topic in data['data']['children']:
            title_words = topic['data']['title'].split()
            for word in title_words:
                word = word.lower()
                if word in count:
                    count[word] += 1

        after = data['data']['after']
        if after is None:
            sorted_results = sorted(count.items(), key=lambda x: (-x[1], x[0]))
            for word, word_count in sorted_results:
                if word_count > 0:
                    print(f"{word}: {word_count}")
        else:
            count_words(subreddit, word_list, after)

    else:
        print(f"Error: Request failed with status code {response.status_code}")

# Example usage
subreddit = "your_subreddit_name"
word_list = ["word1", "word2", "word3"]  # List of words to count
count_words(subreddit, word_list)

