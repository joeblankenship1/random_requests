# Team Programming Basics

### Introduction

For any software development project, team organization and dynamics are extremely important. When the team is remote, this is especially the case. Team dynamics and organization generally fall within considerations of software development and software operations better known as DevOps. Often you will here about DevOps in association with methodologies or frameworks such as Agile, Scrum, and Kanban, but the overall idea is mobilizing people in the most efficient way possible to work together in the production of functional code.

![images](img/devops.svg)

If you are co-located with your software development team, you can try approaches such as [pair programming](https://en.wikipedia.org/wiki/Pair_programming) or [mob programming](https://en.wikipedia.org/wiki/Mob_programming) where one person codes while others sit beside them assisting with the program design, allowing all to use their strengths for the benefit of the group. In a remote setting, there are ways to overcome this such as live video chat sessions and use of linked editors such as Atom Teletype.

However, this is often not feasible for open-source projects. Aside from occasional code sprints and hackathons, open-source projects are generally coordinated through a version control system (VCS)(e.g., Git) and/or project management software (e.g., JIRA, Confluence, Trello, GitHub Project Boards, Slack). These tools allow people and teams to efficiently coordinate their work on a project anywhere, anytime.

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

Ideally, you and your team would be co-located so that pair coding and mob coding practices could be achieved in a positive social space. But the nature of open-source projects and collaboration often involves one or more members of a team being either partially or completely remote. This means that those that cannot meet in person will need to find alternative ways to co-locate with their peers.

Communication channels are perhaps the most important to facilitate good team dynamics. Slack, Discord, and IRC are good places to text chat and to share code snippets with one another. Discord, Zoom, or Hangouts can also facilitate voice, video, and screen sharing which will come in handy for pair or mob coding sessions. Signal and Wire are good alternatives if your team requires secure communications. You may also want to consider text editors and IDEs with live coding features such as Atom’s Teletype. 

##### Timeline

Once your team has figured out what needs to be done, who is working on what parts, and where your work and communication will take place, a timeline for individual and team tasks can be established. Use of tools like GitHub Projects, Trello, Google Calendar, or Google Sheets can help keep team members on track with their tasks. Applications that can produce a `Gantt chart` are especially useful for this. Make sure to use colors schemes and notes to record issues, delays, personnel changes, and task reconfiguration in case requirements change; these will be useful later in helping your team adjust for future iterations.

### Benchmarks

In the course of establishing your timeline, you will need to bin your tasks in between the start date of the project and the expected delivery date of your completed project. This process of deciding what should be done by when is best accomplished through the use of benchmarks. Benchmarks are meta categories within which tasks and sub-tasks are placed to best complete key aspects of a project’s requirements. For example, `collection of data`, `data cleaning`, and `data storage` can be binned in a meta category of `data processing`. This category would then be optimally placed along the timeline to support other meta categories, ultimately pushing the project forward as efficiently as possible.

It is critical that time be taken to properly plan a timeline up front before real work is done on a given software project. This is because a well made timeline will easily become the branching scheme within your VCS. For example, if you have two people working on the `data processing` meta category, they can create the `data processing` branch, commit the tasks and sub-tasks to the branch, and then submit a pull request (PR) once the meta category is complete. The timeline established by the team should have provided them with the division of labor and deadlines for the tasks and sub-tasks, ensuring other teams receive their data on the expected dates.

### Scheduling

Due to the distributed nature of team members for many open	-source projects, it is important to properly schedule meetings and deadlines in a common time zone. Additionally, the timeline should also note absences, vacations, or other known dates/times team members will be unavailable for contact, meetings, or pair/mob coding sessions.

Keep in mind that if you are a part of a project, that project is now a job and should be treated as such. You should commit specific times to working on this project and its your responsibility to communication those times to your team. Many aspects of remote work and collaborations are challenging and not being able to commit to a dedicated work schedule makes it hard on team members who may be working with you on a given set of tasks.

Make sure that any changes to scheduling are updated as soon as possible within the timeline, project management tools, and chat tools. This will let team members know what is going on and can then adjust scheduling and tasks accordingly.

All of the above should be recorded in a common set of tools of which team members have persistent access to throughout the project. Expectations of access and contributions through these tools should also be outlined before a team starts building a given project. These expectations include various leadership roles for code review, task board updates, calendar changes, and meet agendas for teams and sub-teams. Once these challenges have been resolved, building a project becomes much more efficient.

### Pre-execution

Now that planning, benchmarks, and scheduling are outlined and agreed upon, you now have to ensure that those plans are reflected in the code that is produced by the team. We do this through the use of GitFlow.

##### GitFlow

GitFlow is a Git branching model largely attributed to [Vincent Driessen](https://nvie.com/posts/a-successful-git-branching-model/). This involves the use of several branch types that interact with one another to ensure that the Master branch of any project is always 100% functional.

![images](img/gitflow.png)

Here is a brief list of the branches and concepts, but for the fullest understanding of this model, you should read the blog post linked above.

* **Master Branch** - This is your primary production branch. Code should always be at 100% test coverage and functionality at any point in the version control history of this branch.
* **Develop Branch** - This is your primary working branch. This branch ensures that feature branch merges/rebases are tested and functional. This branch also feeds the release branch ensuring that all bugs are reviewed and fixed before being pushed to master.
* **Hotfixes Branch** - This branch is for emergency code fixes to the master branch. Hotfixes are also pushed to the develop branch to ensure errors are accounted for in future releases. Hotfixes are often versioned as `minor` or bug releases (e.g., version 0.2).
* **Release Branch** - This is the intermediate branch that prepares `major` releases for production on the master branch (e.g., version 1.0).
* **Feature Branches** - These branches are what build your application. These are generally created to address a single requirement or group of requirements that are then integrated into the develop branch for overall application testing and review.

These practices should apply to small and large projects alike; practicing these helps you integrate faster into other open-source or work projects over time. It is up to your team to establish what requirements are built into feature branches and how those features are integrated into the develop branch. Likewise, your team must also establish what constitutes a `major` release depending on the scale and duration of a project. Ultimately, working between the develop and release branches prevents your team from pushing untested, buggy code to your master branch.

##### Testing

Testing you code as you build is very important. Not only does it ensure that what you are working on functions the way it should, it makes sure that your code works with everyone elses within the larger product. How you build tests and what tools you use for tests are largely dictates by your team and the languages you are working in to build your project. Here is a brief list of guidelines:

* Tests should be built for small units of functionality to ensure they work correctly.
* Tests must be able to run independently
* Tests should run fast
* Write broken tests to remind you what you need to do next
* Write long, descriptive names for your tests
* Run tests each time before you start coding
* Run tests before you push your code

Even if you are building a project by yourself, it is good practice to build tests as you code. You may want to read a bit more about [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) and [unit testing](https://en.wikipedia.org/wiki/Unit_testing) focusing on the languages you are using and the application spaces into which you plan to deploy your code.

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

The first cycle in execution is that of building the initial prototype. This will be done in line with the aforementioned timeline, benchmarks, and VCS scheme. Predetermined times for pair/mob coding sessions should be adhered to as much as possible to ensure that all developers on the project are on the same page and consistently contribute to the project. This ensures that all team members are leveraging their strongest skill sets towards the best possible deliverable.

##### Integration

Following each benchmark, code should be reviewed by the team and merged with the `master` branch to ensure progress and development knowledge are recorded. This includes the use of GitHub Wikipages, reorganization of GitHub Project cards (or a project management software of your choice), and drafting of basic documentation for that benchmark section. Adjustments to VCS practices, code quality assurance, and packaging should also be addressed during benchmark completion periods.

This cycle will continue until the delivery date for the project with minor shifts afterwards if maintenance and monitoring is required.

##### Testing

Testing can make or break a project. To ensure that your project works beyond delivery for any number of potential use cases, you should consider how to integrated testing and test automation. Every language has its own community led projects that assist developers with tasks such as unit tests, API tests, and any form of regression testing. These ensure that developers have designed and deployed applications with features that have 100% code coverage (tests have been created for all user interactions possible within your application). Python has `unittest` and `pytest` while JavaScript has `jest` and `testcafe` as a few of many suites for testing.

These considerations should be considered before initial execution and should be revisited during benchmark completion periods by the development team.

##### Retrospectives

Perhaps the most important aspect of team programming is that of continuous communication and collaboration. During each benchmark completion period and following final delivery of the project, the team should engage in retrospectives. These are sessions designed to address what when well, what could have gone better, and what could be used to improve various processes. This ultimately makes future benchmarks and deliveries simpler and more efficient.

As you can see above, each major aspect of execution has periods of retrospection built into the benchmark completion periods. This ensures not only better software development practices over time, but ensures collaboration between team members results in the building of a solid community.

### Release

Prior to release, team members will want to undergo final code reviews, code testing, and documentation drafting. This will not only assist in the potential management and maintenance of the software, but ultimately this will allow proper hand-off and training for users and implementers of your project. For simple projects, version numbers, `alpha`, and/or `beta` releases may not be necessary. However, the conditions of a project’s requirements will dictate whether these will be used.

Once the team agrees that the project meets and/or exceeds the requirements within the project scope, the software can be deployed/delivered. The manner in which this is done will be in line with the requirements outlined during the initial phases of the project.

##### Management & Monitor

Often with small, open-source projects, you will not think about management or monitoring of your project once it is deployed (e.g., a JavaScript web application deployed via GitHub Pages). However, these may have API dependencies or external library dependencies that could break over time.

As a developer, you must ensure that if you have designed software that others are using for professional and/or personal reasons (especially if this is a paid service), that you have accounted for management and monitoring of dependencies your software uses. There are several options:

* Download and store dependencies with your software
* Create virtual environments or containers that freeze dependencies
* Make explicit calls to dependency versions accompanied by error handling/logging/message services
* Use a third party monitoring service for your software

It is ultimately up to the development team and end users to navigate these issues based on their needs, use cases, and budgets.

### Conclusion

Hopefully this has been a useful guide for newcomers to team programming. These are not rules or immutable laws, but suggestions gleaned from many experienced developers and programmers that may make your projects exciting experiences rather than collaborative nightmares.

Over time, team members will figure out how they work best in accomplishing tasks, but initially this can seem like a burdensome, confusing, and downright scary set of thoughts. The key is to keep open, persistent, and constructive communication with your team members about what, how, and why you are doing what you are doing to get the tasks completed on time.

