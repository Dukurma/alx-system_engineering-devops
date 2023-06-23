<nav>
    <div><span style="text-align: inherit;">0x0A. Configuration management</span></div>
</nav>
<main>
    <article>
        <div>
            <div>
                <div>
                    <div>DevOpsSysAdminScriptingCI/CD</div>
                </div>
                <div>
                    <ul>
                        <li>&nbsp;By:&nbsp;Sylvain Kalache</li>
                        <li>&nbsp;Weight:&nbsp;1</li>
                        <li>&nbsp;Project will start&nbsp;<span title="">Jun 23, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jun 24, 2023 6:00 AM</span></li>
                        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Jun 23, 2023 12:00 PM</span></li>
                        <li>&nbsp;An auto review will be launched at the deadline</li>
                    </ul>
                </div>
                <div>
                    <div>
                        <h2>Background Context</h2>
                        <p><a href="https://youtu.be/ogYLFyp68cI" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230623%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230623T200456Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0ca063bc9e72fc2925431d03867883b2b6ccb1aa99dfa91a9ec9409e60cb0718" alt=""></a></p>
                        <p>When I was working for SlideShare, I worked on an auto-remediation tool called&nbsp;<a href="https://intranet.alxswe.com/rltoken/0zbIzBqH_ktMmRQvJwZs2A" title="Skynet" target="_blank">Skynet</a> that monitored, scaled and fixed Cloud infrastructure. I was using a parallel job-execution system called MCollective that allowed me to execute commands to one or multiple servers at the same time. I could apply an action to a selected set of servers by applying a filter such as the server&rsquo;s hostname or any other metadata we had (server type, server environment&hellip;). At some point, a bug was present in my code that sent&nbsp;<code>nil</code> to the filter method.</p>
                        <p>There were 2 pieces of bad news:</p>
                        <ol>
                            <li>When MCollective receives&nbsp;<code>nil</code> as an argument for its filter method, it takes this to mean &lsquo;all servers&rsquo;</li>
                            <li>The action I sent was to terminate the selected servers</li>
                        </ol>
                        <p>I started the parallel job-execution and after some time, I realized that it was taking longer than expected. Looking at logs I realized that I was shutting down SlideShare&rsquo;s entire document conversion environment. Actually, 75% of all our conversion infrastructure servers had been shut down, resulting in users not able to convert their PDFs, powerpoints, and videos&hellip; Pretty bad!</p>
                        <p>Thanks to Puppet, we were able to restore our infrastructure to normal operation in under 1H, pretty impressive. Imagine if we had to do everything manually: launching the servers, configuring and linking them, importing application code, starting every process, and obviously, fixing all the bugs (you should know by now that complicated infrastructure always goes sideways)&hellip;</p>
                        <p>Obviously writing Puppet code for your infrastructure requires an investment of time and energy, but in the long term, it is for sure a must-have.</p>
                        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/292/4i8il3B.gif" alt=""></p>
                        <p>That was me ^_^&lsquo;:&nbsp;<a href="https://intranet.alxswe.com/rltoken/jIyF-Oa80s40ssG21cyNAg" title="https://twitter.com/devopsreact/status/836971570136375296" target="_blank">https://twitter.com/devopsreact/status/836971570136375296</a></p>
                        <h2>Resources</h2>
                        <p><strong>Read or watch</strong>:</p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/rltoken/GL30hu-aRcKzPOvK8JO-Bg" title="Intro to Configuration Management" target="_blank">Intro to Configuration Management</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/WON0M4DNRabf88KAG_pDUA" title="Puppet resource type: file" target="_blank">Puppet resource type: file</a> (<em>check &ldquo;Resource types&rdquo; for all manifest types in the left menu</em>)</li>
                            <li><a href="https://intranet.alxswe.com/rltoken/0V2fBdafkfKPMxA1umea3Q" title="Puppet's Declarative Language: Modeling Instead of Scripting" target="_blank">Puppet&rsquo;s Declarative Language: Modeling Instead of Scripting</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/CRUMeEMdcX-UtbWsUM9xLQ" title="Puppet lint" target="_blank">Puppet lint</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/MzHXCntAkPzOqMnI6_rpWQ" title="Puppet emacs mode" target="_blank">Puppet emacs mode</a></li>
                        </ul>
                        <h2>Requirements</h2>
                        <h3>General</h3>
                        <ul>
                            <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
                            <li>All your files should end with a new line</li>
                            <li>A&nbsp;<code>README.md</code> file at the root of the folder of the project is mandatory</li>
                            <li>Your Puppet manifests must pass&nbsp;<code>puppet-lint</code> version 2.1.1 without any errors</li>
                            <li>Your Puppet manifests must run without error</li>
                            <li>Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about</li>
                            <li>Your Puppet manifests files must end with the extension&nbsp;<code>.pp</code></li>
                        </ul>
                        <h2>Note on Versioning</h2>
                        <p>Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.</p>
                        <h3>Install&nbsp;<code>puppet</code></h3>
                        <pre><code>$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
