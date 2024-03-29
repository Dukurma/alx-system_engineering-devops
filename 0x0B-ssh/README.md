<table style="width: 100%;">
    <tbody>
        <tr>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
        </tr>
        <tr>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
        </tr>
        <tr>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
        </tr>
        <tr>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
        </tr>
        <tr>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
        </tr>
        <tr>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
            <td style="width: 25.0000%;"><br></td>
        </tr>
    </tbody>
</table>
<nav>
    <main>
        <article>
            <div>
                <div>
                    <h1>0x0B. SSH</h1>
                    <div>
                        <div>DevOpsSSHNetworkSysAdminSecurity</div>
                    </div>
                    <div>
                        <ul>
                            <li>&nbsp;By:&nbsp;Sylvain Kalache</li>
                            <li>&nbsp;Weight:&nbsp;1</li>
                            <li>&nbsp;Project will start&nbsp;<span title="">Jun 23, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jun 26, 2023 6:00 AM</span></li>
                            <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Jun 24, 2023 12:00 AM</span></li>
                            <li>&nbsp;An auto review will be launched at the deadline</li>
                        </ul>
                    </div>
                    <div>
                        <div>
                            <h2>Background Context</h2>
                            <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif" alt=""></p>
                            <p>Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using&nbsp;<code>ssh</code>. But contrary to level 2, you will not connect using a password but an RSA key. We&rsquo;ve configured your server with the public key you created in the first task of&nbsp;<a href="https://intranet.alxswe.com/rltoken/UQIQV4HJGvBv0qrHhlDFaQ" title="a previous project" target="_blank">a previous project</a> shared in your&nbsp;<a href="https://intranet.alxswe.com/rltoken/8ZlNV0J-sa-dijhmhJolOg" title="intranet profile" target="_blank">intranet profile</a>.</p>
                            <p>You can access your server information in the&nbsp;<a href="https://intranet.alxswe.com/rltoken/e2_s_pXwBVuYbhrvoesfrg" title="my servers" target="_blank">my servers</a> section of the intranet, each line with contains the IP and username you should use to connect via&nbsp;<code>ssh</code>.</p>
                            <p><strong>Note:</strong> Your server is configured with an Ubuntu 20.04 LTS environment.</p>
                            <h2>Resources</h2>
                            <p><strong>Read or watch</strong>:</p>
                            <ul>
                                <li><a href="https://intranet.alxswe.com/rltoken/dkgW9lKiBRiUZHfq0MDJuw" title="What is a (physical) server - text" target="_blank">What is a (physical) server - text</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/AxFcTdcXUCsrVp01X_EbFA" title="What is a (physical) server - video" target="_blank">What is a (physical) server - video</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/ux0eM1QU9reNyG45b0erAQ" title="SSH essentials" target="_blank">SSH essentials</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/Rc9FpSy4ZaQWPlcWLinbNw" title="SSH Config File" target="_blank">SSH Config File</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/tOcxk5mtkedBM0WxyDZxTw" title="Public Key Authentication for SSH" target="_blank">Public Key Authentication for SSH</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/j0atjRrVfZ6F810qmPfAzA" title="How Secure Shell Works" target="_blank">How Secure Shell Works</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/FKqd8CjxExmpWGu6xGavKw" title="SSH Crash Course" target="_blank">SSH Crash Course</a> (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)</li>
                            </ul>
                            <p><strong>For reference:</strong></p>
                            <ul>
                                <li><a href="https://intranet.alxswe.com/rltoken/JB-Vi4dR3q6nF4MBhsn8kQ" title="Understanding the SSH Encryption and Connection Process" target="_blank">Understanding the SSH Encryption and Connection Process</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/SpiYWE79Yfr_vWDg42dzCw" title="Secure Shell Wiki" target="_blank">Secure Shell Wiki</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/f2O0OQq9tch2MYeNAzkg5w" title="IETF RFC 4251 (Description of the SSH Protocol)" target="_blank">IETF RFC 4251 (Description of the SSH Protocol)</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/gd1W1UvB0KeJVWwM8BLvhA" title="Internet Engineering Task Force" target="_blank">Internet Engineering Task Force</a></li>
                                <li><a href="https://intranet.alxswe.com/rltoken/jb-IrnQnUh-PsEDlbAU0Kw" title="Request for Comments" target="_blank">Request for Comments</a></li>
                            </ul>
                            <p><strong>man or help</strong>:</p>
                            <ul>
                                <li><code>ssh</code></li>
                                <li><code>ssh-keygen</code></li>
                                <li><code>env</code></li>
                            </ul>
                            <h2>Learning Objectives</h2>
                            <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/0Wgw_i87NIVCfUcRzdZgkg" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
                            <h3>General</h3>
                            <ul>
                                <li>What is a server</li>
                                <li>Where servers usually live</li>
                                <li>What is SSH</li>
                                <li>How to create an SSH RSA key pair</li>
                                <li>How to connect to a remote host using an SSH RSA key pair</li>
                                <li>The advantage of using&nbsp;<code>#!/usr/bin/env bash</code> instead of&nbsp;<code>/bin/bash</code></li>
                            </ul>
                            <h3>Copyright - Plagiarism</h3>
                            <ul>
                                <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
                                <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</li>
                                <li>You are not allowed to publish any content of this project.</li>
                                <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
                            </ul>
                            <h2>Requirements</h2>
                            <h3>General</h3>
                            <ul>
                                <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
                                <li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
                                <li>All your files should end with a new line</li>
                                <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
                                <li>All your Bash script files must be executable</li>
                                <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
                                <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
                            </ul>
                        </div>
                    </div>
                    <h2>Your servers</h2>
                    <div>
                        <div>
                            <table>
                                <thead>
                                    <tr>
                                        <th>Name</th>
                                        <th>Username</th>
                                        <th>IP</th>
                                        <th>State</th>
                                        <th><br></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>222546-web-01</td>
                                        <td><code>ubuntu</code></td>
                                        <td><code>54.85.88.78</code></td>
                                        <td>running</td>
                                        <td>
                                            <div><button type="button">Actions&nbsp;Toggle Dropdown</button></div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <h2>Tasks</h2>
                    <div>
                        <div>
                            <div>
                                <h3>0. Use a private key</h3>
                                <div>mandatory</div>
                            </div>
                            <div>
                                <p>Write a Bash script that uses&nbsp;<code>ssh</code> to connect to your server using the private key&nbsp;<code>~/.ssh/school</code> with the user&nbsp;<code>ubuntu</code>.</p>
                                <p>Requirements:</p>
                                <ul>
                                    <li>Only use&nbsp;<code>ssh</code> single-character flags</li>
                                    <li>You cannot use&nbsp;<code>-l</code></li>
                                    <li>You do not need to handle the case of a private key protected by a passphrase</li>
                                </ul>
                                <pre><code>sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$ 
