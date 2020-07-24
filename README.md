# telegram ChatBot boilerplate
A telegram chatbot boiler plate in Flask

# How to use It?
  ### 1. change app/config.py.
 
 - [create bot token](https://core.telegram.org/bots#6-botfather)
   
  ```
  TELEGRAM_BOT_TOKEN="YOUR TOKEN HERE"
  URL="YOUR TOKEN HERE"
  ```
  - add your Token here  and  URL will we replace by the URL where your app is deployed.
    ```
    for heroku: https://<YOU APP NAME>.herokuapp.com/
    ```
### 2. To cutomize Chatbot to give reponse according to you requirements.
      ```
      you need to change respond function in /app/api.py.

      here you can find reponse variable like : response = 'Here is your response'

      Just change it to whatever you want to reply or you can integrate you smart reply AI and repond with that result
      Whatever you want.
     ```
 ### 3. after customizing your app.
 
 you can deploy it and then trigger the setwebhook by going to <URl/setwebhook>.
 
 For heruko:
 - create your new app on heruko.
 - add url of the app in app/config.py file.
 - if you are not logged in to heruko first login using:
    ``` heruko login ```
 - initialize an empty git repository and add your app:
    ```
      git init
      heroku git:remote -a <app_name>
    ```
  - deploy the app:
    ```
      git add .
      git commit -m "push"
      git push heroku master
    ```
  - After successfull deployment got to:
  ``` https://<you_app_name>.herokuapp.com/setwebhook ```
  - if you see ``` web hook setup Success ``` Then you are good to go.
  - Now you can chat with your bot and bot will reply to you according to your customization.
  
  
    
    
  
  
