# Teachable Machine
This is the link of the model 
https://teachablemachine.withgoogle.com/models/GDJydNr8X/

### Training the Model with Teachable Machine
First, I visited the Teachable Machine website.
I selected Image Project.

### Set up the classes:
I created two classes:
The first class: Robots.
The second class: Humans.
I collected images of robots.
I collected images of humans.

### Upload the images:
I uploaded the images for each class through the Teachable Machine interface.

### Train the model:
After uploading the images, I clicked Train Model to start training the model.

### Export the model:
After the training was complete, I selected Export Model.
I chose TensorFlow as the export format.
I downloaded the model ZIP file.
I wrote a Python script to load the model and make predictions on an input image.

### Run the Python script
To test the model, I ran the Python script on an image (test1.jpg) that I wanted to classify, and it gave me the predicted class along with the confidence score.

### summary 
In this task, I created a model to distinguish between Robots and Humans. I used Teachable Machine for training, exported the model in TensorFlow format, and then created a Python script to load the model and predict whether a given image is of a robot or a human.
