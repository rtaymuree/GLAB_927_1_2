# GLAB 927.1.2
## What I Used

NLTK is a Python toolkit for working with human language. Tokenization splits text into smaller pieces, such as words. Stemming shortens words by removing endings, while lemmatization looks for a dictionary form.

## What I Learned

I learned how to process email text with NLTK and compare stemming with lemmatization. In my results, stemming sometimes made shortened forms that were not real words, while lemmatization could return a dictionary form. I also saw that setting `pos="v"` changed “running” to “run.”
This project uses Python and NLTK to process sample business emails. I tokenize the email text, then apply stemming and lemmatization to compare how each method changes the words.
Stemming shortens words by removing endings, so the result is not always a real word. Lemmatization uses a dictionary to find a base word, such as changing “children” to “child.”
Lemmatization is more likely to return a real dictionary word. For example, it changes “children” to “child.” Stemming may simply chop off an ending, as it does when it changes “studies” to “studi.”
Lemmatization is more likely to return a dictionary word, while stemming is a simpler way to match related words. Which one is better depends on how the text will be used.
Lemmatization turns different forms of a word (like ran, running, runs) into one real root word (run).

This reduces clutter, keeps total word counts accurate, and helps models understand true meaning without losing context.
he pos argument changes the result by telling the lemmatizer what role the word plays in a sentence.Without it, the lemmatizer assumes every word is a noun by default. Setting the pos tag forces it to look in the correct dictionary category:As a Noun (pos='n'): leaves $\rightarrow$ leafAs a Verb (pos='v'): leaves $\rightarrow$ leaveSpecifying the pos argument ensures words like running get converted to base verbs (run) instead of being treated as unchanged nouns (running).

## Setup and Run

From the project folder, run:

```bash
uv sync
uv run python src/glab_927_1_2/email_processing.pyS
```