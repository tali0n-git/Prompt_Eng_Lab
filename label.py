from openai import OpenAI


def get_sentiment(text: list, index = 0) -> list:
    """
    Input:
        text: A list of strings, each representing a line of text to be categorized.
    Output:
        A list of strings, each representing the sentiment category for the corresponding line of text.
    """

    error = "Wrong input. text must be an array of strings."

    # Set up early return for empty or incorrect type of input
    if text == [] or type(text) != list:
        print(error)
        return(error)
    
    # Check if the input is a list of strings
    for t in text:
        if type(t) != str:
            print(error)
            return(error)
            

    client = OpenAI()

    ### Give an example of the task to the model

    system_prompt = """
    You are a helpful assistant that categorizes text into sentiment categories.
    The categories are positive, neutral, negative, or irrelevant.
    Be careful when trying to identify irrelevant text, as it may be difficult to identify.
    You should use Regex to identify the sentiment of each line of text.
    Ignore html tags, links, and any other non-textual elements.
    Use "irrelevant" for any text that does not fit into the other categories.
    Be consistent with your categorization, do not change your mind when categorizing the same text again.
    """

    prompt = f"""
    For each line of text in the string below, please categorize the review
    as either positive, neutral, negative, or irrelevant.

    Use only a one-word response per line. Do not include any numbers.
    {text}
    """
    soln_list = []
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    soln = response.choices[index].message.content.strip()

    for s in soln.split("\n"):
        if s.strip() != "" and s.strip() != None:
            soln_list.append(str(s.strip()))

    return(soln_list)
