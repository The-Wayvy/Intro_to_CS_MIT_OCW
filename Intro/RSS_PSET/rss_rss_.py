

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
import string
class NewsStory(object):
    def __init__(self,guid,title,subject,summary,link):
        """initializes a NewsStory object.
        all parameters must be strings"""
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def get_guid(self):
        """returns guid string"""
        return self.guid
    def get_title(self):
        """returns title string"""
        return self.title
    def get_subject(self):
        """returns subject string"""
        return self.subject
    def get_summary(self):
        """returns summary string"""
        return self.summary
    def get_link(self):
        """returns link string"""
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
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self,word):
        """initializes WordTrigger object
        word must be a string"""
        self.trigger_word = word

    def is_word_in(self,text):
        """Returns True is trigger word is in text, false otherwise
        text: string"""

        words = text.split()
        for word in words:
            word = word.strip(string.punctuation)
            if '\'' in word:
                word = word[:word.index('\'')]
            word = word.lower()
            if word == self.trigger_word:
                return True
            word = word.upper()
            if word == self.trigger_word:
                return True
            word = word.capitalize()
            if word == self.trigger_word:
                return True
        else:
            return False


class TitleTrigger(WordTrigger):


    def evaluate(self,story):
        """Returns True if an alert should be generated, false otherwise
        story: NewsStory object
        """
        if self.is_word_in(story.get_title()):
            return True
        else:
            return False



class SubjectTrigger(WordTrigger):

    def evaluate(self,story):
        """Returns True if an alert should be generated, false otherwise
        story: NewsStory object
        """
        if self.is_word_in(story.get_subject()):
            return True
        else:
            return False

class SummaryTrigger(WordTrigger):

    def evaluate(self,story):
        """Returns True if an alert should be generated, false otherwise
        story: NewsStory object
        """
        if self.is_word_in(story.get_summary()):
            return True
        else:
            return False



# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger):
    def __init__(self,a_trigger):
        """Initializes NotTrigger object
        a_trigger = instance of WordTrigger object
        item = string
        """
        self.a_trigger = a_trigger

    def evaluate(self,item):
        """Returns True if string 'i' does not set off WordTrigger 'trig', false otherwise
        trig: WordTrigger instance
        i: string"""

        return not self.a_trigger.evaluate(item)
"""
koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
tit_trig = TitleTrigger('SOFT')
not_not = NotTrigger(tit_trig,koala)
print not_not.evaluate()
"""

class AndTrigger(Trigger):
    def __init__(self,first_trigger,second_trigger):
        """Initializes AndTrigger object
        first_trigger: WordTrigger instance
        second_trigger: WordTrigger instance
        """
        self.first_trigger = first_trigger
        self.second_trigger = second_trigger


    def evaluate(self,text):
        """Returns True if string "text" sets off both triggers, returns False otherwise
        text: string"""
        return self.first_trigger.evaluate(text) and self.second_trigger.evaluate(text)


class OrTrigger(Trigger):
    def __init__(self,first_trigger,second_trigger):
        """Initializes OrTrigger object
        first_trigger: WordTrigger instance
        second_trigger: WordTrigger instance
        """
        self.first_trigger = first_trigger
        self.second_trigger = second_trigger


    def evaluate(self,text):
        """Returns True if string "text" sets off either triggers, returns False otherwise
        text: string"""
        return self.first_trigger.evaluate(text) or self.second_trigger.evaluate(text)


class PhraseTrigger(Trigger):
    def __init__(self,phrase):
        """initializes phrase trigger object
        phrase: string"""
        self.trigger_phrase = phrase

    def is_phrase_in(self,text):
        """Returns True if trigger phrase is in text, false otherwise
        text: string"""
        return self.trigger_phrase in text

    def evaluate(self,story):
        """Returns True if string 'phrase' sets off a title, summary or subject trigger.
        story: NewsStory object"""
        return self.is_phrase_in(story.get_title()) or self.is_phrase_in(story.get_subject()) or self.is_phrase_in(story.get_summary())

#======================
# Part 3
# Filtering
#======================

def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory-s.
    Returns only those stories for whom
    a trigger in triggerlist fires.
    """
    interesting = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                interesting.append(story)
                break
    return interesting

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
    
    for line in lines:
        print line

    all_triggers = {}
    to_return = {}
    for line in lines:
        line = line.split()
        print line
        if line[1] == 'SUBJECT':
            all_triggers[line[0]] = SubjectTrigger(line[2])
        elif line[1] == 'TITLE':
            all_triggers[line[0]] = TitleTrigger(line[2])
        elif line[1] == 'SUMMARY':
            all_triggers[line[0]] = SummaryTrigger(line[2])
        elif line[1] == 'PHRASE':
            all_triggers[line[0]] = PhraseTrigger(' '.join(line[2:]))
        elif line[1] == 'NOT':
            all_triggers[line[0]] = NotTrigger(all_triggers[line[2]])
        elif line[1] == 'OR':
            all_triggers[line[0]] = OrTrigger(all_triggers[line[2]],all_triggers[line[3]])
        elif line[1] == 'AND':
            all_triggers[line[0]] = AndTrigger(all_triggers[line[2]],all_triggers[line[3]])
        elif line[0] == 'ADD':
            for trig in line[1:]:
                to_return[trig] = all_triggers[trig]
    trig_list = []
    for trig in to_return:
        trig_list.append(to_return[trig])
    return trig_list



    # TODO: Problem 11
    # 'lines' has a list of lines you need to parse
    # Build a set of triggers from it and
    # return the appropriate ones

import thread

def main_thread(p):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    """
    t1 = SubjectTrigger("Obama")
    t2 = SummaryTrigger("MIT")
    t3 = PhraseTrigger("Supreme Court")
    t4 = OrTrigger(t2, t3)
    triggerlist = [t1, t4]
    """
    # TODO: Problem 11
    # After implementing readTriggerConfig, uncomment this line
    triggerlist = readTriggerConfig("C:/Users/Damian of Brooklyn/My Documents/MIT_Psets/RSS_PSET/triggers.txt")

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


