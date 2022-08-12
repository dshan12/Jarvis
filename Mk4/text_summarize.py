import argparse
from summarizer import Summarizer


def text_summarize(text, **kwargs):
    """
    Summarize the given text. Returns the summarize
    """
    model = Summarizer()
    return model(text, **kwargs)


def main():
    parser = argparse.ArgumentParser(
        description='Summarize the given text')
    parser.add_argument('-t', '--text', help="Text to summarize",
                        type=str)
    parser.add_argument('-f', '--file', help="Filename to read text from",
                        type=str, default="text.txt")
    parser.add_argument('-r', '--ratio',
                        help="Given the ratio of the summarized text "
                             "(default: 0.2)",
                        type=float, default=1)
    parser.add_argument('-o', '--output',
                        help="Given the path to an output file. "
                             "Otherwise output.txt will be used",
                        type=str, default="output.txt")
    args = parser.parse_args()




    if args.file:
        with open(args.file, 'r') as infile:
            text = infile.readlines()
            text = "\n".join(text)
    if args.text:
        text = args.text

    summary = text_summarize(text, ratio=args.ratio)
    if args.output:
        with open(args.output, 'w') as outfile:
            outfile.write(summary)
            outfile.write("\n")
    else:
        print(summary)
