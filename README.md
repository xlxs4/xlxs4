<!-- by clydemdelores -->
<img src="https://raw.githubusercontent.com/xlxs4/xlxs4/master/assets/kanagawa.gif" align="right" width="20%" height="20%">

🧊 CS Undergrad.
Likes the Sci part in SciML.
Might look into the ML more in the future.
Found home in the Julia language.

I occasionally string sentences together over at https://xlxs4.github.io/.
You can find the latest reads below:

<!-- BLOG_START -->
- [JuliaSim Model Optimizer](https://xlxs4.github.io/notes/juliasim-model-optimizer/index.html) (2022-12-12)
- [ESA Design Booster](https://xlxs4.github.io/notes/esa-design-booster/index.html) (2022-11-22)
- [Second Brain](https://xlxs4.github.io/notes/second-brain/index.html) (2022-09-26)
<!-- BLOG_END -->

<br clear="right"/>

&nbsp;

```julia
using Dates

Base.@kwdef struct Orestis
    job::String = "student"
    bdate::Int = 2000
    website::String = "https://xlxs4.github.io/"
    current_projects::Vector{String}
end

age(d) = Dates.year(now()) - d.bdate
Base.summary(d::Orestis) = "Some $(age(d)) year old $(d.job)"
workson(d::Orestis) = d.current_projects 
hobbies(::Orestis) = ("BJJ", "analog photography", "piano", "cooking", "programming")
favorite_project(::Orestis) = "AcubeSAT nanosatellite"

# Begin my description
me = Orestis(current_projects = [
  "AcubeSAT", 
  "ModelingToolkit.jl"
])

println(summary(me))
println("works on: $(join(me.current_projects, ", "))")
println("has hobbies: $(join(hobbies(me), ", "))")
```

&nbsp;

<a href="https://github.com/xlxs4">
  <img align="center" src="https://github-readme-stats-xlxs4.vercel.app/api?username=xlxs4&count_private=true&hide=stars&hide_title=true&show_icons=true&theme=buefy" />
</a>
&nbsp;
<a href="https://github.com/xlxs4">
  <img align="center" src="https://github-readme-stats-xlxs4.vercel.app/api/top-langs/?username=xlxs4&hide=html,javascript,c,css,matlab&hide_title=true&layout=compact&langs_count=6&theme=buefy" />
</a>

&nbsp;

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/xlxs4/xlxs4/master/assets/acubesat-model-white.png">
  <img alt="A render of the AcubeSAT nanosatellite." src="https://raw.githubusercontent.com/xlxs4/xlxs4/master/assets/acubesat-model-black.png" align="left" width=20% height=20%>
</picture>
  
Sometimes I'm trying to send this nanosatellite in space.

This will let us know how gene expression changes in yeast cells.

The yeast will be cultured in-orbit!

I personally like to call it the "glorified yeast farm" myself.

<br clear="left"/>

&nbsp;

<a href="https://open.spotify.com/user/83zjpodyytr2zojufrnni850b">
    <img src="https://spotify-embed-xlxs4.vercel.app/api?theme=dark&scan=true" alt="Current Spotify Song" width="42%" align="right">
</a>

I've currently started dabbling in BJJ, analog photography and jazz (piano).

I like music a lot — this was *probably* the last thing I was listening to!

<br clear="right"/>

&nbsp;

<a href="https://gitlab.com/xlxs4">
  <img align="right" alt="@xlxs4's GitLab" width="21px" src="https://raw.githubusercontent.com/xlxs4/xlxs4/master/assets/gitlab.png" />
</a>
<a href="https://fosstodon.org/@xlxs4#">
  <img align="right" alt="@xlxs4's Mastodon" width="20px" src="https://raw.githubusercontent.com/xlxs4/xlxs4/master/assets/mastodon.png" />
</a>
<a href="https://stallman.org/rms-lifestyle.html#:~:text=I%20feel%20a%20responsibility%20not%20to%20contribute%20to%20the%20pressure%20on%20others.%20I%20hope%20my%20refusal%20to%20wear%20a%20tie%20will%20make%20it%20easier%20for%20you%20to%20refuse%20as%20well.">
  <img align="right" alt="@xlxs4's LinkedIn" width="20px" src="https://raw.githubusercontent.com/xlxs4/xlxs4/master/assets/linkedin.png" />
</a>
<a href="https://holopin.io/@xlxs4">
  <img align="right" alt="@xlxs4's Holopin" width="21px" src="https://raw.githubusercontent.com/xlxs4/xlxs4/master/assets/holopin.png" />
</a>
