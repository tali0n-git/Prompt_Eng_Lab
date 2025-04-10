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

    print("Length of reviews:", len(reviews))

    # get a list of sentiments for each line using get_sentiment
    sentiments_text_0 = get_sentiment(reviews, 0)
    #sentiments_text_1 = get_sentiment(reviews, 1)
    #sentiments_text_2 = get_sentiment(reviews, 2)

    #print(sentiments_text_0)

    # plot a visualization expressing sentiment ratio
    #make_plot(sentiments_text_0, 0)
    make_plot(sentiments_text_0, 1)   #checking if the plot is consistent; RESULT: It did NOT do the thing, made a graph closer to one of the first generated results...
    #make_plot(sentiments_text_1, 1)
    #make_plot(sentiments_text_2, 2)
    print("I DID THE THING!")

    # return sentiments
    return(sentiments_text_0)



if __name__ == "__main__":
    #print(run("data/raw/reviews.json"))
    run("data/raw/reviews.json")
