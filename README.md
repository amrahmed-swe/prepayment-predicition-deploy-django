<div id="top"></div>

![Python][python-shield]
![Django][django-shield]
![HTML5][html-shield]
![CSS3][css-shield]
![JavaScript][js-shield]
![Heroku][heroku-shield]
![NumPy][numpy-shield]
![Pandas][pandas-shield]
![scikit-learn][scikit-shield]
[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/amrahmed-swe/prepayment-predicition-deploy-django">
    <img src="static/image/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Prepayment-Prediction-Django</h3>

  <p align="center">
    An awesome project, and it is an open source.<br/>
    Predicting Mortgage Backed Securities Prepayment Risk Using Machine Learning.
    <img src="https://user-images.githubusercontent.com/78646864/136017729-8b90fe01-9fdc-4840-8887-b271c266e51c.png" alt="Freddie Mac">
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project :grinning:

[![Product Name Screen Shot][product-screenshot]](https://prepayment-prediction-b.herokuapp.com/)

### Definition :sparkles:
<p>Mortgage-backed securities, called MBS, are bonds secured by home and other real estate loans. They are created when a number of these loans, usually with similar characteristics, are pooled together. As the borrowers gradually pay off the underlying mortgage loans, the investors receive payments of interest and principal.</p> 

### Problem Statement :point_down:
</p>A large risk factor in MBS lies in the possibility of prepayments. Prepayments are payment by borrowers,who pay back a part, or the full amount of the loan earlier than discussed in their mortgage contract.<p>

<b>The Goal: :fire::fire:</b>
* The aim of our project is to develop various Machine Learning models that could predict the prepayment risk of mortgage loans<br/>

<b>By using machine learning techniques:</b>
* Random Forest :herb::fire:
* Logistic Regression :v:
* Support Vector Machine (SVM) :skull:

### Dataset :house_with_garden:

We use Freddie Mac’s home loans dataset. This dataset contains 291452 rows which represent the number of mortgages/ data points and 28 columns representing different features of the data.
you can check a description for each feature in [Blueprint](https://github.com/amrsss/prepayment-predicition-deploy-django/blob/main/Blueprint.pdf). Download :point_left:

Use the `README.md` as documentation to get started.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

List of major frameworks/libraries used to bootstrap project. Here are a examples.

* [Python](https://www.python.org/)
* [scikit-learn](https://reactjs.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://dashboard.heroku.com/)
* Others (Scroll down to installation)

### Model Used:
This is a Classification problem so we use Random Forest Classifier and Linear Support Vector Classifier for Model Building.
#### Training and Testing dataset
Split dataset into 80 % for Training and 20% for testing

##### We achieve 100% accuracy in both the models which indicates data leakage. This is due to sub duplicates in the dataset which cannot be solved unless we change the entire dataset.



<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started :rocket:
Follow these instructions on setting up project locally.
To get a local copy up and running follow these simple steps.

### Prerequisites :sparkles:


* [Download Python](https://www.python.org/downloads/)
* Verify **python3** is installed
  ```sh
   python3 --version
  ```
* Check PIP Installed
  ```sh
    pip --version
  ```

### Installation :collision:

_instruction for installing and setting up your app._

1. Clone the repo
   ```sh
   git clone https://github.com/amrsss/prepayment-predicition-deploy-django.git
   ```
2. Creating a virtual environment [option] 
   ```sh
   py -m venv env
   ```
3. Activate your virtual environment [if you create venv]
   ```sh
   nameyourenvironment\Scripts\Activate.ps1
   ```

4. install requirements
   ```sh
   pip install requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE -->
## Usage :star::boom:

### Screenshots

#### Home Page
<img src="Screenshots\home-form.png" alt="home-interface" >

#### Help Button
<img src="Screenshots\help.png" alt="Help" >

#### Result Page
<img src="Screenshots\result.png" alt="result" >

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact :hand::bell:

<!-- [@AmrSiri][tweeter-shield] -->
Socials:
   <!-- [![Tweeter][tweeter-shield]][tweeter-url] -->
<p align="left"> <a href="https://twitter.com/AmrSiri" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="amr ahmed(swe)" height="30" width="40" /></a> <a href="https://www.linkedin.com/in/amr-ahmed-ramadan/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="amr ahmed" height="30" width="40" /></a> <a href="https://www.kaggle.com/amrmoro" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/kaggle.svg" alt="amr ahmed ramadan" height="30" width="40" /></a> <a href="https://www.facebook.com/cvbnm1234568/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="amr ahmed" height="30" width="40" /></a> </p>

Project Link:</br>
   [![GitHub][project-shield]][project-url]

App Link:</br> 
   [![APP][app-shield]][app-url]
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments :gift_heart::gift:

* [README](https://github.com/othneildrew) (Othneil Drew)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/amrsss/prepayment-predicition-deploy-django/graphs/contributors
[forks-shield]: https://img.shields.io/badge/coverage-80%25-yellowgreen
[forks-url]: https://github.com/amrsss/prepayment-predicition-deploy-django/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/amrsss/prepayment-predicition-deploy-django/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/amrahmed-swe/prepayment-predicition-deploy-django/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/amr-ahmed-ramadan/
<!-- Languages-->
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[django-shield]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[html-shield]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white
[css-shield]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[js-shield]:https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[numpy-shield]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[pandas-shield]:https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white
[scikit-shield]: https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white
[heroku-shield]: https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white
[tweeter-shield]: https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FAmrSiri
[tweeter-url]: https://twitter.com/AmrSiri
[project-shield]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[project-url]: https://github.com/amrsss/prepayment-predicition-deploy-django
[app-shield]: https://img.shields.io/badge/APP-app%20link-orange
[app-url]: https://prepayment-prediction-b.herokuapp.com/
[product-screenshot]: Screenshots/home-form.png
