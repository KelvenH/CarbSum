# Testing 

## Contents
- [Summary of Main Bugs and Status](#summary-of-main-bugs-and-status)
- [Testing Against User Stories and Project Brief](#testing-against-user-stories-and-project-brief)
- [Manual Testing](#manual-testing)
- [Lighthouse Testing](#lighthouse-testing)
- [Code Validation](#code-validation)
  * [HTML](#html)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
- [Browser Compatability](#browser-compatability)
- [Responsiveness](#responsiveness)


------

## Summary of Main Bugs and Status

The table below outlines key bugs / defects for which further information can be found from the related testing section. The table focuses on matters which remain outstanding and their affect.   

Issue | Details | Refer to Testing Section | Status | Comments |
-----|----------|----------|-----|----------|
Passive Event Listener | Console log reported 'Violation Added non-passive event listener to scroll-blocking 'touchmove' event materialize.min.js', also identified by Lighthouse | Lighthouse Testing - Performance | Unresolved | Unable to resolve, attempts to add passive event listeners did not affect materialize.js. No apparent impact on site despite Chrome and Lighthouse warnings|
Responsivess - layout for larger screens | Not a bug / failure, but noted for future enhancement to improve the visual appeal on larger screens where content is strecthed wider than needed owing to the site being primarily built for mobile use | Responsiveness | Open | Future Enhancement


------

## Testing Against User Stories and Project Brief





------

## Manual Testing



------

## Lighthouse Testing

![lighthouse score](README%20Files/Lighthouse_scores.png)

Scores were quite high, but each section was investigated further. No changes were applied as a result - key reasons noted below), 1 point related to a known matter (passive event handler) which is noted in the summary table above;

### Performance 95%
- There was a reported opportunity to improve page rendering times by 1.3s. However, the majority were related to externally linked tools (i.e. materialize & jquery). It signified there was a slight benefit in moving some styles from the linked style.css file to in line styles, but this was not deemed to be a significant benefit and could potentially make the site harder to maintain.

- Time savings of c. 0.1s were also identified for 'unused CSS and JavaScript', however these styles / scripts are used by the site.

- Diagnostics - identified 'does not use passive listeners to improve scrolling performance'. This seemingly relates to a Violation reported in the console (Added non-opassive event listener). This relates to materialize.min.js. Attempts were made to resolve by adding passive event listeners but had no affect. Issue noted in bugs summary table.
![chrome violation](README%20Files/Chrome_violation.png)

### Accessibility 92%

- Background and foreground colors do not have a sufficient contrast ratio - point acknowledged but no changes applied to color scheme. Some of these relate to buttons intentionally 'de-focused' as relate to futture developments/ not currently active.

- Link does not have discernible name - this related to materialize side-nav not having a href value. This is per the structure of the materialize element, whilst there is no href attribute for this item, it was not removed for concern of possible unkown consequences.

### Best Practices 100%
- no recommendations / fails

### SEO 92%
- Links are not crawable - this relates to few instances where planned functionality has been held back for future development. The buttons remain on the page, but are marked and styled to indicate inactive.

------

## Code Validation

### HTML 

![HTML Validator Initial](README%20Files/HTMLvalidator-initial.png)

Reviewed with W3C Markup Validation Service. Initial check identified;
- 5 instances of Bad Values - all related to white space in media file links. These were corrected (both media file names and related SRC links).
- 1 Section Lacking H2 - H6 Heading. This relates to Section on HTML used for displaying Flash message. No further action taken as not required.
 
![HTML Validator Post](README%20Files/HTMLvalidator-post.png)



### CSS

![CSS Validator](README%20Files/CSSvalidator.png)

Reviewed with W3C CSS Validation Service. Review identified 13 errors, which can be grouped as;
- 1 x Value Error : caused by materialize.css (no action taken)
- 3 x value + parse errors: caused by erroneous space between rgb and colo value (resolved)
- 4 x background-image too few values : these are linear gradients using 2 var root color referrences. Not clear why identified as an error (reviewed but no action taken)
- 4 x wrong value for grid-template-column : had been used to state the number of columns required, but now changed to reflect 1fr each (fixed)

There were also 514 Warnings for which no action has been take as;
- c. 20 x unknown vendor extensions : all relate to color vairables declared in root. These were reviewed and seem to be stated correctly (no action taken)
- c. 500 x unkowne vendor extension errors relating to materialize (no further action taken)
![CSS Validator Post](README%20Files/CSSvalidatorpost.png)

### JavaScript

![JSHint initial](README%20Files/JSHint%20initial.png)

Reviewed with JSHint. Initially there were 51 findings, following review this was reduced to 2;
- 6 x missing / unneccessary semi-colons: reviewed and addressed (fixed)
- 43 x 'let' is available in es6 (use 'esversion: 6'): these were not errors, but I needed to ammend the JSHint configuration to accept newer JS features (not errors)
- 1 x Expected assignment or function call and saw an expression : this comes from a function i've acknowledged to another developer (to toggle show / hide of password). I have reviewed but not been able to remedy, but the function is providing the desired behaviour (not fixed, but no problem caused)
- 1 x The body of a for in should be wrapped in an if statement : simple for loop, nt clear why this is flagged (no action taken)

![JSHint post](README%20Files/JSHint%20post.png)


### Python

![PEP8-initial](README%20Files/PEP8-initial.png)

The app.py script was checked using PEP8 online. Initially, there were 10 findings all of which were resolved. These can be grouped as;
- 6 x script too long : all fixed. Note that applying a fix to one of these required a break in a text string (flash message content). This was resolved by applying three quotation marks at the start and end of the multi-line string.
- 1 x continutation line under-indented : (fixed)
- 1 x too many blank lines : (fixed)
- 1 x expected 2 blank lines found 4 : (fixed)
- 1 x no new line at end of file : (fixed)
 
![PEP8-initial](README%20Files/PEP8-initial.png)

Note, there is an additional 'problem' reported in the IDE regarding 'env imported but unused'. Not found guidance on-line but unconcerned as this import is required for production site whereas development / workspace access via the env.py file (which is not shared online). 

![app.py-problem](README%20Files/app.py-problem.png)
  
  
  
------  
  
## Browser Compatability
The CSS was run through https://autoprefixer.github.io/ to apply additional CSS tags.

Live testing was performed on https://www.lambdatest.com/ across key browsers, operating systems and resolution sizes. No major issues were noted.


------

## Responsiveness

This site has been developed from a mobile first approach - as it is intended that this would primarily be used on small mobile devices. Pages can scale accordingly for larger screens if desired. Additionally the following development decisions support responsivness;

- font unit sizes are primarily set in REM, with the based REM set to 10px (which has aided calculation of font sizes in development).
- a series of responsive font groups were also established in the css file and used across the site. 
- unit measurements (e.g. height / width / padding / margins) are typically set in VH / VW units (with the exception of measurements coming from materialize)
- the site has been built using the materialize framework with all pages structured using grid layout which scales accordingly.

It should be noted that whilst the page is responsive, it is acknowledged that aspects are larger than they need to be on wide / larger screens. Whilst this does not prohibt use of the site / features, further enhancmenets could be applied to improve the visual layout (noted as a future enhancement).

Local testing was performed on;

- mobile (iOS)
- tablet (ios)
- medium screen (Safari & Chrome)
- wide-screen (Safari & Chrome

Live testing performed on https://www.lambdatest.com/ for a selection of other screen resolution sizes / browsers.



