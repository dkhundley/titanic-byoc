![](docs/images/github-banner.png)

Hello there friends! In this project, we are going to go through the process start to finish of creating a model using the Titanic dataset and then later deploying it to multiple platforms. This effort is also being covered in multiple #livecoding sessions on YouTube that can be collectively found as part of [this YouTube playlist](https://youtube.com/playlist?list=PLNBQNFhVrlVSAi9jIm6K5dWhcD1L372_G).



# Project Scope
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
- Deploying the model to **Google Cloud Platform** as a real-time endpoint

And I haven't committed to the following yet, but I think it'd also be cool to maybe eventually do the following. Let me know if anybody has interest in exploring any of these topics as part of a future livestream:

- Training the model directly in AWS SageMaker using a **SageMaker training job**
- Deploying the model to **Kubernetes** as a scheduled batch cronjob
- Deploying the model to AWS as a **scheduled SageMaker batch inference job**
- Deploying the model to **Google Cloud Platform** as a scheduled batch cronjob



# Directory Structure
The following is how this particular GitHub's directory's contents are organized:
- **container/**: Contains all the relevant files that will be injected into our BYOC container for training and inference
- **data/**: Contains the supporting data for this project, both in raw and cleaned formats
- **dependencies/**: Contains any files that help support the software solution, including installation dependencies
- **docs/**: Contains random files helping to support this project, including things like images and diagrams
- **k8s/**: Contains the YAML files used to deploy our Titanic model to Kubernetes (often abbreviated to "K8s")
- **models/**: Contains the serialized model files created as part of our model training pipeline
- **notebooks/**: Contains the Jupyter notebooks used to support each step of this project
- **terraform/**: Contains all the Terraform files used to deploy the Titanic model out to various platforms, including AWS and GCP
- **tests/**: Contains files supporting proper testing of our software solutions


# Data Dictionary

As mentioned above, this dataset was [sourced from Kaggle](https://www.kaggle.com/c/titanic/data). For your convenience, I have placed the raw datasets (`train.csv` and `test.csv`) in the `data/raw/` directory of this repository. Additionally, I have also shared the same data dictionary here as part of this repo, and I also note in the table below whether or not the feature is included as part of the end model.

| **Feature Name** | **Description** | **Key** | **Included in Model?** |
| ---------------- | --------------- | ------- | ---------------------- |
| `survival` | Binary indicator denoting the person's survival | 0 = No, 1 = Yes | ✅ |
| `pclass` | Ticket class, also a proxy for socio-economic status (SES) | 1 = 1st, 2 = 2nd, 3 = 3rd | ✅ |
| `sex` | Gender of the person (only male or female recorded) | | ✅ |
| `sibsp` | Number of siblings / spouses aboard the Titanic* | | ✅ |
| `parch` | Number of parents / children aboard the Titanic | | ✅ |
| `ticket` | Ticket number | | ❌ |
| `fare` | Passenger fare in dollars | | ✅ |
| `cabin` | Passenger's cabin number | | ❌ |
| `embarked` | Passenger's port of embarkation | C = Cherbourge, Q = Queenstown, S = Southampton | ✅ |

**Funnily enough, Kaggle's official Titanic site notes "mistresses were ignored" for spouse count* 😂