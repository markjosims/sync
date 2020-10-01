# Evaluating Classifiers
- accuracy is most basic measure
- need to retrain model w/ novel (and/or more) data


## Broken Feedback Loop
- defaulting on loans is an example
    - if a record is classified as "unloanable," it will likely be stuck in that category no matter what
    - (can't calculate probability of defaulting if no one takes a loan)
- better example: classifying email as spam
    - users can move email from spam into inbox or vice versa
    - gmail will update its data based on user input

## Class Imbalance Problem
- ex. far more legitimate credit card transactions than illegitimate
    - classifier could label all records as legitimate and get high accuracy
    - **don't** use accuracy to measure, use a confusion matrix

|              | Predicted Class | +       | -       |
|--------------|-----------------|---------|---------|
| Actual Class | +               | F++(TP) | F+-(FN) |
|              | -               | F-+(FP) | F--(TN) |

- sensitivty - what % of actual positives are predicted
- specificity - what % of actual negatives are predicted
- `+` is rare, `-` is common

### Ways to Mitigate Class Imbalance
- undersampling- remove some of majority class records
- oversampling - duplicate some minority class records