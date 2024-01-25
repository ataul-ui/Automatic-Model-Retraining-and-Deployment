# predictive-maintainance-for-a-smart-factory
This repository contains the code for a predictive maintaincence project. A detailed blog of this project is available [here](https://medium.com/@ataul.akbar/how-to-build-a-predictive-maintainance-system-for-a-smart-factory-mlops-2b251434d7c3).



## Activity diagram
![Alt text](./images/3rd-image.png)
After completing the postman api producer certificate I'll update this project to have used more of postman for api testing

I could comment out the ml stuff and instead put in a kafka broker that will eventually return the json requests, the timer for return requests in 5 seconds (aka kafka producer will ingest the messages and only release them from the kafka producer after 5 seconds), and the "ML part" will only be a simple python function that will always return failure.

Also I think I can simulate the app using .net meadow, this way I can learn more about meadow and .net

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

