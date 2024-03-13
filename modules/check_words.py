import enchant
import re


def check_english(text):
    # Initialize an English dictionary
    d = enchant.Dict("en_US")

    # Remove non-alphabetic characters from the text
    text = re.sub('[^A-Za-z ]+', '', text)
    
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    # Determine the number of words to check (up to a threshold of last 100 words)
    threshold = min(100, len(words))
    
    # Use a set for efficient lookup and to remove duplicates within the threshold
    unique_words = set(words[-threshold:])
    
    # Count the number of words in the set that are recognized as English
    count = sum(1 for word in unique_words if d.check(word))
    
    # Determine if at least 50% of the words checked are English
    # If the total number of words is less than the threshold, all words are checked
    return count / threshold >= 0.5
