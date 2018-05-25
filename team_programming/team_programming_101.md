# Team Programming Basics

### Introduction

For any software development project, team organization and dynamics are extremely important. When the team is remote, this is especially the case. Team dynamics and organization generally fall within considerations of software development and software operations better known as DevOps. Often you will here about DevOps in association with methodologies or frameworks such as Agile, Scrum, and Kanban, but the overall idea is mobilizing people in the most efficient way possible to work together in the production of functional code.

![images](img/devops.svg)

If you are co-located with the people that you are developing software, you can try approaches such as peer programming or mob programming where one person codes while others sit beside them assisting with the program design, allowing all to use their strengths for the benefit of the group. In a remote setting, there are ways to overcome this such as live video chat sessions and use of linked editors such as Atom Teletype.

However, this is often not feasible for open-source projects. Aside from occasional code sprints and hackathons, open-source projects are generally coordinated through the version control system (VCS)(e.g., Git) and/or project management software (e.g., JIRA, Confluence, Trello, GitHub Project Boards, Slack). These tools allow people and teams to efficiently coordinate their work on a project anywhere, anytime.

The team programming method I am proposing here will use a mix of the aforementioned methods and tools to accomplish a collaborative software development task. The flow of iterative cycles are as follows.

* Planning the project
* Establishing progress benchmarks
* Scheduling team tasks and timelines
* Executing the plan
* Reviewing each cycles pros/cons/fixes
* Wrapping up the project

This is a simplified set of interrelated processes that allow a remote team to iterate quickly through the tasks and challenges that arise in the process of software development from conceptualization to release. By no means are these set in stone and it is ultimately up to each team to tailor their processes to best suit their project and their team dynamics.

### Planning

The success of any project is in the details. This means that when starting your project with an assigned team of programmers, developers, designers, and others, you should be thinking of:

* What needs to be done
* Who is best situated to do it
* Where should things be done
* When do things need to be completed

##### Requirements

Once you and your team are aware of a project, you should move to have a meeting as soon as possible to establish the details of the project (e.g., the project requirements). This meeting should involve introductions, a rundown of skill sets, and current workloads of the people involved. This should give you an idea of the frequency of meetings required and who should be involved in meetings along the way. **Only hold meetings that are necessary!**

This meeting should then move to the known details surrounding this project. This includes scope/intent of the project, minimum requirements needed to complete the project, coding standards, timeline for the project, and the project deliverables. This will allow the team to focus on what needs to be done and who is potentially best placed to accomplish certain tasks.

##### Personnel

Getting to know your peers is not always necessary in developing open-source projects, but it is an inevitable factor in staying involved in the open-source community. You should always make an effort to build good communication with your team members. As mentioned above, this involves knowledge of their strengths and communication of your strengths to the team. You want to ensure that once scope, intent, and minimum requirements are known for a project that you have the people in place to get the job done. This may involve additional training or push back on the requirements if there are skill gaps in the team that cannot be covered for a given project. It’s good to be confident and to show confidence in yourself and your team members, but honesty is the best policy when it comes to known skill gaps and the team’s ability to overcome them within a given timeline. **Always show respect to your team members** and **listen carefully!**.

##### Location

Ideally, you and your team would be co-located so that peer coding and mob coding practices could be achieved in a positive social space. But the nature of open-source projects and collaboration often involves one or more members of a team being either partially or completely remote. This means that those that cannot meet in person will need to find alternative ways to co-locate with their peers.

Communication channels are perhaps the most important to facilitate good team dynamics. Slack, Discord, and IRC are good places to text chat and to share code snippets with one another. Discord, Zoom, or Hangouts can also facilitate voice, video, and screen sharing which will come in handy for peer or mob coding sessions. Signal and Wire are good alternatives if your team requires secure communications. You may also want to consider text editors and IDEs with live coding features such as Atom’s Teletype. 

##### Timeline

Once your team has figured out what needs to be done, who is working on what parts, and where your work and communication will take place, a timeline for individual and team tasks can be established. Use of tools like GitHub Projects, Trello, Google Calendar, or Google Sheets can help keep team members on track with their tasks. Applications that can produce a `Gantt chart` are especially useful for this. Make sure to use colors schemes and notes to record issues, delays, personnel changes, and task reconfiguration in case requirements change; these will be useful later in helping your team adjust for future iterations.

### Benchmarks

In the course of establishing your timeline, you will want to need to bin your tasks in between the start date of the project and the expected delivery date of your completed project. This process of deciding what should be done by when is best accomplished through the use of benchmarks. Benchmarks are meta categories within which tasks and sub-tasks are placed to best complete key aspects of a project’s requirements. For example, `collection of data`, `data cleaning`, and `data storage` can be binned in a meta category of `data processing`. This category would then be optimally placed along the timeline to support other meta categories, ultimately pushing the project forward as efficiently as possible.

It is critical that time be taken to properly plan a timeline up front before real work is done on a given software project. This is because a well made timeline will easily become the branching scheme within your VCS. For example, if you have two people working on the `data processing` meta category, they can create the `data processing` branch, commit the tasks and sub-tasks to the branch, and then submit a pull request (PR) once the meta category is complete. The timeline established by the team should have provided them with the division of labor and deadlines for the tasks and sub-tasks, ensuring other teams receive their data on the expected dates.

### Scheduling

Due to the distributed nature of team members for many open	-source projects, it is important to properly schedule meetings and deadlines in a common time zone. Additionally, the timeline should also note absences, vacations, or other know dates/times team members will be unavailable for contact, meetings, or peer/mob coding sessions.

Keep in mind that if you are a part of a project, that project is now a job and should be treated as such. You should commit specific times to working on this project and its your responsibility to communication those times to your team and peer coder. Many aspects of remote work and collaborations are challenging and not being able to commit to a dedicated work schedule makes it hard on team members who may be working with you on a given set of tasks.

Make sure that any changes to scheduling are updated as soon as possible within the timeline, project management tools, and chat tools. This will let team members know what is going on and can then adjust scheduling and tasks accordingly.

### Execution

Before getting started with this involved and rapid process, here are a few things to keep in mind that may help make this a pleasant learning experience:

* Stay on schedule, but don’t work overtime unless absolutely necessary
* Be comfortable in a nice, calm location
* Talk openly to your team members
* Minimize distractions
* Take breaks and stretch

You may be super excited about and focused on starting a new project, but make sure that you are taking care of your body and mind through proper rest and preparation before, during, and after these processes. You and your team will ultimately benefit.

At this point, we are prepared to start building our project.

##### Construction



##### Integration



##### Testing



##### Retrospectives



### Release



##### Management & Monitor



### Conclusion




