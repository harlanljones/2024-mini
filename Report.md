# EC463 2024 Miniproject
Howell Xia and Harlan Jones

## Exercise 1: Light
The values we found for max_bright and min_bright approximately were 5500 and 42000, respectively.
[Video Demo](https://drive.google.com/file/d/1G7RjNuhqV7o-_nTj3MPTvbsbykFE_Rgq/view?usp=sharing)

## Exercise 2: Sound
[Video Demo](https://drive.google.com/file/d/1FgJfpBBsMMWhfO6oQWHQScWkZDpRiDvb/view?usp=sharing)

## Exercise 3: Game

### Game data
Average response time: 281.125ms <br>
Minimum response time: 171ms <br>
Maximum response time: 468ms <br>

### Cloud portion
Our data is uploaded via an HTTP request from the Pico in our `exercise_game.py` script to a Firebase project. The HTTP request url is [here](https://firestore.googleapis.com/v1/projects/senior-design-mini-2/databases/(default)/documents/scores) and the project link is [here](https://console.firebase.google.com/project/1015684280757). The project is private but we've shared it with all the BU emails of the professors and GSTs. Below are screenshots of the cloud storage and the video demo.

[Video Demo](https://drive.google.com/file/d/151eSsiIQzSx8i5jm2InsPHCyGzA6QoPb/view?usp=sharing)

<p align="center">
<img src="./images/firebase_ss.png" width="50%">
</p>
<p align="center">
Firebase Database
</p>

<p align="center">
<img src="./images/http_ss.png" width="50%">
</p>
<p align="center">
HTTP URL
</p>
