<div>

<span class="c0"></span>

</div>

<span class="c4 c16">Software Requirements Specifications</span>

<span class="c4 c40">Project: HarmonyBot</span>

<span class="c12 c4"></span>

<span class="c12 c4">Document Version 1.0</span>

<span class="c4 c24">Version date 1/2</span><span class="c4">7</span><span class="c2">/2023</span>

<span class="c2">https://github.com/sbourgeois02/HarmonyBot</span>

<span class="c2">School of Science, Technology and Health, Department of Computer Science,  
Biola University</span>

* * *

<span class="c2"></span>

<span class="c19 c4">Table of Contents</span>

<span class="c0"></span>

<span class="c2">[1 INTRODUCTION](#h.agwbypn9860i)</span><span class="c2">        </span><span class="c2">[3](#h.agwbypn9860i)</span>

<span class="c0">[1.1 Product Overview](#h.93tgp7134x75)</span><span class="c0">        </span><span class="c0">[3](#h.93tgp7134x75)</span>

<span class="c0">[1.2 Document Version History](#h.dfrph6aemn18)</span><span class="c0">        </span><span class="c0">[3](#h.dfrph6aemn18)</span>

<span class="c0">[1.3 Document Intention](#h.9dokdxwgf7ef)</span><span class="c0">        </span><span class="c0">[3](#h.9dokdxwgf7ef)</span>

<span class="c2">[2 SPECIFIC REQUIREMENTS](#h.f07ojghvl6v3)</span><span class="c2">        </span><span class="c2">[4](#h.f07ojghvl6v3)</span>

<span class="c0">[2.1 External Interface Requirements](#h.xl2ttrt8y934)</span><span class="c0">        </span><span class="c0">[4](#h.xl2ttrt8y934)</span>

<span class="c0">[2.1.1 User Interfaces](#h.39dcoyeqb7sl)</span><span class="c0">        </span><span class="c0">[4](#h.39dcoyeqb7sl)</span>

<span class="c0">[2.1.2 Software Interfaces](#h.yuum9pa21dxe)</span><span class="c0">        </span><span class="c0">[4](#h.yuum9pa21dxe)</span>

<span class="c0">[2.1.2.1 Web Management Interface](#h.6egb6c8i5664)</span><span class="c0">        </span><span class="c0">[4](#h.6egb6c8i5664)</span>

<span class="c0">[2.1.3 Communications Protocols](#h.3hg6ine5qz6x)</span><span class="c0">        </span><span class="c0">[4](#h.3hg6ine5qz6x)</span>

<span>[2.2 Software Product Features](#h.wf8drbirof3b)</span><span>        </span><span>[5](#h.wf8drbirof3b)</span>

<span class="c0">[2.2.1 Foundational Features](#h.lhikehzb7cyx)</span><span class="c0">        </span><span class="c0">[5](#h.lhikehzb7cyx)</span>

<span class="c0">[2.2.2 Moderation Features](#h.8by3a36q1xtz)</span><span class="c0">        </span><span class="c0">[5](#h.8by3a36q1xtz)</span>

<span class="c0">[2.2.3 Interaction Features](#h.8v5co2icuebw)</span><span class="c0">        </span><span class="c0">[6](#h.8v5co2icuebw)</span>

<span class="c0">[2.3 Software System Attributes](#h.f6xfb9g77w96)</span><span class="c0">        </span><span class="c0">[6](#h.f6xfb9g77w96)</span>

<span class="c0">[2.3.1 Reliability](#h.slfiw1xozya1)</span><span class="c0">        </span><span class="c0">[6](#h.slfiw1xozya1)</span>

<span class="c0">[2.3.2 Availability](#h.vdhnsqth990a)</span><span class="c0">        </span><span class="c0">[6](#h.vdhnsqth990a)</span>

<span>[2.3.3 Security](#h.1ugczctfwszd)</span><span>        </span><span>[7](#h.1ugczctfwszd)</span>

<span class="c0">[2.3.4 Maintainability](#h.ylqcvrhzk1pt)</span><span class="c0">        </span><span class="c0">[7](#h.ylqcvrhzk1pt)</span>

<span class="c0">[2.3.5 Performance](#h.97hmbi5cn141)</span><span class="c0">        </span><span class="c0">[7](#h.97hmbi5cn141)</span>

<span class="c0">[2.4 Database Requirements](#h.1ukk4jkjbkzm)</span><span class="c0">        </span><span class="c0">[8](#h.1ukk4jkjbkzm)</span>

<span class="c0">[2.4.1 Concept Diagram](#h.fie2hlbd34n)</span><span class="c0">        </span><span class="c0">[8](#h.fie2hlbd34n)</span>

<span class="c0">[2.4.2 Description of Requirements](#h.8ll5biqosjxy)</span><span class="c0">        </span><span class="c0">[8](#h.8ll5biqosjxy)</span>

* * *

<span class="c19 c4"></span>

# <span class="c19 c4">1        INTRODUCTION</span>

## <span class="c12 c4">1.1        Product Overview</span>

<span class="c0">We are making an automatic, modular user (or "bot") for the Discord GUI that can assist in a variety of tasks, most notably storing table information on-sight and providing high-quality social interactions with users.</span>

## <span>1.2        </span><span class="c12 c4">Document Version History</span>

<a id="t.8c4b3af0900a644c94ba5119cc08997a2b9042d5"></a><a id="t.0"></a>

<table class="c25">

<tbody>

<tr class="c33">

<td class="c31" colspan="1" rowspan="1">

<span class="c2">Version</span>

</td>

<td class="c22" colspan="1" rowspan="1">

<span class="c2">Primary Author(s)</span>

</td>

<td class="c22" colspan="1" rowspan="1">

<span class="c2">Description of Version</span>

</td>

<td class="c38" colspan="1" rowspan="1">

<span class="c2">Date Completed</span>

</td>

</tr>

<tr class="c32">

<td class="c31" colspan="1" rowspan="1">

<span class="c0">SRS v1.0</span>

</td>

<td class="c22" colspan="1" rowspan="1">

<span class="c0">Jonathan Yi,  
Matt Stoumbaugh,  
Nathan Schwantes,  
Seth Bourgeois</span>

</td>

<td class="c22" colspan="1" rowspan="1">

<span class="c0">Initial Version</span>

</td>

<td class="c38" colspan="1" rowspan="1">

<span class="c24 c27">1/2</span><span>7</span><span class="c0">/2023</span>

</td>

</tr>

</tbody>

</table>

# <span class="c12 c4"></span>

## <span class="c12 c4">1.3        Document Intention</span>

<span class="c27 c35">This document is intended for management and developers regarding the technical specifications and requirements for the project. As a bot designed for both low and high level interactions, this document may be viewed and referenced by the consumer.</span>

* * *

# <span class="c19 c4">2        SPECIFIC REQUIREMENTS</span>

## <span class="c12 c4">2.1        External Interface Requirements</span>

### <span class="c2">2.1.1        User Interfaces</span>

<span class="c0">The majority of HarmonyBot’s basic operations can be performed using the basic interface provided by Discord.</span>

### <span class="c2">2.1.2        Software Interfaces</span>

<span class="c0">Complex interaction with HarmonyBot will require a basic interface to enable or disable features. This interface must be able to recognize and copy user roles from the bot’s database and then re-apply changes in function abilities and assign privileges.</span>

#### <span class="c4">2.1.</span><span>2</span><span class="c4">.1</span><span>        </span><span class="c4">Web Management Interface</span>

<span>HarmonyBot will feature a simple, browser-based interface where the user can connect HarmonyBot to a Discord server, as well as manage users and commands.</span>

### <span class="c2">2.1.3        Communications Protocols</span>

<span class="c0">HarmonyBot will utilize the Discord API connection between the DB and our bot. HarmonyBot’s WebGUI will exchange the data inputted by the user/moderator and store it in our DB which will be written using MySQL. This data will be visible via the WebGUI.</span>

* * *

## <span class="c12 c4"></span>

## <span class="c12 c4">2.2        Software Product Features</span>

### <span class="c2">2.2.1        Foundational Features</span>

<a id="t.b99774a514c715c7d4b20ce79cf4e5ccddb50cf8"></a><a id="t.1"></a>

<table class="c25">

<tbody>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c2">Name</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Description</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.1.1\. Database access</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Access to a schema using MySQL or a similar database management system, named using a unique server ID</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.1.2\. Server Connectivity</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Access to the Discord API for server connections</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.1.3\. Text and token analysis</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Ability to read chat channels and tokenize input strings</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.1.4\. Command use</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Ability to perform functions based on certain inputs from a text channel</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.1.5\. Role and permission recognition</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Ability to enable or disable functions depending on the permission level of a user</span>

</td>

</tr>

</tbody>

</table>

### <span class="c2"></span>

### <span class="c2">2.2.2        Moderation Features</span>

<a id="t.ae99024a9f8325258b2fa1906120863f72130af5"></a><a id="t.2"></a>

<table class="c25">

<tbody>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c2">Name</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c2">Description</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.2.1\. Ban List</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Keep a table of banned users, with an optional timer to prompt the reinstatement of a user</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.2.2\. Violations List</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Keep a table of all users with a counter for minor violations that can then prompt addition to the ban list based on a threshold</span>

</td>

</tr>

<tr class="c17">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.2.3\. Text channel moderation</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Keep a table of banned phrases that prompt additions to the list of violations when read in the text channel</span>

</td>

</tr>

</tbody>

</table>

### <span class="c2"></span>

* * *

### <span class="c2"></span>

### <span class="c2">2.2.3        Interaction Features</span>

<a id="t.431a5a0b1259a5337ec9674de8680a89cf961b20"></a><a id="t.3"></a>

<table class="c25">

<tbody>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c2">Name</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c2">Description</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.3.1\. Canned Response</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Set a table of interactive responses that output when the bot reads specific strings of tokens into the text channel.</span>

</td>

</tr>

<tr class="c1">

<td class="c13" colspan="1" rowspan="1">

<span class="c0">2.2.3.2\. Mass user commands</span>

</td>

<td class="c13" colspan="1" rowspan="1">

<span class="c0">Set a table of basic bot interactions that do not require user permissions</span>

</td>

</tr>

</tbody>

</table>

<span class="c0"></span>

## <span class="c4 c12">2.3        Software System Attributes</span>

### <span class="c2">2.3.1        Reliability</span>

<span class="c0">HarmonyBot’s features will be repeatable and reliable throughout all levels of the software. DB, source code, and GUI will all run without significant errors/bugs. The user will be able to upload data through the Discord interface and access this data via the online GUI. This data will be synchronized so there will not be any discrepancies between the data uploaded by the bot and the data stored in the DB.</span>

### <span class="c2">2.3.2        Availability</span>

<span>HarmonyBot will run with an uptime of 99.99% SLA. Since we will not be hosting our own services, we will rely on certain Discord services, which have an estimated uptime of 99.999% SLA.</span>

* * *

### <span class="c2">2.3.3        Security</span>

<span class="c0">Moderation features of HarmonyBot will only be accessible by users that were permitted by the server administrator. Regular users will not be able to access HarmonyBot’s powerful features (kick/ban/etc). Also, only users permitted by the server administrator will be able to access the online DB. These security measures will protect sensitive information from being accessed by anyone.</span>

### <span class="c2">2.3.4        Maintainability</span>

<span class="c0">HarmonyBot will be easily maintainable by the server administrators. The bot interface will have server management features that will allow for easy cleanup of data and information that had previously been organized by the bot. This data will also be manageable through the online DB.</span>

### <span class="c2">2.3.5        Performance</span>

<span class="c0">HarmonyBot will be able to encapsulate small amounts of data within the DB, and it should be able to handle any amount of data. We will be storing usernames, messages, and other text-based information in the DB. Since we will not be storing larger data types like images or videos, HarmonyBot will be scalable to accommodate nearly any amount of data without sacrificing performance on a noticeable level.</span>

## <span class="c12 c4">2.4        Database Requirements</span>

### <span class="c35">2.4.1 Concept Diagram</span><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 624.00px; height: 270.67px;">![](img/srsDBOverview.png)</span>

### <span class="c2">2.4.2 Description of Requirements</span>

<span class="c0">The database requires the ability to handle information about users, their roles, and what these roles allow them to do. User information includes their status (banned, temporarily muted and information about this mute, or unrestricted) and their role. Role information gives information about manual server permissions (muting other users, assigning roles, channel access) and what commands they are allowed to use.</span>

# <span class="c4 c19"></span>
