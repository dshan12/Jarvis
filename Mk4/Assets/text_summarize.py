import argparse
from summarizer import Summarizer


def text_summarize(text_0, **kwargs):
    """
    Summarize the given text. Returns the summarize
    """
    model = Summarizer()
    return model(text_0, **kwargs)


def main(text_file):
    global text

    with open(text_file, 'r') as infile:
        text = infile.readlines()
        text = "\n".join(text)

    summary = text_summarize(text, ratio=args.ratio)
    with open('output.txt', 'w') as outfile:
        outfile.write(summary)
        outfile.write("\n")