</code></pre>
                        <p>You do&nbsp;<strong>not</strong> need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet.</p>
                        <p><a href="https://intranet.alxswe.com/rltoken/fsIr2xFkJHTkaXwqZFFcbA" title="Puppet 5 Docs" target="_blank">Puppet 5 Docs</a></p>
                        <h3>Install&nbsp;<code>puppet-lint</code></h3>
                        <pre><code>$ gem install puppet-lint
</code></pre>
                    </div>
                </div>
                <h2>Tasks</h2>
                <div>
                    <div>
                        <div>
                            <h3>0. Create a file</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <p>Using Puppet, create a file in&nbsp;<code>/tmp</code>.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>File path is&nbsp;<code>/tmp/school</code></li>
                                <li>File permission is&nbsp;<code>0744</code></li>
                                <li>File owner is&nbsp;<code>www-data</code></li>
                                <li>File group is&nbsp;<code>www-data</code></li>
                                <li>File contains&nbsp;<code>I love Puppet</code></li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>root@6712bef7a528:~# puppet-lint --version
puppet-lint 2.5.2
root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
root@6712bef7a528:~# 
root@6712bef7a528:~# puppet apply 0-create_a_file.pp
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as &apos;{md5}f1b70c2a42a98d82224986a612400db9&apos;
Notice: Finished catalog run in 0.03 seconds
root@6712bef7a528:~#
root@6712bef7a528:~# ls -l /tmp/school
-rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
root@6712bef7a528:~# cat /tmp/school
I love Puppetroot@6712bef7a528:~#
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0A-configuration_management</code></li>
                                    <li>File:&nbsp;<code>0-create_a_file.pp</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>1. Install a package</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <p>Using Puppet, install&nbsp;<code>flask</code> from&nbsp;<code>pip3</code>.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Install&nbsp;<code>flask</code></li>
                                <li>Version must be&nbsp;<code>2.1.0</code></li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>root@9665f0a47391:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
root@9665f0a47391:/# flask --version
Python 3.8.10
Flask 2.1.0
Werkzeug 2.1.1
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0A-configuration_management</code></li>
                                    <li>File:&nbsp;<code>1-install_a_package.pp</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>2. Execute a command</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <p>Using Puppet, create a manifest that kills a process named&nbsp;<code>killmenow</code>.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Must use the&nbsp;<code>exec</code> Puppet resource</li>
                                <li>Must use&nbsp;<code>pkill</code></li>
                            </ul>
                            <p>Example:</p>
                            <p>Terminal #0 - starting my process</p>
                            <pre><code>root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
done

root@d391259bf577:/# ./killmenow
</code></pre>
                            <p>Terminal #1 - executing my manifest</p>
                            <pre><code>root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/# 
</code></pre>
                            <p>Terminal #0 - process has been terminated</p>
                            <pre><code>root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0A-configuration_management</code></li>
                                    <li>File:&nbsp;<code>2-execute_a_command.pp</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </article>
    <div>Copyright &copy; 2023 DUKURMA, All rights reserved.</div>
</main>
