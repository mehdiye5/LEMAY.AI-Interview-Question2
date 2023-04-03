# LEMAY.AI  Interview Question 2

## Instructions

Using following line to pull the docker image from the github image registry. 
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
