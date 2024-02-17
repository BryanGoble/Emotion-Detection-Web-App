# Emotion-Detection-Web-App
AI-based web application using Watson NLP library for IBM Course Final Project

## Introduction

For this project, I assumed the role of a software engineer who needs to develop an embeddable Watson AI-based web application for emotion detection.

> Emotion detection extends the concept of sentiment analysis by extracting the finer emotions, like joy, sadness, anger, and so on, from statements rather than the simple polarity that sentiment analysis provides. This makes emotion detection a very important branch of study and businesses use such systems widely for their AI based recommendation systems, automated chat bots, and so on.

I met the following tasks:
1. Clone the project repository
2. Create an emotion detection applicaiton using Watson NLP library
3. Format the output of the application
4. Package the application
5. Develop/Run unit tests on the application
6. Web deployment of the application using Flask
7. Incorporate error handling
8. Run static code analysis

### Task 1

The base GitHub repo was cloned using a Cloud-based IDE

![](images\1_folder_structure.png)

### Task 2

The Watson NLP libraries are embedded, so I don't have a need to import them. I built a function to send a post request to the correct function in the library and receive the output.

![](images\2a_emotion_detection.png)

Testing the application after importing my code

![](images\2b_application_creation.png)

### Task 3

Here, I formatted the output by converting the response text into a dictionary using the `json` library funcitons.

The required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores were all extracted.

![](images\3a_output_formatting.png)

Tested the application again in the `python3.11` shell

![](images\3b_formatted_output_test.png)

### Task 4

This step, I packaged the application naming it [EmotionDetection](EmotionDetection).

![](images\4a_packaging.png)

I then validated that I had created the package successfully by importing my function from the package

![](images\4b_packaging_test.png)

### Task 5

Next, I wrote unit tests in [test_emotion_detection.py](test_emotion_detection.py) that called the required application function from the package and tested it for the following statements and dominant emotions.

| Statement | Dominant Emotion |
| :--       | :--              |
| I am glad this happened | joy |
| I am really mad about this | anger |
| I feel disgusted just hearing about this | disgust |
| I am so sad about this | sadness |
| I am really afraid that this will happen | fear |

<br>

![](images\5a_unit_testing.png)

Verified the unit tests actually passed successfully

![](images\5b_unit_testing_result.png)

### Task 6

I wrote a script, `server.py` to handle the deployment of the web application using Flask

> `index.html` in the `templates` folder and `mywebscript.js` in the `static` folder were already provided as part of the original repo. I did not need to update them. 

![](images\6a_server.png)

I then tested the Web Application to ensure the data was displaying properly

![](images\6b_deployment_test.png)

### Task 7

Now, I incorporated error handling capability in my `emotion_detector` function to manage blank entries from users, i.e. running the application without any input.

I added checks based on the `status_code` attribute ofthe server response to correctly display the system response for blank entries.

![](images\7a_error_handling_function.png)

After modifying my function, I incorporated error handling into `server.py` when the `dominant_emotion` is `None`.

![](images\7b_error_handling_server.png)

Here, I tested the output displayed correctly for an invalid entry.

![](images\7c_error_handling_interface.png)

### Task 8

Lastly, I conducted static code analysis to ensure my code was in compliance with current PEP8 standards.

The first time around, I received a 7.14/10. I added several DocString comments and modified the `text_response` in `server.py` to now contain several f-strings rather than one meeting the max 100 character recommended limit of each.

![](images\8a_server_modified.png)

Once all changes were implemented, I received a 10/10.

![](images\8b_static_code_analysis.png)

## Conclusion

By completing this project, I had:

1. Created an Emotion Detection application using the functions from an embeddable AI library
2. Extracted relevant information from the output received from the function
3. Tested and packaged the application created using the Emotion Detection function
4. Completed web deployment of the application using Flask
5. Incorporated error handling in the application to account for invalid input
6. Written code that is in perfect compliance with PEP8 guidelines, getting a 10/10 score in static code analysis