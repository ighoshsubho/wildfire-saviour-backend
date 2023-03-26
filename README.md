
# ✨ Wildfire Saviour ✨

### Wildfires can be a significant threat to both human life and property.

It can not only cause a loss of life but also property damage and Economic impact.

Not only that, wildfires can cause enviornmental imact where they can cause destruction of natural habitats.

And to tackle this problem, we present you - Wildfire Savior!

### Wildfire Saviour 🚀

This website keeps track of all the ongoing wildfires from the NASA API, and keeps you in track of your surrounding.

Not only that if anyone enters thir latitude and longitude, the website will show the current ongoing wildfires.

This happens almost in realtime.

Repo link - https://github.com/anirban-25/wildfire-saviour

### Exclusive Feature 💥

This is the feature repo of Wildfire Saviour.

The OpenCV part is in the other repo.

Here we implemented OpenCV to predict the wildfire and then send an email as well as ringing an alarm for 11s.

### Validation

And one can validate whether the fire detection is fake or not by referring to our website which will fetch the data from NASA API in almost realtime.

## Tech Stack

**Frontend:** Next 12, Tailwind

**Authentication:** Firebase

**Object Detection:** OpenCV

**Others:** Python, AWS, NASA API

## Run Locally

### First get your AWS Secret key and specify in send_email.py file using .env. And don't forgert to specify sender email as well!

Clone the project

```bash
  git clone [Link to project]
```

Go to the project directory

```bash
  cd wildfire-saviour-backend
```

Install dependencies

```bash
  pip install -r requirements.txt
```
Run it locally

```bash
  python fire_detection.py
```

