<div>

<span class="c9"></span>

</div>

<span class="c29">Software Design Description</span>

<span class="c33 c36">Project: HarmonyBot</span>

<span class="c15"></span>

<span class="c15">Document Version 1.0</span>

<span class="c17">Version date 2/3/2023</span>

<span class="c17">https://github.com/sbourgeois02/HarmonyBot</span>

<span class="c17">School of Science, Technology and Health, Department of Computer Science,  
Biola University</span>

* * *

<span class="c9"></span>

<span class="c18">Table of Contents</span>

<span class="c18"></span>

<span class="c20">[1 Introduction](#h.rn2c9ejxzuo2)</span><span class="c20">        </span><span class="c20">[3](#h.rn2c9ejxzuo2)</span>

<span class="c14">[1.1 Product Overview](#h.5trm5u5nngum)</span><span class="c14">        </span><span class="c14">[3](#h.5trm5u5nngum)</span>

<span class="c14">[1.2 Document Version History](#h.dfrph6aemn18)</span><span class="c14">        </span><span class="c14">[3](#h.dfrph6aemn18)</span>

<span class="c14">[1.3 Document Intention](#h.9dokdxwgf7ef)</span><span class="c14">        </span><span class="c14">[3](#h.9dokdxwgf7ef)</span>

<span class="c14">[1.4 Feature Traceability Matrix](#h.liwvxug02jm1)</span><span class="c14">        </span><span class="c14">[4](#h.liwvxug02jm1)</span>

<span class="c20">[2 Architectural Design](#h.3wycifrs50bo)</span><span class="c20">        </span><span class="c20">[7](#h.3wycifrs50bo)</span>

<span class="c14">[2.1 Architectural Overview](#h.ayew9k3ui0h3)</span><span class="c14">        </span><span class="c14">[7](#h.ayew9k3ui0h3)</span>

<span class="c14">[2.2 Sequence of Interaction](#h.t0su44qsbvq6)</span><span class="c14">        </span><span class="c14">[8](#h.t0su44qsbvq6)</span>

<span class="c14">[2.3 Alternate Design Considerations](#h.7gbykbpq18qx)</span><span class="c14">        </span><span class="c14">[9](#h.7gbykbpq18qx)</span>

<span class="c17">[3 Components](#h.duzugtt62hfk)</span><span class="c17">        </span><span class="c17">[10](#h.duzugtt62hfk)</span>

<span class="c14">[3.1 Database Diagram](#h.iok67aimsn6h)</span><span class="c14">        </span><span class="c14">[10](#h.iok67aimsn6h)</span>

<span>[3.2 Database Description](#h.v4vx6h4rs4ed)</span><span>        </span><span>[11](#h.v4vx6h4rs4ed)</span>

<span class="c17">[4 User Interface Design](#h.urd6ndtz7os7)</span><span class="c17">        </span><span class="c17">[12](#h.urd6ndtz7os7)</span>

<span class="c9">[4.1 User Interface Description](#h.b4n97s3h6hr4)</span><span class="c9">        </span><span class="c9">[12](#h.b4n97s3h6hr4)</span>

<span>[4.2 Sample Screen Image](#h.u18duign2md7)</span><span>        </span><span>[12](#h.u18duign2md7)</span>

<span class="c18"></span>

* * *

<span class="c9"></span>

# <span class="c18">1 Introduction</span>

## <span class="c15">1.1        Product Overview</span>

<span class="c9">We are making an automatic, modular user (or "bot") for the Discord GUI that can assist in a variety of tasks, most notably storing table information on-sight and providing high-quality social interactions with users.</span>

## <span class="c15">1.2        Document Version History</span>

<a id="t.3a214fd4beefa08855a7fda776d5bf083ed30a13"></a><a id="t.0"></a>

<table class="c32">

<tbody>

<tr class="c44">

<td class="c37" colspan="1" rowspan="1">

<span class="c17">Version</span>

</td>

<td class="c19" colspan="1" rowspan="1">

<span class="c17">Primary Author(s)</span>

</td>

<td class="c19" colspan="1" rowspan="1">

<span class="c17">Description of Version</span>

</td>

<td class="c41" colspan="1" rowspan="1">

<span class="c17">Date Completed</span>

</td>

</tr>

<tr class="c23">

<td class="c37" colspan="1" rowspan="1">

<span class="c9">SDD v1.0</span>

</td>

<td class="c19" colspan="1" rowspan="1">

<span class="c9">Jonathan Yi,  
Matt Stoumbaugh,  
Nathan Schwantes,  
Seth Bourgeois</span>

</td>

<td class="c19" colspan="1" rowspan="1">

<span class="c9">Initial Version</span>

</td>

<td class="c41" colspan="1" rowspan="1">

<span>2/03</span><span class="c9">/2023</span>

</td>

</tr>

</tbody>

</table>

# <span class="c15"></span>

## <span class="c15">1.3        Document Intention</span>

<span class="c21">This document is intended for management and developers regarding</span> <span>the design and architecture of this project.</span> <span class="c9"> As a bot designed for both low and high level interactions, this document may be viewed and referenced by the consumer.</span>

* * *

## <span class="c15"></span>

## <span class="c15">1.4        Feature Traceability Matrix</span>

<span class="c22 c38">Project Name:</span><span class="c22"> HarmonyBot        </span><span class="c22 c38">Starting Date:</span><span class="c6">        January 13th, 2023        </span>

<span class="c22 c38">Project Description:</span><span class="c6"> A Discord bot designed for server moderation and basic interaction with its users</span>

<a id="t.866c31ebacc328286496d8e669c7a62e599e3ed7"></a><a id="t.1"></a>

<table class="c43">

<thead>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c33 c22">Feature Number</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c33 c22">Feature ID</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c33 c22">Feature Name</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c33 c22">Description</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c22 c33">Status</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c33 c22">Priority</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c33 c22">Root Feature</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">String Tokenizer</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Read and separate words in chat into tokens</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Basic (1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.1.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Reader</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Determine if a string is a command and read the string as such</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">String Tokenizer (1.1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">3</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.1.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Chat Reader</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Determine if a string is not a command and read it as part of basic chat</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">String Tokenizer (1.1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">4</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Permission Reading</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Determine the highest permission level of a user based on their role, enumerated in the “roles” table</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Basic (1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">5</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.2.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Role-based Command Denial</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Determine if a user has a high-enough permission level to use a command which they entered, refusing to execute if the user does not have a prerequisite permission level</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Permission Reading (1.2)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">6</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.3</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">User Moderation</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Establish two moderation tables and an additional column under the “Users” table to track Prohibited Language, Moderation Actions made by the bot, and number of rules violations, respectively</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Basic (1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">7</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.3.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Moderation Log</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A log of all the bot’s moderation actions and execution of built-in commands as well as who used them</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">User Moderation (1.3)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">8</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.3.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Timed Banlist</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A list of banned users, with an optional timer at the end of which the corresponding user is removed from the list</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Low</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">User Moderation (1.3)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">9</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.3.3</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Chat Deletion</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Delete a phrase containing prohibited language from the chat list</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">User Moderation (1.3)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">10</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.3.3</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Banned Language Table</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A list of words that are used to send rules violations to users if they are detected using any of the words</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">User Moderation (1.3)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">11</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Keep a list of built-in commands that cannot be deleted from the database.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Basic (1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">12</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Ban</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that bans a user, optionally for a limited time.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">13</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.1.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Unban</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that removes a ban status from a user.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Ban (1.4.1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">14</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Kick</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that removes a user from the server.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">15</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.3</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Mute</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that removes the user’s ability to chat for a set amount of time.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">16</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.3.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Unmute</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that restores a user’s ability to chat.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Mute (1.4.3)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">17</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.4</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Strike</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that assigns a rule violation to a user and optionally for a set amount of time and also sends a warning message.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">18</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.4.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Unstrike</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that removes a rule violation from a user.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Strike (1.4.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">19</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.4.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Clearstrike</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that removes all rule violations from a user.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Strike (1.4.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">20</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.4.3</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Strikes</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that views a user’s rule violations.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Strike (1.4.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">21</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.5</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Banlist</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that displays a list of banned users.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">22</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.6</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Modlist</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A command that displays the list of users with a set permission level.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">23</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.7</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Roles</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">View the list of roles and their corresponding permission levels</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">24</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.7.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Role Set</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Set a role’s corresponding permission level.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Roles (1.4.7)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">25</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.7.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Role Unset</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Reset a role’s corresponding permission level to the lowest one.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Roles (1.4.7)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">26</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.7.3</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Role Clear</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Remove a role from the table.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Roles (1.4.7)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">27</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.8</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">SetPerm [Command]</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Set the required permission level to execute a command</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">28</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.4.9</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Help</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">View a list of commands and their required permission levels</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Built-in Commands (1.4)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">29</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.5</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Creation</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Allowing users to create their own commands for the bot</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">In Progress</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Basic (1)</span>

</td>

</tr>

</thead>

<tbody>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">30</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.5.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Coding</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Create customizable and modular element of this bot</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Creation (1.5)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">31</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.5.1.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Add Command</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Create the ability to add a command to the database that the bot can execute</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Creation (1.5)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">32</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.5.1.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">WebGUI Add Command</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Add the ability to add commands from the web interface</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Creation (1.5)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">33</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.5.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Deletion</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Delete commands that have been added to that database</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Creation (1.5)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">34</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.5.2.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Delete Command</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Create the ability to delete a command from the discord interface</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Creation (1.5)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">35</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">1.5.2.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">WebGUI Delete Command</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Create the ability to delete the command from the Web GUI</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">High</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Creation (1.5)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">36</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">2.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Toggle Menu</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Create a menu that can toggle for enabling or disabling the use of individual commands</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Low</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Peripheral (2)</span>

<span class="c6"></span>

</td>

</tr>

<tr class="c0">

<td class="c26" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c46" colspan="1" rowspan="1">

<span class="c6"></span>

<span class="c6"></span>

</td>

<td class="c48" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c42" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

</tr>

<tr class="c0">

<td class="c49" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c11" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c11" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c45" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c47" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c11" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

<td class="c11" colspan="1" rowspan="1">

<span class="c6"></span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">37</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">2.1.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Command Toggling</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Implement the ability to enable or disable commands</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very Low</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Toggle Menu (2.1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">38</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">2.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Selectable Command Prefix</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Allow the user to change the default prefix (!) to their own prefix that the bot will recognize as the user inputting a command.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Low</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Peripheral (2)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">39</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">2.2.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Prefix Token Replacement</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Implement the ability to change the preset command prefix permanently</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very Low</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Selectable Command Prefix (2.2)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">40</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">2.3</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">User Interaction Commands</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">A list of harmless built-in commands intended for the lowest permission levels of users</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Low</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Peripheral (2)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">41</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">2.3.1</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Choose</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Randomly return a single token from a set of inputted tokens</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very Low</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">User Interaction Commands (2.3.1)</span>

</td>

</tr>

<tr class="c0">

<td class="c13" colspan="1" rowspan="1">

<span class="c6">42</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">2.3.2</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Respond/Ping</span>

</td>

<td class="c16" colspan="1" rowspan="1">

<span class="c6">Respond with a stock phrase or a timer indicating the bot’s response time.</span>

</td>

<td class="c2" colspan="1" rowspan="1">

<span class="c6">Not Started</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">Very Low</span>

</td>

<td class="c3" colspan="1" rowspan="1">

<span class="c6">User Interaction Commands (2.3.2)</span>

</td>

</tr>

</tbody>

</table>

<span class="c9"></span>

* * *

# <span class="c18"></span>

# <span>2</span> <span class="c18">Architectural Design</span>

## <span class="c15">2.1 Architectural Overview</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 331.00px; height: 311.00px;">![](./img/sddArchOverview.png)</span>

<span class="c21">Our application has two ways in which users can interact with the bot. The first way will be through the discord interface, which is provided for us by Discord. This is communicated with by the Discord API. The bot application is then coded in a language of our choice which will control the bot’s interaction between the database and the interface. The Web GUI allows management of the bot through a browser. This connects to a backend which will communicate these changes to the bot application and to the Bot database.</span>

<span class="c9"></span>

## <span class="c15">2.2 Sequence Diagrams</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 273.33px;">![](images/image2.png)</span>

<span class="c9"></span>

<span class="c9">When interacting with the bot through the Web GUI, once a command is executed from this interface it will send a signal to the backend that a command has been executed and gives it the information necessary to deal with it (i.e. the name of the command, the user it is being performed on, etc.). The backend will then communicate with the database to update the information necessary as well as alert the bot application that a command has been executed as well as telling it what information will be relevant for it to query in the database. The bot then checks the database for these changes and once it finds these, it updates the server by executing the necessary command and verifying that the command has been correctly executed. Once this is verified, it will return to the web backend that it has been completed and the web backend will update the GUI to display that the command was successfully executed.</span>

<span class="c9"></span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 321.33px;">![](images/image3.png)</span>

<span class="c9">When interacting with the bot through the discord interface, the user must type in a command. The bot application will then query the database to see if this command exists and once this is verified, it will query the database to ensure that the user has the proper permissions level in order to execute this command. Once these queries have been completed and all proper information has been verified, it will execute the command.</span>

## <span class="c15">2.3 Alternate Design Considerations</span>

<span class="c21">The main alternative consideration in our design was whether to connect the bot application to the web backend directly or to only have them connect indirectly through the MySQL database. By having them connect solely through the MySQL database, this would reduce the complexity of our project by eliminating the need to connect these two components. However, we decided to go with the approach of having them connected as this will reduce the time between an action being taken on the web interface and it resulting in a command in the discord interface. By connecting these components indirectly, the bot application would instead be required to periodically check the database for changes</span><span>, which is not ideal.</span>

<span class="c9">        </span>

# <span class="c18">3 Components</span>

## <span class="c15">3.1 Database Diagram</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 577.33px;">![](images/image1.png)</span>

* * *

## <span class="c15"></span>

## <span class="c15">3.1.1 Database Description</span>

<span class="c9">The User table has UserStatusID and UserRoleID, which map to the Status and Role table PrimaryKeys, respectively. Discord also uses User Tags, which are a 4-digit numerical ID used to allow for users with the same username. These tags are not unique, but when paired with the UserName, can uniquely ID a single user. Status and Role are calculated by ID, which are made the Primary Keys and stored as an INT for hierarchical calculations, but also stored as a string for user ease of viewing. The Commands table includes the CommandInput, which is what the user will type to activate the command, and either a CommandAction, which is code to be performed by the bot within Discord, and/or a CommandOutput, which the bot will type into the chat. The bot will compare CommandMinRoleID with the UserRoleID of the user trying to use the command, and if UserRoleID >= CommandMinRoleID execute the command, else return Invalid Permissions and deny execution. There will also be a list of “bad” words that the bot will scan the chat for in order to trigger a moderation. When triggered, it will log the offending user and the offending word, as well as the message that triggered the moderation. The moderation will also increase the UserNumStrikes value in the User table, and take the appropriate action based on the number of strikes.</span>

## <span class="c15">3.2        Bot Description</span>

<span class="c9">The computational portion of the bot will be stored directly on Discord’s servers using the discord.py library as a connection point. As the bot joins a specific server room, it becomes a constantly running Python program. NodeJS will be used to connect the bot to an external database that will enable the bot to utilize its intended features as listed in the Feature Traceability Matrix (1.4). The core feature of the bot is the string tokenizer and the text analyzer. The bot will be able to recognize if a message starts with the command prefix (currently planned to be hard-coded to “!”, but with plans to possibly allow the user to choose their own prefix), then parse the command, including any added variables, and run the command’s action and/or reply with the command’s output, as stored in the database. The bot will also analyze all messages for pre-defined (and user-added) words that will cause a moderation, as described in the Database Description (3.1.1). After logging the message, the offending message is deleted from the server, and as the number of strikes that a user has increases, so does the length of their timeout (mute), until on the final strike, they are banned from the server.</span>

# <span class="c18">4 User Interface Design</span>

## <span class="c15">4.1 User Interface Description</span>

<span class="c9">The user interface will be a web-based GUI that will allow the server moderators to access the data stored by HarmonyBot’s database. The GUI will show comprehensive lists of all the pertinent information at a glance, along with sorting options that the user can take advantage of to make sifting through the data easier. The user will also be able to access moderative features through the GUI including but not limited to: “add command”, “delete command”, and “ban user”.  </span>

## <span class="c15">4.2 Sample Screen Image</span>

<span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 382.67px;">![](images/image4.png)</span>
