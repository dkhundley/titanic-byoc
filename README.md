![](docs/images/github-banner.png)

Hello there friends! In this project, we are going to go through the process start to finish of creating a model using the Titanic dataset and then later deploying it to multiple platforms. This effort is also being covered in multiple #livecoding sessions on YouTube that can be collectively found as part of [this YouTube playlist](https://youtube.com/playlist?list=PLNBQNFhVrlVSAi9jIm6K5dWhcD1L372_G).



## Project Scope
This project is intended to teach others how to deploy a machine learning model across multiple different platforms in multiple different contexts using a "bring your own container" (BYOC) with the Titanic dataset. The Titanic dataset is a very popular dataset supported on the Kaggle platform ([link](https://www.kaggle.com/c/titanic)) often used by students to practice their machine learning / data science skills specifically for supervised, binary classification algorithms.

While a rather grim topic, the Titanic dataset is a popular choice amongst students because it is relatively easy to understand the data. This dataset covers [the tragedy of the Titanic](https://en.wikipedia.org/wiki/Titanic) sinking to the bottom of the ocean in 1912. You might wondering, "Isn't this the same tragedy that was covered in the popular 1997 film starring Kate Winslet and Leo DiCaps?" Why yes, my friend, tis indeed the same tragedy.



<p align="center">
<img src="https://media.giphy.com/media/XOY5y7YXjTD7q/giphy.gif">
</p>



The Titanic dataset contains individual records about every individual who was aboard the Titanic along with attributes known about each individual. (See the section below on data to learn more.) As touched on above, the dataset contains a binary "Survived / Did Not Survive" column, which students use as the predictor value for creating binary classification models.

The general sequence for this project will shake out as the following:

- Performing **feature engineering** on the raw dataset to generate proper features to feed into our predictive model
- Creating a **binary classification** model on top of the "clean", feature engineered dataset
- Creating a **serialized pipeline** that transforms raw Titanic inputs into an inferential expectation for whether or not the person survived
- Creating a **FastAPI-based implementation** for getting real time model results from an API
- Packaging the FastAPI implementation along with the model itself in a **standalone Docker container**
- Deploying the model to **Kubernetes** as a real-time endpoint
- Deploying the model to AWS as a **SageMaker real-time endpoint**

And I haven't committed to the following yet, but I think it'd also be cool to maybe eventually do the following. Let me know if anybody has interest in exploring any of these topics as part of a future livestream:

- Training the model directly in AWS SageMaker using a **SageMaker training job**
- Deploying the model to **Google Cloud Platform** as a real-time endpoint
- Deploying the model to **Kubernetes** as a scheduled batch cronjob
- Deploying the model to AWS as a **scheduled SageMaker batch inference job**