![CarbSum image](README%20Files/Main-image.svg)

***

# Overview; 
- `CarbSum` is a tool to support Type 1 Diabetics who perform carb counting to manage the amount of insulin taken with food and drinks. The tool aims to act as both a reference point (how much carbs are typically present in the food item) but also a simple calculator. The aim is to make daily life easier by reducing the time taken to establish carbs useful when at home but also perhaps more importantly when eating out / on the go when you do not have access to weighing scales! 

This supports working with both labelled (nutritional values are printed) and unlabelled meals such as home cooked or raw (fruit / vegetables). Some common examples are;
 - a packet of biscuits states 60g of carbs per 100g weight - but how do you determine the carbs for a single biscuit when you do not have access to weighing scales?
 - packet of pasta states the uncooked nutritional values, but what is it once cooked (given the nutritional ratio changes due to the amount of water absorbed)?
 - a home cooked meal consists of multiple ingredients, how can the calculations of each of these be more readily obtained?  

- Key features of `CarbSum`;
  Quick access (no log in required) to;
    - editable database of food items, search by category, name or tags
    - calculator which determines amount of carbs present when the value per 100g is provided

  If logged in, access to personalised features such as;
    - create new items to expand the list
    - create variations of existing items
 

Link to live site [here] (https://carbsum.herokuapp.com/)

------
------

## Contents
- [Disclaimer](#disclaimer)
- [About](#about)
    * [What is Diabetes?](#what-is-diabetes)
    * [How Is Diabetes Treated?](#how-is-diabetes-treated)
    * [So How Does CarbSum Come into This?](#so-how-does-carbsum-come-into-this)
-  [User Experience UX](#user-experience-ux)
    * [Problem Statement](#problem-statement)
    * [Intended Users](#intended-users)
    * [User Stories](#user-stories)
- [Scope](#scope)
- [Structure](#structure)
    * [Design Principles and Features](#design-principles-and-features)
    * [Userflow and Screens](#userflow-and-screens)
    * [Data](#data)
    * [Features](#features)
- [Skeleton](#skeleton)
    * [Low Fidelity Wireframes](#low-fidelity-wireframes)
    * [Medium Fidelity Wireframes](#medium-fidelity-wireframes)
- [Surface](#surface)
    * [Mood Board Images](#mood-board-images)
    * [Typography and Colors](#typography-and-colors)
    * [Final Mock Up](#final-mock-up)
- [Technologies, Languages and Frameworks Used](#technologies-languages-and-frameworks-used)
- [Testing](#testing)
- [Bugs and Defects](#bugs-and-defects)
- [Future Enhancements](#future-enhancements)
- [Deployment](#deployment)
- [Acknowledgements](#acknowledgements)

------

## Disclaimer
Special Note: This project is for educational purposes and to support management of Type 1 Diabetes via the 'carb counting' approach. It is not intended, nor should it be inferred that this provides any form of dietary or medical advice. 


------

## About

### What is Diabetes?
In it's simplest form, Diabetes is a serious condition which affects the body's blood glucose levels. Everybody needs to fuel their body with glucose (sugar) as this provides energy for the body to function (both internally and physically). Glucose is present in many (but not all!) of the foods and drinks we consume. Our digestive system breaks down the nutrients into small molecules for our body to absorb and along with the breakdown of other nutrients, minerals and vitamins, carbohydrates are broken down into glucose. 

In a typical healthy person, the pancreas senses when glucose has entered the bloodstream and releases the right amount of a hormone called insulin. This acts as a key which lets cells within muscles and organs absorb the glucose. There's far more to it than that (such as the body???s natural release of insulin at specific times of the day).

Type 1 Diabetes (T1) is an auto-immune disease whereby the immune system has attacked and destroyed the insulin producing cells in the pancreas. Without insulin, the glucose cannot enter the cells; blood sugar levels will rise (hyperglycaemic). Conversely, too little glucose (hypoglycaemic) is equally serious. Someone with either hypo / hyper blood sugar levels may struggle to function properly as they feel severe fatigue, dizziness, confusion, impaired vision. The way that body attempts to manage excess glucose or seek alternative sources of energy can also lead to long term consequences if not managed appropriately.


---
### How Is Diabetes Treated?
There is currently no 'cure' for T1 - but medical advancements coupled with good management techniques can significantly reduce the occurrence of hypos / hypers and therefore reduce the likelihood of short term and long-term health consequences. Diabetics need to administer insulin to mimic the natural rise and decrease of insulin - and that's 24hours not just at mealtimes!

There are a variety of approaches, but typically diabetics will have an approach which manages levels 'round the clock' (basal) and for mealtimes / food in-take (bolus). 

Carb counting is the practice of working out how many carbohydrates are present in the food and drink being consumed which is then calculated against their personal carb to insulin ratios to determine the correct level of insulin to be taken (which is called a bolus). 

---
### So How Does CarbSum Come into This?
CarbSum is a tool which is specifically intended to support Diabetics using an approach known as 'carb counting'. As mentioned earlier, it's vital to ensure that the body receives the right level of insulin. There are 2 key parts to this calculation;

```
Amount of carbs   x    insulin (mmols) per carb    =     insulin (mmols) to be administered
```

The second part of the equation (how much insulin should they receive per gram of carbs) is completely unique to each individual and is agreed with the Diabetic's doctor / medical support team and will have a range of factors (age, type of insulin, etc) **this app in no way makes any recommendations to this part of the formula and patients should always follow the advice of their doctor / medical support team** 

But what it does do is help with the initial input - the amount of carbs being consumed.


---
### Isn't this information already available?
Often yes, food labelling is generally good, restaurants tend to have better understanding & able to share nutritional information, good resources / apps exist. But as a parent of a T1 Diabetic (son was diagnosed at the age of 2!) my wife and I encounter a variety of 'challenges'. Each on their own may not be that significant but multiply that by the number of times we need to reach for the calculator each day and there's an opportunity to make life that bit easier. Additionally, as our son nears an age of having to take more control, I also want to ensure he has tools to minimise impact upon his life. The UI / UX section below goes into the specific challenges in more detail.

Thank you for taking the time to read the above ........ now onto the fun stuff!



------
## User Experience UX

   ### Problem Statement
   The following problems summarise small scale field research with parents of Type 1 Diabetics and our own experiences;
   
   * Food labelling - can be good, but;
        - is often printed very small and / or lacks contrast with packaging (hard for grandparents and those with less than 20/20 vision to read!)
        - may not be present where labelling is only stated on main packaging but not on individual items (e.g. multi-packs)
        - often only states the minimum information requirement of carbs per 100g weight, additional calculations are needed to translate that to the actual weight being consumed (e.g. 1 sweet)
   - does not account for cooked weight (e.g. nutritional ratio of uncooked vs cooked pasta differ)
   - impact of cooking / preparation styles  (e.g. deep-fried vs oven baked)
   
   * Unlabelled - not all food types are labelled (raw ingredients such as fruit and vegetables), or common ingredients like adding milk to a tea! 
   
   * Multiple Calculations - meals prepared at home often consist of a mix of labelled and unlabelled and require multiple calculations. For example, a roast dinner consisting of potatoes & vegetables (unlabelled) with gravy (labelled). Throw a home-made Yorkshire pudding in and there's a mini collection for the flour, milk and eggs to consider! The ability to create a menu of meals would make this a lot quicker / easier especially if you could add / swap items and adjust the individual portion sizes.



---

   ### Intended Users
   `CarbSum` is intended to be used by Type 1 Diabetics and / or parents / guardians who follow the 'carb counting' technique to support their insulin therapy.
    
   
----

   ### User Stories
   
   #### As a User; 
   * I have the nutritional info and weight and want to be able to calculate the carbs quickly 
   * I am not in posession of the nutritional information and / or weight and want to be able to calculate the carbs quickly
   * I want to be able to seach and find food items quickly
   * I want to be able to register to access personalised features
   * I want clear guidance how to use the site

   #### As a Returning User; 
   * I want to be able to log into my account / dashboard
   * I want to be able to create my own personalised food items
   * I want to be able to change the values of my own personally created foods
   * I want to be able to filter / search my personally created foods easily
   * I want to be able to delete any food items I create
   * I don't want other users to access / ammend / delete food items I create

   #### As site owner;
   * I want to be able to create an account with admin priviledges
   * I want to be able to create / read / update and delete all site content
    

  
 ------

## Scope

### In Scope;
   The scope is defined to the parameters of being able to calculate food carbohydrates and associated inputs (i.e. food weights /  portion sizes, carb values).
   Satisfy the requirements of the user stories and map to the problem statement.

### Out of Scope;
   All other nutritional / dietary information is out of scope (i.e. calories, recommended food / carb intakes, etc).
   Any form of medical / diabetes advice.


------

##  Structure

  ### Design Principles and Features
  The following design principles are informed by the problem statement and user stories and underpin the design and feature set;
  * Design a website / app which provides quick and easy calculations of food carbohydrates (used as an input to determine insulin needs).
  * Clear categorisations (with additional 'tags' for quick identification)
  * Ability to adjust 'size' of portion (e.g. weight, portion, volume)
  * Distinction of preparation type; for example, roast potato vs. mashed potato (to be managed via 'tags')
  * Enable 'quick' use i.e. access core functions without need to sign-in
  * Further 'personalised' options available after sign-in
  * Minimal use of images and animations to enhance screen loading times
  * Allow user to build a menu of multiple items and save for future use
  * Allow users to create their own entries and edit existing entries 


  ### Userflow and Screens
  
![CarbSum Site Flow and Data Structure](https://user-images.githubusercontent.com/73842369/127577915-c7551ebc-8229-43d9-836a-8071a67f2109.png)

  ### Data
  Data is held in a series of collections hosted on MongoDB as displayed in the image below. 
  
  ![DBStructure](README%20Files/Final_DB_Structure.png)
  
  The primary bulk load of data was undertaken via Mongo Compass. This tool allowed the data to be compiled off-line in a CSV format spreadsheet. Compass connects to the databse using the same credentials as hed in the env.py file. Duirng the upload process, the field data types can be set. All Ids are auto-generated by Mongo upoon load.
  Data created / edited via the front end app only requires specific data type rules for the numerical fields to ensure that these are parsed as float (decimal) values. Mongo auto-determines the data-tpes and applies the BSON type of Double. This ensures that when the data is pulled back into the front end that any numeical fields can be used for the required calculations.
  
---  
  
  ### Features
 
 | Key Feature | Available | Delivered | Notes |
 |-------------|-----------|-----------|-------|
 | Nav bar + mobile side nav | All Users | Yes | - |
 | Recorded Demos | All Users | Yes | 4 .mp4 files created |
 | Quick Calc. | All Users | Yes | includes upto 4 items + total |
 | Food Database | All Users | Yes | Loaded with c. 350 items |
 | Search Foods by text | Registered Users | Yes | - |
 | Search Foods by category | Registered Users | Yes | - |
 | Search Foods by tag | Registered Users | Yes* | Note outstanding bug with tags which impacts reliability of tags |
 | Create Account | All Users | Yes | - |
 | Log In | Registered Users | Yes | - |
 | Log Out | Registered Users | Yes | - |
 | View Dashboard | Registered Users | Yes | - |
 | Create Own Foods | Registered Users | Yes | - |
 | Search Own Foods | Registered Users | Yes | - |
 | Edit Own Foods | Registered Users | Yes | - |
 | Delete Own Foods | Registered Users | Yes | - |
 | Create / Edit / Delete Meal | Registered Users | No | Unable to implement in time, noted for future enhancement |

 

------

##  Skeleton

### Low Fidelity Wireframes

![Low Fidelity Wireframe](https://user-images.githubusercontent.com/73842369/127049903-2efe8cae-9393-4b8e-939f-38102f983b4f.png)


### Medium Fidelity Wireframes

Recorded demo of wireframes & screen flow:

https://user-images.githubusercontent.com/73842369/127034187-cd119b08-f024-4296-a49b-4599be8f1b3b.mp4



------

##  Surface

### Mood Board Images

![CarbSum Moodboard - Imagery](https://user-images.githubusercontent.com/73842369/127062370-47eebf88-8c9c-48cc-85f4-68c4bc9d3806.png)


 ### Typography and Colors
 
![CarbSum Moodboard - Fonts   Colors](https://user-images.githubusercontent.com/73842369/127062386-1df4f221-4000-4632-99df-9f40c4d638ef.png)


### Final Mock Up

![mobile-mock-up](README%20Files/mobile-mockup.png)


------

## Technologies, Languages and Frameworks Used

### Design & Development; 
- Adobe XD (UI / UX development stage)
- Lucidchart (process mapping of functions) 


### Build Stage
- GitHub (host repo)
- GitPod / VS Code (building code)
- HTML5
- CSS3
- Materialize (html / css styles framework)
- Python
- Flask
- Jinja (templating HTML)


### Back End
- MongoDB (hosting database)
- Mongo Compass (bulk data uploader)


### Testing
- Lighthouse
- W3C Markup Validation Service (HTML)
- W3C CSS Validation Service (CSS)
- JSHint (JS)
- PEP8 online (Python)
- autoprefixer (browser compatability extensions)
- lamdatest.com (browser / os compatability, responsiveness testing)


### Deployment
- Heroku 

### Miscellaneous
- Adobe Illustrator (hero image)
- Adboke Photoshop (mobile screen mock-up)



------

## Testing
- please refer to seperate [testing.md](https://github.com/KelvenH/CarbSum/blob/main/Testing.md) page for full details of testing undertaken. Note that significant bugs / defects are summarised in the following section.


------

## Bugs and Defects 

- please refer to seperate [testing.md](https://github.com/KelvenH/CarbSum/blob/main/Testing.md) page for full details of testing undertaken. Note that significant bugs / defects are summarised in the following section.

Issue | Details | Refer to Testing Section | Status | Comments |
|-----|----------|----------|-----|----------|
Passive Event Listener | Console log reported 'Violation Added non-passive event listener to scroll-blocking 'touchmove' event materialize.min.js', also identified by Lighthouse | Lighthouse Testing - Performance | OPEN | Unable to resolve, attempts to add passive event listeners did not affect materialize.js. No apparent impact on site despite Chrome and Lighthouse warnings|
Responsivess - layout for larger screens | Not a bug / failure, but noted for future enhancement to improve the visual appeal on larger screens where content is strecthed wider than needed owing to the site being primarily built for mobile use | Responsiveness | OPEN | Future Enhancement
Updating Tags | Updating an existing record caused all tags to be selected for the multiple select options, and not just those applied | Development | OPEN |  Given tags work, decision made not to back this feature out, but focus was not given in the recorded demos due to possible unreliability. Understand the issue to relate to method attempted to loop through options but unable to solve in time for project submission |
Materialize Overrides | Complications / high number of unique css rules to target | Development | Closed | Styling issues resolved, but noted Future Enhancement to investigate alternative framework |
Fluid Measurements | Suspended inclusion of fluid measurements. Whilst ml appears as a dropdown alternative to grams, there are more widespread changes which need to be fully explored before these can be included.| Development | OPEN | Future Enhancement |


------

## Future Enhancements

- Capability to create Meals (effecively combination of Food Cards and Quick Calc for collection of multiple items) - WITHDRAWN due to project time constraints 
- Tags - (post fix of bug affecting updating records) expand list of Tags and apply to data-set
- Materialize - identify alternative styling framework to improve ongoing manage-ability of site
- Fluids - incorporate capability to capture carb values against fluid measurements (ml) 

------

## Deployment

The key components in deployment are:

- GitPod ??? development environment
- GitHub ??? repository 
- MongoDb ??? database
- Heroku ??? cloud hosting platform

The key deployment steps linking these components together are as follows.

### GitPod
To connect to MongoDB and deploy through Heroku within GitPod a requirements and Procfile were created.
These files are pushed to the repository on GitHub.

An env.py file is also created in GitPod which holds;
-	IP
-	PORT
-	SECRET_KEY (a unique secret key generated by an online password generator)
-	MONGO_URI (the Mongo address)
-	MONGO_DB (the database collection name)

This file is not pushed to GitHub given the secure nature of the information.
To prevent this being loaded, the env.py file is added to git.ignore.

### Heroku
A new app was created and connected to the GitHub repo (using the repo URL address).
The contents of the env.py file are stored directly in HeroKu app settings under Configuration Variables. This ensures that the details are accessible to he live environment without needing to be made publicly available on GitHub.
Once these details are provided, you are in a position to deploy the site. The initial build will take a few moments to build.


------

## Acknowledgements
- BringYourOwnLaptop(BYOL) Youtube channel - used for guidance on UI / UX and using Adobe XD
- Carbsandcals.com - key data source
- Tutor Support - specifically, Sean, Igor and Michael!
- Code Institute - template and course content (sepcifically Task Manager walkthrough)
- Seun Owonikoko - Mentor
- Code Institute - Nov-20 joiners WhatsApp Group
- Slack
- StackOverflow

------


