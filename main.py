from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str)-> list:
    """
    Input:
        filepath: The path to the json file containing reviews.
    Output:
        A list of sentiments for each review in the json file.
    """
    # open the json object
    with open(filepath, 'r') as file:
        data = json.load(file)["results"]


    # extract the reviews from the json file
    # and remove any empty lines or irrelevant text
    reviews = []
    for review in data:
        if review not in ["", None, " ", "\n"]:
            reviews.append(review)


    # get a list of sentiments for each line using get_sentiment
    sentiments_text = get_sentiment(reviews)
    if sentiments_text == None:
        print("Error: get_sentiment returned None.")
        return None
    sentiments_list = []
    for line in sentiments_text:
        sentiments_list.append(str(line.strip()))


    print("Length of sentiments_list: *", len(sentiments_list), "*")


    # plot a visualization expressing sentiment ratio
    make_plot(sentiments_list)

    return sentiments_list



if __name__ == "__main__":
    sentiments = run("data/raw/reviews.json")
    print(sentiments)
'''
    # To check the first 7 lines of the sentiment list:
    # 11th line should be POSITIVE!
    i = 7
    for sentiment in sentiments[:7]:
        print(f"For line {i}: ", sentiment)
        i += 1
'''