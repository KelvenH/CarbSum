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
- [Details on Specific Bugs and Defects](#details-of-key-bugs-and-defects)

------

## Summary of Main Bugs and Status

Issue


Issue | Details | Refer to Testing Section | Status | Comments |
-----|----------|----------|-----|----------|
Passive Event Listener | Console log reported 'Violation Added non-passive event listener to scroll-blocking 'touchmove' event materialize.min.js', also identified by Lighthouse | Lighthouse Testing - Performance | Unresolved | Unable to resolve, attempts to add passive event listeners did not affect materialize.js. No apparent impact on site despite Chrome and Lighthouse warnings|





## Testing Against User Stories and Project Brief







## Manual Testing





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



## Code Validation

### HTML

### CSS

### JavaScript

### Python
  
  
  
  
  
  
  
## Browser Compatability







## Responsiveness









## Details on Specific Bugs



