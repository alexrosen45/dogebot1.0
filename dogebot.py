import tweepy
import re

class Dogebot:
    def __init__(self, keys_tokens, handle):
        self.API_key = keys_tokens[0]
        self.API_secret_key = keys_tokens[1]
        self.access_token = keys_tokens[2]
        self.access_token_secret = keys_tokens[3]
        self.handle = handle
        self.API = None
        self.last_tweet = None
        self.doge_present = False
        self.new_order = False
        self.error = False

        try:
            auth = tweepy.OAuthHandler(self.API_key, self.API_secret_key)
            auth.set_access_token(self.access_token, self.access_token_secret)
            self.API = tweepy.API(auth, wait_on_rate_limit=True)
        except tweepy.TweepError as e:
            print("ERROR: connection failed check OAuth keys and tokens")
            self.error = True
        else:
            print("authorized connection")

    def get_last_tweet(self):
        if self.error == False:
            try:
                # get last tweet
                self.last_tweet = self.API.user_timeline(screen_name=self.handle, count=1)[0]
                # cleaning the last tweet
                self.last_tweet.text = re.sub(r"@[A-Za-z0-9]+", "", self.last_tweet.text) # removes mentions
                self.last_tweet.text = re.sub(r"#", "", self.last_tweet.text) # removes hashtag symbol(s)
                self.last_tweet.text = re.sub(r"RT[\s]+", "", self.last_tweet.text) # removes retweets
                self.last_tweet.text = re.sub(r"https?:\/\/\S+", "", self.last_tweet.text) # removes hyperlinks
                self.last_tweet.text = re.sub(r"\W+", "", self.last_tweet.text) # only keeps numbers, letters, underscores

                if open("last_tweet.txt", "r").read() != str(self.last_tweet.text):
                    # remove encoding parameter for unicode
                    last_tweet_doc = open("last_tweet.txt", "wt")
                    last_tweet_doc.write(str(self.last_tweet.text))
                    last_tweet_doc.close()
                    self.new_order = True
                    print("new tweet")
                else:
                    print("same tweet")
            except IndexError:
                print("ERROR: could not retrieve tweet")
                self.error = True

    def doge_scan(self):
        if self.error == False:
            # checking for 'doge' substring
            if "doge" in self.last_tweet.text.lower():
                self.doge_present = True

    def buy(self):
        if self.error == False:
            print("order fulfilled")