</code></pre>
                            </div>
                            <div>
                                <div>
                                    <p><strong>Repo:</strong></p>
                                    <ul>
                                        <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                        <li>Directory:&nbsp;<code>0x0B-ssh</code></li>
                                        <li>File:&nbsp;<code>0-use_a_private_key</code></li>
                                    </ul>
                                </div>
                            </div>
                            <div>
                                <div>
                                    <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button></div>
                                    <div><br></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div>
                            <div>
                                <h3>1. Create an SSH key pair</h3>
                                <div>mandatory</div>
                            </div>
                            <div>
                                <p>Write a Bash script that creates an RSA key pair.</p>
                                <p>Requirements:</p>
                                <ul>
                                    <li>Name of the created private key must be&nbsp;<code>school</code></li>
                                    <li>Number of bits in the created key to be created 4096</li>
                                    <li>The created key must be protected by the passphrase&nbsp;<code>betty</code></li>
                                </ul>
                                <p>Example:</p>
                                <pre><code>sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key&apos;s randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$ 
</code></pre>
                            </div>
                            <div>
                                <div>
                                    <p><strong>Repo:</strong></p>
                                    <ul>
                                        <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                        <li>Directory:&nbsp;<code>0x0B-ssh</code></li>
                                        <li>File:&nbsp;<code>1-create_ssh_key_pair</code></li>
                                    </ul>
                                </div>
                            </div>
                            <div>
                                <div>
                                    <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button></div>
                                    <div><br></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div>
                            <div>
                                <h3>2. Client configuration file</h3>
                                <div>mandatory</div>
                            </div>
                            <div>
                                <p>Your machine has an SSH configuration file for the local SSH client, let&rsquo;s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.</p>
                                <p>Requirements:</p>
                                <ul>
                                    <li>Your SSH client configuration must be configured to use the private key&nbsp;<code>~/.ssh/school</code></li>
                                    <li>Your SSH client configuration must be configured to refuse to authenticate using a password</li>
                                </ul>
                                <p>Example:</p>
                                <pre><code>sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 47: Applying options for *
