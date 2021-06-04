## iMaskerYA 

In response to the impact of the Covid-19 epidemic, the mask detection system uses a camera to detect whether people on the screen are wearing masks. The system uses YOLOv4 and combines with Quasar to set up a page to achieve the project goal of "real-time detection, warning, and statistics".

### Install Steps
1. Clone this repo and install quasar dependencies
```
git clone https://github.com/Pianochicken/iMaskerYA.git
cd iMaskerYA
yarn
```
2. Clone the repo from [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet) under iMaskerYA folder 
```
git clone https://github.com/AlexeyAB/darknet.git
```

3. Install darknet dependencies [Requirements](https://github.com/AlexeyAB/darknet#requirements).
    * Notice that openCV have to below 4.4.0

4. Follow the tutorial from [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet#how-to-compile-on-windows-using-cmake) to compile darknet depends on your OS

5. Dulplicate the <b>darknet</b> folder in iMaskerYA_File to the responding folder in darknet from the previous step

p.s Install [Python](https://www.python.org/downloads/) if you don't have it.

### Implement

Click the <b>run_main.py</b> in iMaskerYA folder to enjoy the mask-detecting system! 

<br/>

![Mask_detecting](https://github.com/Pianochicken/iMaskerYA/blob/main/public/iMaskerYA_demo.png)

[Demo Link](https://www.youtube.com/watch?v=GY70J7ilkrk)
