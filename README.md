# Sign language translator

this project will help normal people to understand deaf people
by taking a video file or video from webcam and translate the hand's sign in it.

## Getting Started

These instructions will get you a copy of the project up and running on your computer for development and testing purposes.

### Prerequisites

1) you need to have an account in azure custom vision for hand's sign classification. if you don't have, click this link to start creating one.
```
https://azure.microsoft.com/en-us/services/cognitive-services/custom-vision-service/
```

2) Python version 3 or later.
```
https://www.python.org/
```

3) OpenCV package for python
write this command line in 'cmd' to install it after you install python.
```
$pip install opencv-python
```

### Fill the requirement

once you clone this project to your computer, please check these lines of code and complete what is asking you before running the program.

```
line 15: 'Prediction-Key': '<enter your predection kay>',
line 17: 'Ocp-Apim-Subscription-id': '<enter your Subscription id>'
line 22: 'application': '<enter your service name>'
line 25: file_path = "<put your video file_path>"
line 45: conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com') # use your endpoint here as this example
line 46: conn.request("POST", "https://eastus.api.cognitive.microsoft.com/customvision/v3.0/Prediction/<enter your project id>/classify/iterations/<enter your iteratin name>/image?%s"
```

## Running the tests

when you run the code with video file or webcam you git output like this

```
b'{"id":"**********","project":"**********","iteration":"**********","created":"****-**-*****:**:**.****","predictions":[{"probability":0.791616261,"tagId":"30768361-7f2d-4911-9ac0-961f68c628fd","tagName":"No hand sign"},...
```

once you done, go and translate a sign language to enrich your service by tagging what you catch.


## Built With

* [Anaconda](https://www.anaconda.com/distribution/) - The World's Most Popular Python/R Data Science Platform
* [Atom](https://atom.io/) - A hackable text editor built by GitHub
* [OpenCV](https://opencv.org/) - Open Source Computer Vision Library

## Contributing

Please read [CONTRIBUTING.md](https://github.com/self-speech/Amirican-sign-language-translator-ASL/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Raghad Al-Jabr** - *Initial work* - [self-speech](https://github.com/self-speech)

## Acknowledgments

* Advanced Electronics Company
* Engineer.Abdulaziz AlSadhan
* Engineer.Mohammad AlJabr
* Dev.Hessa AlZamel
