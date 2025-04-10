import matplotlib.pyplot as plt


def make_plot(sentiments: list, index: int) -> list:        # Shouldn't the return type be None?
    """
    Input:
        sentiments: A list of strings, each representing a sentiment category.
    Output:
        None, but saves a plot of the sentiment categories to a file in the form of a pie chart.
    """
    # Set up early return for empty input
    if sentiments == [] or sentiments == None:
        print("Wrong input. sentiments must be an array of strings.")
        return sentiment

    # Count the occurrences of each sentiment category
    sentiment_counts = {}
    for sentiment in sentiments:
        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1
        else:
            sentiment_counts[sentiment] = 1

    # Create a pie chart
    labels = list(sentiment_counts.keys())
    sizes = list(sentiment_counts.values())
    colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the plot to a file
    plt.savefig(f"images/sentiments{index}.png")

    return None
