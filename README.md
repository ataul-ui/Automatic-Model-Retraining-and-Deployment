# predictive-maintainance-for-a-smart-factory
This repository contains the code for a predictive maintaincence project. A detailed blog of this project is available [here](https://medium.com/@ataul.akbar/how-to-build-a-predictive-maintainance-system-for-a-smart-factory-mlops-2b251434d7c3).



## Activity diagram
![Alt text](./images/2nd-fixed-image.png)

** 
On uml diagram instead of field technician it should be iot device. 

And instead of "technician opens app" it should be "device establishes connection with app" 

Rest can be the same I believe, except if there is a fail condition it should send a notification message to field technician. 

And the whole process repeats until connection is lost. 
**

## Requirements
Make sure you have conda installed. If you want to deploy this app on the web make sure you have a Heroku or Render account.



## Streamlit web app

To access the web deployed version, please follow this link (you will need to wait about a minute for render to build the website) (in the future I plan to replace render with azure webapp service):
```
https://smart-factory-form.onrender.com
```

## Streamlit local app
To start the  app on your local machine, clone this repository then run these commands in your terminal:
```bash
conda activate your_environment_name
conda install --file requirements.txt
streamlit run app.py
```

