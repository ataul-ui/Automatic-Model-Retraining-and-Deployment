# predictive-maintainance-for-a-smart-factory
This repository contains the code for a predictive maintaincence project. A detailed blog on this project is coming soon. Actually i think I'll get rid of mlflow in this, I'll create another project and use it there, in this one, hyperopt is good enough. For that new project I think I could use tensorflow, maybe. Or I could deploy it on azure cloud (use azure autoML). All of this needs to come together for me preparing for the databricks certification somehow


## Requirements
Make sure you have conda installed. If you want to deploy this app on the web make sure you have a Heroku or Render account.





## Streamlit web app

To access the web deployed version, please create a pull request on production branch to put your username and date access in records.txt file; once the pull request has completed go to this link to access the site:
```
https://smart-factory-form.onrender.com
```

## Streamlit local app
- To start the  app on your local machine, clone this repository then run these commands in your terminal:
```bash
conda activate your_environment_name
conda install --file requirements.txt
streamlit run app.py
```

