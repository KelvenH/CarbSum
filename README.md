insert logo here

***

TL:DR; 
- `CarbSum` is a tool to support Type 1 Diabetics who perform carb counting to manage the amount of insulin taken with food and drinks. Carb counting is the practice of working out how many carbohydrates are present in the food and drink being consumed which is then calculated against their personal carb to insulin ratios to determine the correct level of insulin to be taken (which is called a bolus). The tool aims to act as both a reference tool (how much carbs are typically present in the food item) but also a simple calculator. More enhanced features such as saving favourites and building a complete meal aim to make daily life easier by reducing the time taken to establish the carbs useful when at home but also perhaps more importantly when eating out / on the go when you do not have access to weighing scales. 

This supports working with both labelled (nutritional values are printed) and unlabelled meals such as home cooked or raw (fruit / vegetables). Some common examples are;

    - a packet of biscuits states 60g of carbs per 100g weight - but how do you determine the carbs for a single biscuit when you do not have access to weighing scales?
    - packet of pasta states the uncooked nutritional values, but what is it once cooked (given the nutritional ratio changes due to the amount of water absorbed)?
    - a home cooked meal consists of multiple ingredients, how can the calculations of each of these be more readily obtained?  

- Key features of `CarbSum`;
  Quick access (no log in required) to;
    - editable database of food items, search by category, name or tags
    - calculator which determines amount of carbs present when the value per 100g is provided

  If logged in, access to personalised features such as;
    - save common items as favourites - making reference quicker
    - build meals, i.e. equivalent to a playlist of multiple items which can be individually edited (both portion and carbs) 
    - create new items to expand the list
    - apply tags to improve the search / find functionality (e.g. baked or fried, brand names)

- link to deployed site (with icons)

***
Screenshot
***

