## Homework 10

In this homework, you are going to use and compare two different trackers (of your liking) and compare the results.

### Step 1
Decide what video you are going to use for this homework, select an object and generate the template. You can use any video you want (your own, from Youtube, etc.)
and track any object you want (e.g. a car, a pedestrian, etc.).

### Step 2
Initialize a tracker (e.g. KCF).

### Step 3
Run the tracker on the video and the selected object. Run the tracker for around 10-15 frames.

### Step 4
For each frame, print the bounding box on the image and save it.

### Step 5
Select a different tracker (e.g. CSRT) and repeat steps 2, 3 and 4.

### Step 6
Compare the results:
* Do you see any differences? If so, what are they?
* Does one tracker perform better than the other? In what way?

# Answers
* Yes, KCF bounding box was can't change his resolution box. TLD always trying search box and sometimes get wrong prediction of object position. CSRT have best bounding box, but not when car gone from view.
* KCF have good result but with good fps video, with less fps KCF can failure(but work faster than other). Seems like TLD have problem with tracking after car gone from view. As for me CSRT have best result but sometimes can not detect when car gone from view

# Video Link
* https://www.youtube.com/watch?v=NQGYIbspMzc