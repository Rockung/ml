## A Brief Introduction to Machine Learning for Engineers

### Abstract

key concepts
algorithms
theoretical frameworks

supervised learning
unsupervised learning
statistical learning

probabilistic grahpical models
approximate inference

discriminative and generative models
directed and undirected models

frequentist and Bayesian approaches
exact and approximate inference

convex and non-convex optimization

### Notation

### Introduction

pattern recognition

- automatic discovery of regularities in data for 
	- decision-making
  - prediction
	- data mining
- by identifying models that explain relevant aspects of the data
- by directly learning signal processing algorithms, such as filters, with desirable properties
	
machine learning

> development of efficient pattern recognition methods that
are able to scale well with the size of the problem domain
and of the data sets.

> at a high level, letting large amounts of data dictate algorithms
and solutions for complex inferential problems

> be contrasted with the time-honored approach of relying on domain
experts for the development of tailored solutions

> collect large data sets, e.g., of labelled speech, images or videos,
and to use this information to train general-purpose learning machines
to carry out the desired task

three different types of machine learning problems

- supervised learning
> identify a predictive distribution p(t|x) for the value of the label
the output may be in the form of deterministic predictive function t=t(x)
  - classification
	- regression

- unsupervised learning
> less well defined. refers to the task of learning properties of the
mechanism that generates the data of interest.
  - clustering
	- dimensionality reduction
	- feature extraction
	- representation learning

- reinforcement learning
> refers to the problem of inferring optimal actions based on rewards or
punishments received as a result of previous actions


MDL: minimum description length
GLM: generalized linear model

training loss
generalization
overfitting

interpretation
causality
information-theoretic metrics

### Linear Regression

- supervised learning
> the goal is to identify a predictive algorithm that minimizes the
generalization loss, that is, the error in the prediction of a new label
t for an unobserved explanatory variable x

  - free variables(x): covariates, domain points, explanatory variables
	- dependent variables(t): labels, responses

no free lunch theorem
> one cannot learn rules that generalize to unseen examples without making
assumptions about the mechanism generating the data

inductive bias
> the set of all assumptions made by the learning algorithm

To think is to forget details, generalize, make abstractions.
== quote by Jorge Luis Borges

  - memorizing: retrieval of a value of t corresponding to an already observed pair(x, t) in D
	- learning: capability to predict the value t for an unseen domain point x
	  converts experience(in the form of D) into expertise or knowledge(in the form of a predictive algorithm)

optimal prediction
decision rule
posterior distribution
joint distribution
conditional mean
independent identically distributed

loss function
quadratic loss
0-1 loss: detection error
generalization risk/losss

ERM: empirical risk minimization
ML: maximum likelihood
MAP: maximum a posteriori
