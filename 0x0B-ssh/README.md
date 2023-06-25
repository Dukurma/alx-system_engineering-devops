<p>Toggle navigation</p>
<p>You just released the advanced tasks of this project. Have fun!</p>
<p>0x0B. SSH</p>
<p>DevOps</p>
<p>SSH</p>
<p>Network</p>
<p>SysAdmin</p>
<p>Security</p>
<p>&nbsp;By: Sylvain Kalache</p>
<p>&nbsp;Weight: 1</p>
<p>&nbsp;Project will start Jun 23, 2023 6:00 AM, must end by Jun 26, 2023 6:00 AM</p>
<p>&nbsp;Checker was released at Jun 24, 2023 12:00 AM</p>
<p>&nbsp;An auto review will be launched at the deadline</p>
<p>Background Context</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We&rsquo;ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.</p>
<p>&nbsp;</p>
<p>You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.</p>
<p>&nbsp;</p>
<p>Note: Your server is configured with an Ubuntu 20.04 LTS environment.</p>
<p>&nbsp;</p>
<p>Resources</p>
<p>Read or watch:</p>
<p>&nbsp;</p>
<p>What is a (physical) server - text</p>
<p>What is a (physical) server - video</p>
<p>SSH essentials</p>
<p>SSH Config File</p>
<p>Public Key Authentication for SSH</p>
<p>How Secure Shell Works</p>
<p>SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)</p>
<p>For reference:</p>
<p>&nbsp;</p>
<p>Understanding the SSH Encryption and Connection Process</p>
<p>Secure Shell Wiki</p>
<p>IETF RFC 4251 (Description of the SSH Protocol)</p>
<p>Internet Engineering Task Force</p>
<p>Request for Comments</p>
<p>man or help:</p>
<p>&nbsp;</p>
<p>ssh</p>
<p>ssh-keygen</p>
<p>env</p>
<p>Learning Objectives</p>
<p>At the end of this project, you are expected to be able to explain to anyone, without the help of Google:</p>
<p>&nbsp;</p>
<p>General</p>
<p>What is a server</p>
<p>Where servers usually live</p>
<p>What is SSH</p>
<p>How to create an SSH RSA key pair</p>
<p>How to connect to a remote host using an SSH RSA key pair</p>
<p>The advantage of using #!/usr/bin/env bash instead of /bin/bash</p>
<p>Copyright - Plagiarism</p>
<p>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</p>
<p>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</p>
<p>You are not allowed to publish any content of this project.</p>
<p>Any form of plagiarism is strictly forbidden and will result in removal from the program.</p>
<p>Requirements</p>
<p>General</p>
<p>Allowed editors: vi, vim, emacs</p>
<p>All your files will be interpreted on Ubuntu 20.04 LTS</p>
<p>All your files should end with a new line</p>
<p>A README.md file, at the root of the folder of the project, is mandatory</p>
<p>All your Bash script files must be executable</p>
<p>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</p>
<p>The second line of all your Bash scripts should be a comment explaining what is the script doing</p>
<p>Your servers</p>
<p>Name Username IP State&nbsp;</p>
<p>222546-web-01 ubuntu 54.85.88.78 running&nbsp;</p>
<p>Tasks</p>
<p>0. Use a private key</p>
<p>mandatory</p>
<p>Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.</p>
<p>&nbsp;</p>
<p>Requirements:</p>
<p>&nbsp;</p>
<p>Only use ssh single-character flags</p>
<p>You cannot use -l</p>
<p>You do not need to handle the case of a private key protected by a passphrase</p>
<p>sylvain@ubuntu$ ./0-use_a_private_key</p>
<p>ubuntu@server01:~$ exit</p>
<p>Connection to 8.8.8.8 closed.</p>
<p>sylvain@ubuntu$&nbsp;</p>
<p>Repo:</p>
<p>&nbsp;</p>
<p>GitHub repository: alx-system_engineering-devops</p>
<p>Directory: 0x0B-ssh</p>
<p>File: 0-use_a_private_key</p>
<p>&nbsp;&nbsp;</p>
<p>1. Create an SSH key pair</p>
<p>mandatory</p>
<p>Write a Bash script that creates an RSA key pair.</p>
<p>&nbsp;</p>
<p>Requirements:</p>
<p>&nbsp;</p>
<p>Name of the created private key must be school</p>
<p>Number of bits in the created key to be created 4096</p>
<p>The created key must be protected by the passphrase betty</p>
<p>Example:</p>
<p>&nbsp;</p>
<p>sylvain@ubuntu$ ls</p>
<p>1-create_ssh_key_pair</p>
<p>sylvain@ubuntu$ ./1-create_ssh_key_pair</p>
<p>Generating public/private rsa key pair.</p>
<p>Your identification has been saved in school.</p>
<p>Your public key has been saved in school.pub.</p>
<p>The key fingerprint is:</p>
<p>5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu</p>
<p>The key's randomart image is:</p>
<p>+--[ RSA 4096]----+</p>
<p>| oo... |</p>
<p>| .+.o = |</p>
<p>| o + B + |</p>
<p>| o. = O |</p>
<p>| .. S = . |</p>
<p>| .. . |</p>
<p>| E. . |</p>
<p>| .. |</p>
<p>| .. |</p>
<p>+-----------------+</p>
<p>sylvain@ubuntu$ ls</p>
<p>1-create_ssh_key_pair school school.pub</p>
<p>sylvain@ubuntu$&nbsp;</p>
<p>Repo:</p>
<p>&nbsp;</p>
<p>GitHub repository: alx-system_engineering-devops</p>
<p>Directory: 0x0B-ssh</p>
<p>File: 1-create_ssh_key_pair</p>
<p>&nbsp;&nbsp;</p>
<p>2. Client configuration file</p>
<p>mandatory</p>
<p>Your machine has an SSH configuration file for the local SSH client, let&rsquo;s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.</p>
<p>&nbsp;</p>
<p>Requirements:</p>
<p>&nbsp;</p>
<p>Your SSH client configuration must be configured to use the private key ~/.ssh/school</p>
<p>Your SSH client configuration must be configured to refuse to authenticate using a password</p>
<p>Example:</p>
<p>&nbsp;</p>
<p>sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98</p>
<p>OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014</p>
<p>debug1: Reading configuration data /etc/ssh/ssh_config</p>
<p>debug1: /etc/ssh/ssh_config line 47: Applying options for *</p>
<p>debug1: Connecting to 98.98.98.98 port 22.</p>
<p>debug1: Connection established.</p>
<p>debug1: identity file /home/sylvain/.ssh/school type -1</p>
<p>debug1: identity file /home/sylvain/.ssh/school-cert type -1</p>
<p>debug1: Enabling compatibility mode for protocol 2.0</p>
<p>debug1: Local version string SSH-2.0-OpenSSH_8.1</p>
<p>debug1:Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4ubuntu0.5</p>
<p>debug1: match: OpenSSH_7.6p1 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000</p>
<p>debug1: SSH2_MSG_KEXINIT sent</p>
<p>debug1: SSH2_MSG_KEXINIT received</p>
<p>debug1: kex: server-&gt;client aes128-ctr hmac-sha1-etm@openssh.com none</p>
<p>debug1: kex: client-&gt;server aes128-ctr hmac-sha1-etm@openssh.com none</p>
<p>debug1: sending SSH2_MSG_KEX_ECDH_INIT</p>
<p>debug1: expecting SSH2_MSG_KEX_ECDH_REPLY</p>
<p>debug1: Server host key: ECDSA bd:03:f8:6a:12:28:d6:17:85:c1:b6:91:f1:da:0f:37</p>
<p>debug1: Host '98.98.98.98' is known and matches the ECDSA host key.</p>
<p>debug1: Found key in /home/sylvain/.ssh/known_hosts:1</p>
<p>debug1: ssh_ecdsa_verify: signature correct</p>
<p>debug1: SSH2_MSG_NEWKEYS sent</p>
<p>debug1: expecting SSH2_MSG_NEWKEYS</p>
<p>debug1: SSH2_MSG_NEWKEYS received</p>
<p>debug1: SSH2_MSG_SERVICE_REQUEST sent</p>
<p>debug1: SSH2_MSG_SERVICE_ACCEPT received</p>
<p>debug1: Authentications that can continue: publickey,password</p>
<p>debug1: Next authentication method: publickey</p>
<p>debug1: Trying private key: /home/sylvain/.ssh/school</p>
<p>debug1: key_parse_private2: missing begin marker</p>
<p>debug1: read PEM private key done: type RSA</p>
<p>debug1: Authentication succeeded (publickey).</p>
<p>Authenticated to 98.98.98.98 ([98.98.98.98]:22).</p>
<p>debug1: channel 0: new [client-session]</p>
<p>debug1: Requesting no-more-sessions@openssh.com</p>
<p>debug1: Entering interactive session.</p>
<p>debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0</p>
<p>debug1: Sending environment.</p>
<p>debug1: Sending env LANG = en_US.UTF-8</p>
<p>ubuntu@magic-server:~$</p>
<p>In the example above, we can see that ssh tries to authenticate using school and does not try to authenticate using a password. You can replace 98.98.98.98 by the IP of your server for testing purposes.</p>
<p>&nbsp;</p>
<p>Repo:</p>
<p>&nbsp;</p>
<p>GitHub repository: alx-system_engineering-devops</p>
<p>Directory: 0x0B-ssh</p>
<p>File: 2-ssh_config</p>
<p>&nbsp;&nbsp;</p>
<p>3. Let me in!</p>
<p>mandatory</p>
<p>Now that you have successfully connected to your server, we would also like to join the party.</p>
<p>&nbsp;</p>
<p>Add the SSH public key below to your server so that we can connect using the ubuntu user.</p>
<p>&nbsp;</p>
<p>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN</p>
<p>Repo:</p>
<p>&nbsp;</p>
<p>GitHub repository: alx-system_engineering-devops</p>
<p>Directory: 0x0B-ssh</p>
<p>&nbsp; &nbsp;</p>
<p>4. Client configuration file (w/ Puppet)</p>
<p>#advanced</p>
<p>Let&rsquo;s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we&rsquo;d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.</p>
<p>&nbsp;</p>
<p>Requirements:</p>
<p>&nbsp;</p>
<p>Your SSH client configuration must be configured to use the private key ~/.ssh/school</p>
<p>Your SSH client configuration must be configured to refuse to authenticate using a password</p>
<p>Example:</p>
<p>&nbsp;</p>
<p>vagrant@ubuntu:~$ sudo puppet apply 100-puppet_ssh_config.pp</p>
<p>Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds</p>
<p>Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created</p>
<p>Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created</p>
<p>Notice: Finished catalog run in 0.03 seconds</p>
<p>vagrant@ubuntu:~$</p>
<p>Repo:</p>
<p>&nbsp;</p>
<p>GitHub repository: alx-system_engineering-devops</p>
<p>Directory: 0x0B-ssh</p>
<p>File: 100-puppet_ssh_config.pp</p>
<p>&nbsp;&nbsp;</p>
<p>Copyright &copy; 2023 DUKURMA, All rights reserved.</p>
