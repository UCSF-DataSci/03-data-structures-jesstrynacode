#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "I don't understand dating.. and the other things that people do.. all I know is that you ought to find the one you recognize. The one who gives you four arms, four legs, four eyes, and has the other half of your heart. There's only one of those, so what are all the other things for? Like dating? - C. JoyBell C.",
    "Select your purpose … selfless, without any thought of personal pleasure or personal profit, and then use selfless means to attain your goal. - Gandhi",
    "If you are to have a great kingdom,” he said, “rule over yourself! - Publius Syrus",
    "It is easier to act yourself into a new way of thinking, than it is to think yourself into a new way of acting. - Millard Fuller",
    "If you can’t do the little things right, you will never do the big things right. -Naval Admiral William H. McRaven. McRaven is the commander of U.S. Special Operations, navy SEAL",
    "The world is moving so fast these days that the man who says it can't be done is generally interrupted by someone doing it. - Harry Emerson Fosdick, 1878 - 1969",
    "In life, we cannot always control the first arrow. However, the second arrow is our reaction to the first. The second arrow is optional.",
    "A good marriage is one in which each spouse secretly thinks he or she got the better deal, and this is true also of our friendships. - Anne Lamott",
    "Men seek for seclusion in the wilderness, by the seashore, or in the mountains - a dream you have cherished only too fondly yourself. But such fancies are wholly unworthy of a philosopher, since at any moment you choose you can retire within yourself. Nowhere can man find a quieter or more untroubled retreat than in his own soul; above all, he who possesses resources in himself, which he need only contemplate to secure immediate ease of mind - the ease that is but another word for a well-ordered spirit. Avail yourself often, then, of this retirement, and so continually renew yourself. - Marcus Aurelius",
    "We chase what's sexy and miss what matters.",
    "While excitement starts something, execution completes it.",
    "While speed makes a good story, velocity makes an outcome.",
    "While complexity makes you sound smart, focusing on the key basics matters more.",
    "While new commands our attention, nature offers insight.",
]

def get_quote_of_the_day(quotes):
    today = date.today()
    random.seed(today.toordinal())
    todays_quote = random.choice(quotes)
    
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt