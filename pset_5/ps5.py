# 6.00 Problem Set 5
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from news_gui import Popup

#-----------------------------------------------------------------------
#
# Problem Set 5

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory(object):

    def __init__(self, guid, title, subject, summary, link):
        """
        Constructor

        guid: string
        title: string
        subject: string
        summary: string
        link: string

        Return : None
        """
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        """
        return : string
        """
        return self.guid

    def get_title(self):
        """
        return : string
        """
        return self.title

    def get_subject(self):
        """
        return : string
        """
        return self.subject

    def get_summary(self):
        """
        return : string
        """
        return self.summary

    def get_link(self):
        """
        return : string
        """
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):

    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        pass


# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):

    def __init__(self, word):
        """
        word : string
        """
        self.word = word.lower()

    def get_word(self):
        """
        return : string
        """
        return self.word

    def is_word_in(self, text):
        """
        text: string

        return: boolean
        """
        trig_word = self.get_word()
        text = text.lower()
        words = text.split(" ") 
        words = [word[:word.index("'")] if "'" in word else word for word in words] # remove apostrophes
        equals_word = [trig_word == string.strip(word,string.punctuation) for word in words] # strip punctuation
        return any(equals_word)

class TitleTrigger(WordTrigger):

    def __init__(self,word):
        """
        word : string
        """
        self.word = word.lower()

    def evaluate(self,story):
        """
        story : NewsStory object
        """
        return self.is_word_in(story.get_title())


class SubjectTrigger(WordTrigger):

    def __init__(self,word):
        """
        word : string
        """
        self.word = word.lower()

    def evaluate(self,story):
        """
        story : NewsStory object
        """
        return self.is_word_in(story.get_subject())

class SummaryTrigger(WordTrigger):

    def __init__(self,word):
        """
        word : string
        """
        self.word = word.lower()

    def evaluate(self,story):
        """
        story : NewsStory object
        """
        return self.is_word_in(story.get_summary())

class NotTrigger(Trigger):

    def __init__(self,trigger):
        """
        other_trigger : object of class Trigger or one of its child classes
        """
        self.trigger = trigger

    def get_trigger(self):
        """
        return : trigger object
        """
        return self.trigger

    def evaluate(self,story):
        """
        story : NewsStory object

        return : boolean
        """
        return not (self.get_trigger()).evaluate(story)


class AndTrigger(Trigger):

    def __init__(self,trigger1,trigger2):
        """
        trigger1: object of class Trigger or one of its child classes
        trigger2: object of class Trigger or one of its child classes
        """
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def get_trigger1(self):
        """
        return : Trigger
        """
        return self.trigger1

    def get_trigger2(self):
        """
        return : Trigger
        """
        return self.trigger2

    def evaluate(self,story):
        """
        story : NewsStory 

        return : boolean
        """
        return (self.get_trigger1()).evaluate(story) and (self.get_trigger2()).evaluate(story)

class OrTrigger(Trigger):

    def __init__(self,trigger1,trigger2):
        """
        trigger1: object of class Trigger or one of its child classes
        trigger2: object of class Trigger or one of its child classes
        """
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def get_trigger1(self):
        """
        return : Trigger
        """
        return self.trigger1

    def get_trigger2(self):
        """
        return : Trigger
        """
        return self.trigger2

    def evaluate(self,story):
        """
        story : NewsStory 

        return : boolean
        """
        return (self.get_trigger1()).evaluate(story) or (self.get_trigger2()).evaluate(story)


class PhraseTrigger(Trigger):

    def __init__(self, phrase):
        """
        phrase: string
        """
        self.phrase = phrase

    def get_phrase(self):
        """
        return : string
        """
        return self.phrase

    def evaluate(self, story):
        """
        story : NewsStory
        return : boolean
        """
        phrase = self.get_phrase()
        return phrase in story.get_title() or phrase in story.get_summary() or phrase in story.get_subject() 




#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.

    stories : list of NewsStory
    triggerlist : list of Trigger

    return : list
    """

    triggered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                triggered_stories.append(story)
                break
    return triggered_stories




#======================
# Part 4
# User-Specified Triggers
#======================

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """
    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    trigger_set = {}
    keep_these = []

    for line in lines:
        elements = line.split(" ")
        if elements[1] == "TITLE":
            trigger_set[elements[0]] = TitleTrigger(elements[2])
        elif elements[1] == "SUBJECT":
            trigger_set[elements[0]] = SubjectTrigger(elements[2])
        elif elements[1] == "SUMMARY": 
            trigger_set[elements[0]] = SummaryTrigger(elements[2])
        elif elements[1] == "PHRASE":
            trigger_set[elements[0]] = PhraseTrigger(" ".join(elements[2:]))
        elif elements[1] == "NOT":
            trigger_set[elements[0]] = NotTrigger(trigger_set[elements[2]])
        elif elements[1] == "AND":
            trigger_set[elements[0]] = AndTrigger(trigger_set[elements[2]], trigger_set[elements[3]])
        elif elements[1] == "OR":
            trigger_set[elements[0]] = OrTrigger(trigger_set[elements[2]], trigger_set[elements[3]])
        else:
            for index in range(1,len(elements)):
                keep_these.append(trigger_set[elements[index]])

    return keep_these
    


    
import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
     
    triggerlist = readTriggerConfig("triggers.txt")

    guidShown = []
    
    while True:
        print "Polling..."

        # Get stories from Google's Top Stories RSS news feed
        stories = process("http://news.google.com/?output=rss")
        # Get stories from Yahoo's Top Stories RSS news feed
        stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

        # Only select stories we're interested in
        stories = filter_stories(stories, triggerlist)
    
        # Don't print a story if we have already printed it before
        newstories = []
        for story in stories:
            if story.get_guid() not in guidShown:
                newstories.append(story)
        
        for story in newstories:
            guidShown.append(story.get_guid())
            p.newWindow(story)

        print "Sleeping..."
        time.sleep(SLEEPTIME)

SLEEPTIME = 60 #seconds -- how often we poll
if __name__ == '__main__':
    p = Popup()
    thread.start_new_thread(main_thread, (p,))
    p.start()

