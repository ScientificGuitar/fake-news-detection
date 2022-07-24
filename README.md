# Fake News Detection

## TABLE OF CONTENTS

* [Background](#background)
* [Objective](#objective)
* [Tools and Packages](#tools)
* [Data Collection](#data-collection)

<hr>

## BACKGROUND 
With 2022 on track to be the worst year for South Africa for load shedding, the highest stage ever being implemented, and Eskom workers striking, conversations on social media has increased dramatically, with dissent towards Eskom growing.

<hr>

## OBJECTIVE 
<li>Gather fake news and real news from multiple websites.</li>
<li>Exploratory Data Analysis of both fake news and real news to investigate and learn some of the potential differences.</li> 
<li>Explore and compare different machine learning models and neural networks to classify news as fake or real.</li> 

<hr>

## TOOLS

<table style="width:100%">
  <tr>
    <th>Task</th>
    <th>Technique</th> 
    <th>Tools/Packages Used</th>
  </tr>
  <tr>
    <td>Data Collection</td>
    <td>Web scraping from multiple websites</td> 
    <td>requests, BeautifulSoup</td>
  </tr>
  <tr>
    <td>Environments &amp Platforms</td>
    <td></td> 
    <td>Jupyter Lab, VSCode</td>
  </tr>
</table><br>

<hr>

## DATA-COLLECTION

Originally sourced 53 possible fake news websites from https://www.factcheck.org/2017/07/websites-post-fake-satirical-stories/. Majority of these websites are for sale and no longer active, or have been sold and no longer post news. After removing those from the list, 13 websites remain.
These 13 websites are cross checked with https://mediabiasfactcheck.com/ to remove satire websites, and only use websites with Low and Very Low factual reporting. 10 Fake News websites remain.
After inspecting the websites to see that majority of posts are not articles and that the websites are static, only the following 7 websites remain to be scraped:
<li>https://americasfreedomfighters.com/</li>
<li>https://blingnews.com/</li>
<li>https://conservativepost.com/</li>
<li>https://theconservativetreehouse.com/</li>
<li>https://gellerreport.com/</li>
<li>https://newspunch.com/</li>
<li>https://rightwingtribune.com/</li>

<hr>