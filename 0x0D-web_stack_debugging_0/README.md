<nav>
    <nav><br></nav>
    <main>
        <article>
            <h1>0x0D. Web stack debugging #0</h1>
            <div>
                <div>DevOps SysAdmin Scripting Debugging</div>
            </div>
            <div>
                <ul>
                    <li>&nbsp;By: Barnabas Moses Yabilsu</li>
                    <li>&nbsp;Project start &nbsp;date <span title="">June 27, 2023 8:44&nbsp; PM</span>,&nbsp;</li>
                    <li>Project deadline&nbsp;&nbsp;<span title="">June 28, 2023 6:00 AM</span></li>
                    <li>&nbsp;Checker will be released at <span title="">Jun 27, 2023 6:00 PM</span></li>
                    <li>&nbsp;An auto review will be launched at the deadline</li>
                </ul>
            </div>
            <div>
                <div>
                    <h3>Concepts</h3>
                </div>
                <div>
                    <p><em>For this project, we expect you to look at these concepts:</em></p>
                    <ul>
                        <li><a href="https://intranet.alxswe.com/concepts/33">Network basics</a></li>
                        <li><a href="https://intranet.alxswe.com/concepts/65">Docker</a></li>
                        <li><a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a></li>
                    </ul>
                </div>
            </div>
            <div>
                <div>
                    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/265/uWLzjc8.jpg" alt=""></p>
                    <h2>Background Context</h2>
                    <p>The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that&rsquo;s the &ldquo;fun&rdquo; part of the job!).</p>
                    <p>Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.</p>
                    <p>In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.</p>
                    <p>Let&rsquo;s start with a very simple example. My server must:</p>
                    <ul>
                        <li>have a copy of the&nbsp;<code>/etc/passwd</code> file in&nbsp;<code>/tmp</code></li>
                        <li>have a file named&nbsp;<code>/tmp/isworking</code> containing the string&nbsp;<code>OK</code></li>
                    </ul>
                    <p>Let&rsquo;s pretend that without these 2 elements, my web application cannot work.</p>
                    <p>Let&rsquo;s go through this example and fix the server.</p>
                    <pre><code>vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
Unable to find image &apos;ubuntu:14.04&apos; locally
14.04: Pulling from library/ubuntu
34667c7e4631: Already exists
d18d76a881a4: Already exists
119c7358fbfc: Already exists
2aaf13f3eff0: Already exists
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:14.04
76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
76f44c0da25e        ubuntu:14.04        &quot;/bin/bash&quot;         13 seconds ago      Up 12 seconds                           infallible_bhabha
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK &gt; /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/#
vagrant@vagrant:~$
</code></pre>
                    <p>Then my answer file would contain:</p>
                    <pre><code>sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK &gt; /tmp/isworking
sylvain@ubuntu:~$
</code></pre>
                    <p>Note that as you cannot use interactive software such as&nbsp;<code>emacs</code> or&nbsp;<code>vi</code> in your Bash script, everything needs to be done from the command line (including file edition).</p>
                    <h2>Installing Docker</h2>
                    <p>For this project you will be given a container which you can use to solve the task.&nbsp;<strong>If</strong> you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.</p>
                    <ul>
                        <li><a href="https://intranet.alxswe.com/rltoken/wuCgR0pVioCnvtMKTeMgdQ" title="Mac OS" target="_blank">Mac OS</a></li>
                        <li><a href="https://intranet.alxswe.com/rltoken/9nVKpuQIDJhZoLP4mZmbRA" title="Windows" target="_blank">Windows</a></li>
                        <li><a href="https://intranet.alxswe.com/rltoken/crVTooJdN8U8wATMvG2-og" title="Ubuntu 14.04" target="_blank">Ubuntu 14.04</a> (Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing)</li>
                        <li><a href="https://intranet.alxswe.com/rltoken/wTjFrD8iy96EZW9MFYwa9Q" title="Ubuntu 16.04" target="_blank">Ubuntu 16.04</a></li>
                    </ul>
                    <h2>Resources</h2>
                    <p><strong>man or help</strong>:</p>
                    <ul>
                        <li><code>curl</code></li>
                    </ul>
                    <h2>Requirements</h2>
                    <h3>General</h3>
                    <ul>
                        <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
                        <li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
                        <li>All your files should end with a new line</li>
                        <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
                        <li>All your Bash script files must be executable</li>
                        <li>Your Bash scripts must pass&nbsp;<code>Shellcheck</code> without any error</li>
                        <li>Your Bash scripts must run without error</li>
                        <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
                        <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
                    </ul>
                </div>
            </div>
            <h2>Tasks</h2>
            <div>
                <div>
                    <div>
                        <h3>0. Give me a page!</h3>
                        <div>mandatory</div>
                    </div>
                    <div>
                        <p>Be sure to read the&nbsp;<strong>Docker</strong> concept page</p>
                        <p>In this first debugging project, you will need to get&nbsp;<a href="https://intranet.alxswe.com/rltoken/HVGgLL51qmuulmw802M-Jg" title="Apache" target="_blank">Apache</a> to run on the container and to return a page containing&nbsp;<code>Hello Holberton</code> when querying the root of it.</p>
                        <p>Example:</p>
                        <pre><code>vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   &quot;/bin/bash&quot;         3 seconds ago       Up 2 seconds        0.0.0.0:8080-&gt;80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
</code></pre>
                        <p>Here we can see that after starting my Docker container, I&nbsp;<code>curl</code> the port&nbsp;<code>8080</code> mapped to the Docker container port&nbsp;<code>80</code>, it does not return a page but an error message. Note that you might also get the error message&nbsp;<code>curl: (52) Empty reply from server</code>.</p>
                        <pre><code>vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
</code></pre>
                        <p>After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains&nbsp;<code>Hello Holberton</code>. Paste the command(s) you used to fix the issue in your answer file.</p>
                    </div>
                    <div>
                        <div>
                            <p><strong>Repo:</strong></p>
                            <ul>
                                <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                <li>Directory:&nbsp;<code>0x0D-web_stack_debugging_0</code></li>
                                <li>File:&nbsp;<code>0-give_me_a_page</code></li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <div>
                            <div><button>&nbsp;Done?</button> <button>Help</button> <button>Get a sandbox</button></div>
                            <div><br><br></div>
                        </div>
                    </div>
                </div>
            </div>
        </article>
        <div>Copyright &copy; 2023 DUKURMA, All rights reserved.</div>
    </main>
</nav>
<main><br></main>
