# Image Classification with CNN

This was a project during the course "AI Engineering". We Built a Convolutional Neural Network (CNN) model to classify images from a given dataset into predefined categories/classes.

[Task Descriptions and Project Instructions](https://github.com/ironhack-labs/project-1-deep-learning-image-classification-with-cnn)


## Project Results
In this project, we classified images from the animals 10 data set.

<img width="1016" alt="Screenshot 2025-03-07 at 16 12 26" src="https://github.com/user-attachments/assets/56448240-a605-4b58-ad04-51b1e8e77a20" />

- Built a sequential CNN model
- Optimized the model
- Prediction accuracy of on holdout data set: 91.02%
- transfer learning from VGG16
- Deployed on Gradio where user could upload image to predict animal class (link expired after 72 hours)

[Project presenatation](
https://docs.google.com/presentation/d/11OfQFu_mEn0karKFN0GwSh32nj1BKaMf4u_9GwSmyRY/edit#slide=id.p)


## Repository Folders and Files

Here is a short description of the folder and files available on the repository.


### Documents
- holdout_subset.zip. You can use these images to predict with the model

### Notebooks  
- [Split_Validation_Data](Split_Validation_Data): split the data set to one set for training and testing (90%) and a second one to make predictions (10%)
- [Model1](Notebooks/Model1.ipynb) : The starting point model
- [Model2(optimized)](Notebooks/Model2(optimized).ipynb) : The optimized model
- [Transfer_learning(winner_model)](Notebooks/Transfer_learning(winner_model).ipynb) : Using VGG16 to predict the data set
- [Deploy_gradio](Deploy_gradio.ipynb) : Notebook to deploy the model to a website by using gradi


## Installation
Use **requirements.txt** to install the required packages to run the notebooks.
