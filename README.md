# Restaurant-Recommendation-System
Restaurant Recommendation System is a system used to recommend restaurant based on user's requirement like his/her location and Cuisine of his/her choice. It is filtering/Content based recommendation system. We have used the zomato data of banglore restaurants. This System requires User’s location within the Banglore city and the cuisine that user want to have and based on that recommend best restaurant to the user on the basis of the sentiment extracted from the previous reviews of the other users. I have used MmongoDB database that comes under NoSQL Databases to store the data of my restaurant to fetch  the restauraant faster as per the user requirement.

For This Project, You need to install few libraries of python 

- Flask
- Pandas
- Nltk

```python 
 pip3 install flask 

 pip3 install pandas

 pip3 install nltk
```
To install MongoDB Database in Ubuntu 18.04, type comand on Terminal 
```cmd
  sudo apt update
  sudo apt install -y mongodb
```

Initial Dataset is 
```data
  /Restaurant-Recommendation-System/Restaurant Recommendation System/zomato.zip
```  
Final  Dataset to be imported on MongoDB is 
```data
   /Restaurant-Recommendation-System/Restaurant Recommendation System/final_Dataset.zip
```
first extract this data then import oon mongoDB dataabase  using command  on terminal : 
```mongoDB
 mongoimport -d restaurants -c data --type=json /Restaurant-Recommendation-System/Restaurant Recommendation System/final_Dataset.json
 
 Where restaurants is database name
 & data is the name of Collection
```

I have created a video and Project Report as well which helps you to understand how this project works and what is the flow oof this project Which you can find in directory 
```dir
 Restaurant-Recommendation-System/Restaurant Recommendation System/Additional/Project.mp4
 Restaurant-Recommendation-System/Restaurant Recommendation System/Additional/Project__Report.pdf
```

You can find my project on the link below
```Link
http://13.127.218.217:5000/
```

## Happy Coding 😊


