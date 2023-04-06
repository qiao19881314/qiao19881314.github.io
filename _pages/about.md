---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<span id="Biography" class="section-subheading">Biography</span>
<!-- ====== -->

Yongliang Qiao (Member, IEEE) received the B.S. degree in electrical engineering and automation and the M.S. degree in agricultural electriﬁcation and automation from Northwest A&F University, Xianyang, China, and the Ph.D. degree in computer science from the University of Technology of Belfort-Montbéliard, Belfort, France. He was a Research Associate with the Australian Centre for Field Robotics, University of Sydney, Australia. His research interests include smart farming, agricultural robots, deep learning, multi-sensor fusion, and intelligent perception.

{% include education.html %}

<span id="News" class="section-subheading">News</span>
{% include News.html %}

<span id="Publications" class="section-subheading">Publications</span>
  <ul>
  {% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}
  </ul>

<span id="Talks" class="section-subheading">Talks and presentations</span>
  {% include talkmap.html %}
  <ul>
  {% for post in site.talks reversed %}
    {% include archive-single-talk.html %}
  {% endfor %}
  </ul>


<span id="Patent" class="section-subheading">Patent</span>
  <ul>
  {% for post in site.patent reversed %}
    {% include archive-single-patent.html %}
  {% endfor %}
  </ul>

<span id="Honour" class="section-subheading">Honour</span>
  <ul>
  {% for post in site.honour reversed %}
    {% include archive-single-honour.html %}
  {% endfor %}
  </ul>

<span id="Services"></span>
  {% include service.html %}

<span id="Contact" class="section-subheading"></span>
  {% include Contact.html %}


<!-- Talks
======
  <ul>
  {% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}
  </ul>


Teaching
======
  <ul>
  {% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}
  </ul>


Service and leadership
======
* Currently signed in to 43 different slack teams -->

<!-- 个人Github信息小卡片 -->
<!-- ![Christmas's GitHub stats](https://github-readme-stats.vercel.app/api?username=Shunli-W&show_icons=true&theme=tokyonight) -->

<!-- 个人主页各个国家的访问人数 -->
<!-- <a href="https://flagcounter.me/details/doX"><img src="https://flagcounter.me/doX/" alt="Flag Counter"></a> -->

<!-- 主页访问人数 -->
<!-- ![Visitor Count](https://profile-counter.glitch.me/qiao19981314/count.svg)
![Visitor Count](https://komarev.com/ghpvc/?username=qiao19981314&label=PROFILE+VIEWS) -->