debug1: Connecting to 98.98.98.98 port 22.
debug1: Connection established.
debug1: identity file /home/sylvain/.ssh/school type -1
debug1: identity file /home/sylvain/.ssh/school-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
debug1: Local version string SSH-2.0-OpenSSH_8.1
debug1:Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4ubuntu0.5
debug1: match: OpenSSH_7.6p1 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: server-&gt;client aes128-ctr hmac-sha1-etm@openssh.com none
debug1: kex: client-&gt;server aes128-ctr hmac-sha1-etm@openssh.com none
debug1: sending SSH2_MSG_KEX_ECDH_INIT
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ECDSA bd:03:f8:6a:12:28:d6:17:85:c1:b6:91:f1:da:0f:37
debug1: Host &apos;98.98.98.98&apos; is known and matches the ECDSA host key.
debug1: Found key in /home/sylvain/.ssh/known_hosts:1
debug1: ssh_ecdsa_verify: signature correct
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: SSH2_MSG_SERVICE_REQUEST sent
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Trying private key: /home/sylvain/.ssh/school
debug1: key_parse_private2: missing begin marker
debug1: read PEM private key done: type RSA
debug1: Authentication succeeded (publickey).
Authenticated to 98.98.98.98 ([98.98.98.98]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Sending environment.
debug1: Sending env LANG = en_US.UTF-8
ubuntu@magic-server:~$
</code></pre>
                                <p>In the example above, we can see that&nbsp;<code>ssh</code> tries to authenticate using&nbsp;<code>school</code> and does not try to authenticate using a password. You can replace&nbsp;<code>98.98.98.98</code> by the IP of your server for testing purposes.</p>
                            </div>
                            <div>
                                <div>
                                    <p><strong>Repo:</strong></p>
                                    <ul>
                                        <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                        <li>Directory:&nbsp;<code>0x0B-ssh</code></li>
                                        <li>File:&nbsp;<code>2-ssh_config</code></li>
                                    </ul>
                                </div>
                            </div>
                            <div>
                                <div>
                                    <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button></div>
                                    <div><br></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div>
                            <div>
                                <h3>3. Let me in!</h3>
                                <div>mandatory</div>
                            </div>
                            <div>
                                <p>Now that you have successfully connected to your server, we would also like to join the party.</p>
                                <p>Add the SSH public key below to your server so that we can connect using the&nbsp;<code>ubuntu</code> user.</p>
                                <pre><code>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
</code></pre>
                            </div>
                            <div>
                                <div>
                                    <p><strong>Repo:</strong></p>
                                    <ul>
                                        <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                        <li>Directory:&nbsp;<code>0x0B-ssh</code></li>
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
                                <h3>4. Client configuration file (w/ Puppet)</h3>
                                <div>#advanced</div>
                            </div>
                            <div>
                                <p>Let&rsquo;s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we&rsquo;d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.</p>
                                <p>Requirements:</p>
                                <ul>
                                    <li>Your SSH client configuration must be configured to use the private key&nbsp;<code>~/.ssh/school</code></li>
                                    <li>Your SSH client configuration must be configured to refuse to authenticate using a password</li>
                                </ul>
                                <p>Example:</p>
                                <pre><code>vagrant@ubuntu:~$ sudo puppet apply 100-puppet_ssh_config.pp
Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds
Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created
Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created
Notice: Finished catalog run in 0.03 seconds
vagrant@ubuntu:~$
</code></pre>
                            </div>
                            <div>
                                <div>
                                    <p><strong>Repo:</strong></p>
                                    <ul>
                                        <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                        <li>Directory:&nbsp;<code>0x0B-ssh</code></li>
                                        <li>File:&nbsp;<code>100-puppet_ssh_config.pp</code></li>
                                    </ul>
                                </div>
                            </div>
                            <div>
                                <div>
                                    <div><button>&nbsp;Done!</button> <button>Help</button> <button>Check your code</button></div>
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
</nav>
<main><br></main>
