## Question 1

What is the most common sentiment observed in your sample of 50 reviews according to your OpenAI labeled data?

ANS: The most common sentiment observed was 'negative'.

## Question 2

How reliable do you believe these labels are? Look at the respective labels OpenAI has generated for specific reviews, does it seem like the large language model accurately described the user's review? What risk do model hallucinations introduce into this analysis?

ANS: The LLM does not always accurately describe user reviews, as we can see with the 4th and 5th reviews (on lines 10 and 11 in the JSON file); the LLM continues to incorrectly label them as 'positive' and 'negative', respectively, when they are supposed to be 'negative' and 'positive'. It appears to have trouble interpreting reviews that are longer than two or three sentances. I believe that the lables are mostly correct, though with some hallucinated responses that cause it to return more labels than necessary. My solution to this issue was to re-run the LLM with the same data until the correct number of labels are returned (this may take up to 5 minutes, just a heads up).

## Question 3

Using the most common sentiment, what would you recommend to this Coconut Water producer to improve customer satisfaction? Should they continue to pursue current market/product outcomes, or does there exist an opportunity for this business to improve its product?

ANS: One recommendation I would make to this producer would be to pinpoint the most common complaint about their product, potentially utilizing the same LLM. If it's that the supply is too little or too much, they should consider offering a wider array of pack options. If it's the taste that's the issue, they should consider reformulating their product. Given that about 60-75% of the reviews are negative, they should not continue to pursue current market outcomes.