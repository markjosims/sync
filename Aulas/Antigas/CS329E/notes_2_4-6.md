# Three types of machine learning
- Supervised learning - labeled data
- Unsupervised learning - unlabled data
- Reinforcement learning - unlabeled input, model creates categories, user gives feedback, model tries again
	- e.g. teaching computer to play chess

# Decision Trees
- nominal, continous & ordinal attribute splits
algorithm:
	1. if all records belogn to same class or have same attr values, leaf node
	2. else, choose an attribute to partition & split on
- choose attributes depending on impurity of child nodes
	- entropy
	- gini
- nominal attribute splits
	- if just two, split on those twoCl
	- if more, split into two groups
		- Marital Status {single, married, divorced} -> {single} vs {married, divorced}, {single, divorced} vs {married} etc.
	- **or** split into more than two groups
		- computationally easier to do binary splits, but doesn't necessarily change the quality of the tree
- continuous attribute splits
	- split at point where predicted label changes

| Class  | no | no | no | yes | yes | yes | no  | no  | no  | no  |
|--------|----|----|----|-----|-----|-----|-----|-----|-----|-----|
| Income | 60 | 70 | 75 | 85  | 90  | 95  | 100 | 120 | 125 | 220 |  


	- split at 80 or at 97.5  
- ordinal attribute splits
	- treat similarly to continuous

- multi-way splits can make data purity easier to achieve, but can overfit very quickly
	- measure on **gain-ratio** (Gain / SplitInfo)
	- entropy of attribute itself

## Characteristics of Decisions Tree
- easy to interpret
- computationally inexpensive
- robust to noise, easy to optimize to avoid overfitting
- irrelevant or redundant attributes do not have meaningful impact on accuracy
	- may result in larger-than-necessary tree, though