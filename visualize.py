import matplotlib.pyplot as plt


def make_plot(sentiments: list, index = "") -> None:
    """
    Description:
        This function takes a list of sentiment categories 
        and creates a pie chart to visualize the distribution of these categories.
        The pie chart is saved to a file in the form of a PNG image.
        The function also includes an early return for empty or invalid input.
    Input:
        sentiments: A list of strings, each representing a sentiment category.
    Output:
        None, but saves a plot of the sentiment categories to a file in the form of a pie chart.
    """
    # Set up early return for empty input
    if sentiments in [[], [""], None]:
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
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Save the plot to a file
    plt.savefig(f"images/sentiments{index}.png")

    return None