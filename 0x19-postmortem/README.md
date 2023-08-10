<nav>
    <nav>
        <nav><a href="https://intranet.alxswe.com/"></a>
            <nav><a href="https://intranet.alxswe.com/"></a><a href="https://intranet.alxswe.com/">
                    <div><br></div>
                </a></nav>
            <main>
                <div><br></div>
                <article>
                    <h1>0x19. Postmortem</h1>
                    <div>
                        <div>DevOps Sys Admin</div>
                    </div>
                    <div>
                        <ul>
                            <li>&nbsp;By: Barnabas Moses Yabilsu&nbsp;</li>
                        </ul>
                    </div>
                    <div>
                        <div>
                            <h3>Concepts</h3>
                        </div>
                        <div>
                            <p><em>For this project, we expect you to look at this concept:</em></p>
                            <ul>
                                <li><a href="https://intranet.alxswe.com/concepts/39">On-call</a></li>
                            </ul>
                        </div>
                    </div>
                    <div>
                        <h2>Background Context</h2>
                        <p><a href="https://youtu.be/rp5cVMNmbro" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/tWUPWmR.png" alt=""></a></p>
                        <p>Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error&hellip; Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won&rsquo;t happen again. Failing is fine, but failing twice because of the same issue is not.</p>
                        <p>A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:</p>
                        <ul>
                            <li>To provide the rest of the company&rsquo;s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.</li>
                            <li>And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.</li>
                        </ul>
                        <h2>Resources</h2>
                        <p><strong>Read or watch</strong>:</p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/rltoken/vkEjk-M6yBWW-wyB-7-I9Q" title="Incident Report, also referred to as a Postmortem" target="_blank">Incident Report, also referred to as a Postmortem</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/QwvgCYt2zjKRT7qMRe7I8A" title="The importance of an incident postmortem process" target="_blank">The importance of an incident postmortem process</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/kBjhT2PIr4X-U8FLI97--Q" title="What is an Incident Postmortem?" target="_blank">What is an Incident Postmortem?</a></li>
                        </ul>
                        <h2><br></h2>
                    </div>
                    <h2>Tasks</h2>
                    <div>
                        <div>
                            <h3>0. My first postmortem</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <p><a href="https://twitter.com/devopsreact/status/834887829486399488" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif" alt=""></a></p>
                            <p>Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Issue Summary (that is often what executives will read) must contain:<ul>
                                        <li>duration of the outage with start and end times (including timezone)</li>
                                        <li>what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)</li>
                                        <li>what was the root cause</li>
                                    </ul>
                                </li>
                                <li>
                                    <p>Timeline (format bullet point, format:&nbsp;<code>time</code> -&nbsp;<code>keep it short, 1 or 2 sentences</code>) must contain:</p>
                                    <ul>
                                        <li>when was the issue detected</li>
                                        <li>how was the issue detected (monitoring alert, an engineer noticed something, a customer complained&hellip;)</li>
                                        <li>actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)</li>
                                        <li>misleading investigation/debugging paths that were taken</li>
                                        <li>which team/individuals was the incident escalated to</li>
                                        <li>how the incident was resolved</li>
                                    </ul>
                                </li>
                                <li>
                                    <p>Root cause and resolution must contain:</p>
                                    <ul>
                                        <li>explain in detail what was causing the issue</li>
                                        <li>explain in detail how the issue was fixed</li>
                                    </ul>
                                </li>
                                <li>
                                    <p>Corrective and preventative measures must contain:</p>
                                    <ul>
                                        <li>what are the things that can be improved/fixed (broadly speaking)</li>
                                        <li>a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory&hellip;)</li>
                                    </ul>
                                </li>
                                <li>
                                    <p>Be brief and straight to the point, between 400 to 600 words</p>
                                </li>
                            </ul>
                            <p>While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.</p>
                            <p>Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.</p>
                        </div>
                        <div>
                            <div>
                                <h4>Add URLs here:</h4>
                                <div><br></div>
                                <ol>
                                    <li><a target="_blank" href="https://docs.google.com/document/d/1oOuMM83J_sZ3HuDFuGjKdxAXzxcGw7B2ZROU5CdbxB8/edit?usp=drivesdk">https://docs.google.com/document/d/1oOuMM83J_sZ3HuDFuGjKdxAXzxcGw7B2ZROU5CdbxB8/edit?usp=drivesdk</a></li>
                                </ol>
                            </div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x19-postmortem</code></li>
                                    <li>File:&nbsp;<code>README.md</code></li>
                                </ul>
                            </div>
                        </div>
                        <div><br></div>
                    </div>
                    <div>
                        <div>
                            <h3>1. Make people want to read your postmortem</h3>
                            <div>#advanced</div>
                        </div>
                        <div>
                            <p>We are constantly stormed by a quantity of information, it&rsquo;s tough to get people to read you.</p>
                            <p>Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.</p>
                            <p>Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.</p>
                        </div>
                        <div>
                            <div>
                                <h4>Add URLs here:</h4>
                                <div><br></div>
                                <ol>
                                    <li><a target="_blank" href="https://docs.google.com/document/d/1fOczdHaELq2CGQgQHeQ-p6HvpVByxaOiIDkZphy_k3A/edit?usp=drivesdk">https://docs.google.com/document/d/1fOczdHaELq2CGQgQHeQ-p6HvpVByxaOiIDkZphy_k3A/edit?usp=drivesdk</a></li>
                                </ol>
                            </div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x19-postmortem</code></li>
                                    <li>File:&nbsp;<code>README.md</code></li>
                                </ul>
                            </div>
                        </div>
                        <div><br></div>
                    </div>
                    <div><br></div>
                </article>
                <div>Copyright &copy; 2023 DUKURMA, All rights reserved.</div>
            </main>
        </nav>
    </nav>
</nav>
<main><br></main>