## Contents
- [Disclaimer](#disclaimer)
- [About](#about)
    * [What is Diabetes?](#what-is-diabetes)
    * [How Is Diabetes Treated?](#how-is-diabetes-treated)
    * [So How Does CarbSum Come into This?](#so-how-does-carbsum-come-into-this)
    * [Links to external references](#links-to-external-references)
-  [User Experience Design - UI/UX](#user-experience-design)
    * [Problem Statement](#problem-statement)
    * [Intended Users](#intended-users)
    * [User Stories](#user-stories)
    * [Design Principles](#design-principles)
- Scope
- Structure
    * Content 
    * Features
    * Data
- Skeleton
- Surface
    * Styles (Mood Board images / extracts)
    * Images / Icons (?)
- Technologies Used
- Testing (including against User Stories)
- Bugs & Defects (link to list plus call out any major o/s)
- Future Enhancements
- Deployment
- Acknowledgements

```
example - how to reference specific code sections
```

------

## Disclaimer
Special Note: This project is for educational purposes and to support management of Type 1 Diabetes via the 'carb counting' approach. It is not intended, nor should it be inferred that this provides any form of dietary or medical advice. Please see disclaimer section below which also provides links to external sites for more information on Diabetes, insulin therapy management and carb counting. 


------

## About

### What is Diabetes?
In its simplest form, Diabetes is a serious condition which affects the body's blood glucose levels. Everybody needs to fuel their body with glucose (sugar) as this provides energy for the body to function (both internally and physically). Glucose is present in many (but not all!) of the foods and drinks we consume. Our digestive system breaks down the nutrients into small molecules for our body to absorb, along with the breakdown of other nutrients, minerals and vitamins, carbohydrates are broken down into glucose. 

In a typical healthy person, the pancreas senses when glucose has entered the bloodstream and releases the right amount of a hormone called insulin. This acts as a key which lets cells within muscles and organs absorb the glucose. There's far more to it than that (such as the body’s natural release of insulin at specific times of the day).

Type 1 Diabetes (T1) is an auto-immune disease whereby the immune system has attacked and destroyed the insulin producing cells in the pancreas. Without insulin, the glucose cannot enter the cells; blood sugar levels will rise (hyperglycaemic). Conversely, too little glucose (hypoglycaemic) is equally serious. Someone with either hypo / hyper blood sugar levels may struggle to function properly as they feel severe fatigue, dizziness, confusion, impaired vision. The way that body attempts to manage excess glucose or seek alternative sources of energy can also lead to long term consequences if not managed appropriately.


--
### How Is Diabetes Treated?
There is currently no 'cure' for T1 - but medical advancements coupled with good management techniques can significantly reduce the occurrence of hypos / hypers and therefore reduce the likelihood of short term and long-term health consequences. Diabetics need to administer insulin to mimic the natural rise and decrease of insulin - and that's 24hours not just at mealtimes!

There are a variety of approaches, but typically diabetics will have an approach which manages levels 'round the clock' (basal) and for mealtimes /food in-take (bolus). 


--
### So How Does CarbSum Come into This?
CarbSum is a tool which is specifically intended to support Diabetics using an approach known as 'carb counting'. As mentioned earlier, it's vital to ensure that the body receives the right level of insulin. There are 2 key parts to this calculation;

```
Amount of carbs   x    insulin (mmols) per carb    =     insulin (mmols) to be administered
```

The second part of the equation (how much insulin should they receive per gram of carbs) is completely unique to each individual and is agreed with the Diabetic's doctor / medical support team and will have a range of factors (age, type of insulin, etc) **this app in no way makes any recommendations to this part of the formula and patients should always follow the advice of their doctor / medical support team** 

But what it does do is help with the initial input - the amount of carbs being consumed.


--
### Isn't this information already available?
Often yes, food labelling is generally good, restaurants tend to have better understanding & able to share nutritional information, good resources / apps exist. But as a parent of a T1 Diabetic (son was diagnosed at the age of 2!) my wife and I encounter a variety of 'challenges'. Each on their own may not be that significant but multiply that by the number of times we need to reach for the calculator each day and there's an opportunity to make life that bit easier. Additionally, as our son nears an age of having to take more control, I also want to ensure he has tools to minimise impact upon his life. The UI / UX section below goes into the specific challenges in more detail.

Thank you for taking the time to read the above, below are some recommended links to external sites for more information and support on Diabetes ........ now onto the fun stuff!

### Links to external references
Add external links here!!!!



------
## User Experience Design - UI/UX

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

   * Fats Flag! (![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) earmarked for removal or consider as future enhancement) - the amount of fats being consumed can also affect glucose levels as they can lengthen the time it takes the body to absorb sugars. A higher fat content meal (like pizza) can take hours for the digestive system to extract the sugars by which time the rapid acting insulin delivered as a bolus may have ended - pushing glucose levels up. The ability to 'flag' certain food items helps  to remind users where additional considerations maybe needed (e.g. increase basal an hour later, or use a square wave bolus where a portion of the bolus is delivered gradually over a specified time period).


---

   ### Intended Users
   `CarbSum` is intended to be used by Type 1 Diabetics and / or parents / guardians who follow the 'carb counting' technique to support their insulin therapy.
    
   
----

   ### User Stories
   
   #### New User
   * access the site without registering to see if this is use to me
   * be able to register easily 
    
   #### All Users (i.e. incl existing users without need to 'sign-in)
   * easily find items by name and / or appropriate categorisations
   * adjust parameters (e.g. weight / portion sizes; cooked / uncooked; preparation style e.g. fried / baked)
   * understand / verify how the carb values have been calculated
   * create / edit / delete own versions of item card & edit carb values
   * ability to add notes
  
   #### Existing User (Signed in)
   * sign in / out easily
   * save 'favourite' items
   * create 'menu' of a collection of items
   * submit new card for review / approval by site admin for visibility by all site visitors
   *  

---
  ### Design Principles 
  The following design principles are informed by the problem statement and user stories and underpin the design and feature set;
  * Design a website / app which provides quick and easy calculations of food carbohydrates (used as an input to determine insulin needs).
  * Clear categorisations (with additional 'tags' for quick identification)
  * Ability to adjust 'size' of portion (e.g. weight, portion, volume)
  * Distinction of preparation type; for example, roast potato vs. mashed potato (to be managed via 'tags')
  * Enable 'quick' use i.e. access core functions without need to sign-in
  * Further 'personalised' options available after sign-in
  * Minimal use of images and animations to enhance screen loading times
  * Allow user to build a menu of multiple items and save for future use
  * Allow users to create their own entries and edit existing entries (including previously saved menus)
  * Add an alarm feature - used to support reminder where later bolus is also required
  
  
 ------

## Scope



------

##  Structure
  ### Content
  ### Features
  ### Data



------

##  Skeleton

Low Fidelity - wireframe image;

![Low Fidelity Wireframe](https://user-images.githubusercontent.com/73842369/127049903-2efe8cae-9393-4b8e-939f-38102f983b4f.png)


Medium Fidelity - video demo of wireframes & screen flow:

https://user-images.githubusercontent.com/73842369/127034187-cd119b08-f024-4296-a49b-4599be8f1b3b.mp4




------

##  Surface

### Mood Board images

![CarbSum Moodboard - Imagery](https://user-images.githubusercontent.com/73842369/127062370-47eebf88-8c9c-48cc-85f4-68c4bc9d3806.png)


 ### Typography & Colors
 
![CarbSum Moodboard - Fonts   Colors](https://user-images.githubusercontent.com/73842369/127062386-1df4f221-4000-4632-99df-9f40c4d638ef.png)




------

## Languages, Frameworks and Technologies Used

### Design & Development; 
- Adobe XD (UI / UX development stage)
- Lucidchart (process mapping of functions) 

### Build Stage
- GitHub (host repo)
- GitPod / VS Code (building code)
- HTML5
- CSS3
- Materialize (html / css styles framework)
- FontAwesome
- Python
- Flask
- Jinja (templating HTML)

### Back End
- MongoDB (hosting database)

### Testing
- Lighthouse
- HTML Validator
- .......css / python / responsiveness / pythontutor

### Deployment
- Heroku 

### Miscellaneous
Linters / extensions/ pword generator



------

## Testing (including against User Stories)



------

## Bugs & Defects (link to list plus call out any major o/s)



------

## Future Enhancements



------

## Deployment



------

## Acknowledgements
- BringYourOwnLaptop(BYOL) Youtube channel - used for guidance on UI / UX and using Adobe XD
- Carbsandcals.com

------
