# LEMAY.AI  Interview Question 2

## GitHub Docker Registry Authentication Process

Authenticate with the GitHub Docker registry by logging in using the Docker CLI.
```shell
docker login docker.pkg.github.com -u USERNAME -p ACCESS_TOKEN
```
Replace USERNAME with your GitHub username and ACCESS_TOKEN with a personal access token that has the appropriate permissions to read from the GitHub Packages registry. You can generate a personal access token in the "Settings" section of your GitHub account.

### How to Generate Personal Access Token
To generate a personal access token for use with the GitHub Packages registry, you need to follow these steps:

1. Go to the "Settings" section of your GitHub account.
2. Click on "Developer settings" and then "Personal access tokens".
3. Click on "Generate new token".
4. Give the token a name and select the appropriate scopes for the token. For example, you may want to select the **read:packages** and **write:packages** scope to allow read and write access to packages in the GitHub Packages registry.
5. Click on "Generate token" and copy the token to your clipboard.
6. Store the token securely in a safe place. You will need it when logging in to the GitHub Packages registry.


## Instructions

Once you have been authenticated with GiHub Docker Registry, use following line to pull the docker image from the github image registry. 
**Note:** The image is approximately 6gb in size.

```shell
docker pull docker.pkg.github.com/mehdiye5/lemay.ai-interview-question2/huggingface-inference:1.0
```

Once image is downloaded, run the following code to start the API.
**Note:** Make sure that port 8080 is not busy

```shell
docker run -p 8080:8080 -e PORT=8080 huggingface-inference
```

Now that API is running, download the notebook and execute the test scenario.

## Why did I choose CAMemBERT Base as the model to demonstrate my API?
CAMemBERT is a language model that is based on RoBERTa with 12 layers and 110 million parameters. It was pre-trained on large amounts of unlabeled text and fine-tuned on downstream tasks such as natural language understanding and sentiment analysis.I chose this model to see how my API handles a relatively smaller model that still achieves good performance on a variety of NLP tasks. The reason I chose the "fill-mask" task for the model to predict the most likely word for the blank space in a given sentence is that I wanted to see how my API performs with streaming for the response data that is too large to transmit in a single response. To demonstrate the support for multiple parallel incoming requests I used threading in the provided notebook.
