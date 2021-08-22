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

Scores were quite high, but each score was investigated further;

### Performance 95%
- There was a reported opportunity to improve page rendering times by 1.3s. However, the majority were related to externally linked tools (i.e. materialize & jquery). It signified there was a slight benefit in moving some styles from the linked style.css file to in line styles, but this was not deemed to be a significant benefit and could potentially make the site harder to maintain.

- Time savings of c. 0.1s were also identified for 'unused CSS and JavaScript', however these styles / scripts are used by the site.

- Diagnostics - identified 'does not use passive listeners to improve scrolling performance'. This seemingly relates to a Violation reported in the console (Added non-opassive event listener). This relates to materialize.min.js. Attempts were made to resolve by adding passive event listeners but had no affect. Issue noted in bugs summary table.
![chrome violation](README%20Files/Chrome_violation.png)

### Accessibility 92%



### Best Practices 100%

### SEO 92%




## Code Validation

### HTML

### CSS

### JavaScript

### Python
  
  
  
  
  
  
  
## Browser Compatability







## Responsiveness









## Details on Specific Bugs



