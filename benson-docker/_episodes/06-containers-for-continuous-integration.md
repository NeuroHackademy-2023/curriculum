---
title: "Containers used in generating this lesson"
teaching: 20
exercises: 0
questions:
- "How can containers be useful to me for building websites?"
objectives:
- "Demonstrate how to construct a website using containers to transform a specification into a fully-presented website."
keypoints:
- "The generation of this lesson website can be effected using a container."
---
The website for this lesson is generated mechanically, based on a set of files that specify the configuration of the site, its presentation template, and the content to go on this page. This is far more manageable than editing each webpage of the lesson separately, for example, if the page header needs to change, this change can be made in one place, and all the pages regenerated. The alternative would be needing to edit each page to repeat the change: this is not productive or suitable work for humans to do!

In your shell window, in your `docker-intro` create a new directory `build-website` and `cd` into it. We will later be expanding a ZIP file into this directory later.

Now open a web browser window and:
1. Navigate to the GitHub repository that contains the files for this session, at <https://github.com/richford/docker-introduction/>;
2. Click the green "Clone or download" button on the right-hand side of the page;
3. Click "Download ZIP".
4. The downloaded ZIP file should contain one directory named `docker-introduction-gh-pages`.
5. Move the `docker-introduction-gh-pages` folder into the `build-website` folder you created above.

> ## There are many ways to work with ZIP files
> Note that the last two steps can be achieved using a Mac or Windows graphical user interface. There are also ways to effect expanding the ZIP archive on the command line, for example, on my Mac I can achieve the effect of those last two steps through running the command `unzip ~/Downloads/docker-introduction-gh-pages.zip`.
{: .callout}

In your shell window, if you `cd` into the `docker-introduction-gh-pages` folder and list the files, you should see something similar to what I see:
~~~
$ cd docker-introduction-gh-pages
$ ls
~~~
{: .language-bash}
~~~
AUTHORS			_episodes		code
CITATION		_episodes_rmd		data
CODE_OF_CONDUCT.md	_extras			fig
CONTRIBUTING.md		_includes		files
LICENSE.md		_layouts		index.md
Makefile		aio.md			reference.md
README.md		assets			setup.md
_config.yml		bin
~~~
{: .output}

You can now request that a container is created that will compile the files in this set into the lesson website, and will run a simple webserver to allow you to view your version of the website locally. Note that this command will be long and fiddly to type, so you probably want to copy-and-paste it into your shell window. This command will continue to (re-)generate and serve up your version of the lesson website, so you will not get your shell prompt back until you type <kbd>control</kbd>+<kbd>c</kbd>. This will stop the webserver, since it cleans away the container.

> ## If you happen to have the `make` tool already installed...
> We are taking an atypical approach in using the command that follows, since you are not required to have set up the `make` tool on your computer. However you may want to see whether you happen to have `make` installed anyway, by typing `make docker-serve` instead of the command below. At worst, this will fail and you can use the command shown below.
{: .callout}

For macOS, Linux and PowerShell:
~~~
$ docker run --rm -it -v ${PWD}:/srv/jekyll -p 127.0.0.1:4000:4000 jekyll/jekyll:pages jekyll serve
~~~
{: .language-bash}

For `cmd.exe` shells on Microsoft Windows:
~~~
> docker run --rm -it -v "%CD%":/srv/jekyll -p 127.0.0.1:4000:4000 jekyll/jekyll:pages jekyll serve
~~~

When I ran the macOS command, the output was as follows:
~~~
Unable to find image 'jekyll/jekyll:pages' locally
pages: Pulling from jekyll/jekyll
cbdbe7a5bc2a: Already exists 
aa8ae8202b42: Already exists 
b21786fe7c0d: Already exists 
68296e6645b2: Already exists 
6b1c37303e2d: Already exists 
4d49f4d60e44: Pull complete 
Digest: sha256:3741cb6d48b1ed3c544db4af9e2485fba31ddb5c2deb83a93b33fd252e8e2768
Status: Downloaded newer image for jekyll/jekyll:pages
ruby 2.7.1p83 (2020-03-31 revision a0c7c23c9c) [x86_64-linux-musl]
Configuration file: /srv/jekyll/_config.yml
            Source: /srv/jekyll
       Destination: /srv/jekyll/_site
 Incremental build: disabled. Enable with --incremental
      Generating... 
      Remote Theme: Using theme carpentries/carpentries-theme
                    done in 2.996 seconds.
 Auto-regeneration: enabled for '/srv/jekyll'
    Server address: http://0.0.0.0:4000
  Server running... press ctrl-c to stop.
~~~
{: .output}

In the preceding output, you see Docker downloading the image for Jekyll, which is a tool for building websites from specification files such as those used for this lesson. The line `jekyll serve` indicates a command that runs within the Docker container instance. The output below that is from the Jekyll tool itself, highlighting that the website has been built, and indicating that there is a server running.

Open a web browser window and visit the address <http://localhost:4000/>. You should see a site that looks very similar to that at <https://richford.github.io/docker-introduction/>.

Using a new shell window, or using your laptop's GUI, locate the file `index.md` within the `docker-introduction-gh-pages` directory, and open it in your preferred editor program.

Near the top of this file you should see the description starting "This session aims to introduce the use of Docker containers with the goal of using them to effect reproducible computational environments." Make a change to this message, and save the file.

If you reload your web browser, the change that you just made should be visible. This is because the Jekyll container saw that you changed the `index.md` file, and regenerated the website.

You can stop the Jekyll container by clicking in its terminal window and typing <kbd>control</kbd>+<kbd>c</kbd>.

You have now achieved using a reproducible computational environment to reproduce a lesson about reproducible computing environments.

{% include links.md %}

{% comment %}
<!--  LocalWords:  keypoints _episodes_rmd CODE_OF_CONDUCT.md aio.md
 -->
<!--  LocalWords:  CONTRIBUTING.md LICENSE.md index.md reference.md
 -->
<!--  LocalWords:  README.md setup.md _config.yml webserver srv
 -->
<!--  LocalWords:  jekyll x86_64-linux-musl favicons github.io
 -->
<!--  LocalWords:  links.md _episodes_rmd _config.yml endcomment
 -->
{% endcomment %}
