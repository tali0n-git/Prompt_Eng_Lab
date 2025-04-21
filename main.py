from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str)-> list:
    """
    Description:
        This function takes a file path to a json file containing reviews,
        extracts the reviews, and categorizes each review into one of the following sentiment categories: 
        positive, neutral, negative, or irrelevant.
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
    sentiments_list = get_sentiment(reviews)
    if sentiments_list == None:
        print("Error: get_sentiment returned None.")
        return None


    # plot a visualization expressing sentiment ratio
    make_plot(sentiments_list)

    return sentiments_list



if __name__ == "__main__":
    sentiments = run("data/raw/reviews.json")
    print(sentiments)