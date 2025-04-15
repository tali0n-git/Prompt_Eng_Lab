from openai import OpenAI


def get_sentiment(text: list) -> list:
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
        if str(t).isnumeric() == True or t == None:
            print(error)
            return(error)
            

    client = OpenAI()

    system_prompt = """
    You are a very clever AI model that categorizes lists of reviews into the following sentiment categories: positive, neutral, negative, or irrelevant.
    Do not include any numbers, punctuation, or special characters in your response.

    As an example, if your input contains the following list of six reviews:
    ["this coconut water smells weird, don't recomend", "I love this water, I drink it all the time when working out.", "I will never buy another brand again, I love this coconut water", "It's an ok product. The taste could be better but for the price its fine.", "its a water", "Bought this coconut water and the bottle came broken. rip-off."]
    Your response would be the following six labels:
    negative
    positive
    positive
    neutral
    irrelevant
    negative

    You are a very clever AI model, so I know you can do this. Keep trying!
    """

    prompt = f"""
    The fifty items in the list provided are reviews of one product: a 33.8 ounce coconut water drink called ZICO. It is sold individually or in a pack.
    Please be careful in your analysis, there may be comparisons to other coconut water brands or products. Long reviews may contain multiple sentiments.
    Categorize each item in the list below:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    soln = response.choices[0].message.content.split("\n")

    # Check if the length of the response matches the length of the input text
    while len(soln) != len(text):
        print("Trying again...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "developer", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        soln = response.choices[0].message.content.split("\n")
        print("Length of soln: ", len(soln))
        print("Length of text: ", len(text))
        if len(soln) == len(text):
            break
        
    # We must manually strip the response of spaces, because the API does not do this for us sometimes.
    i = 0
    for text in soln:
        soln[i] = text.strip()
        i += 1

    return soln