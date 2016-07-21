from com.xebialabs.xlrelease.api.v1.forms import Comment

# Find tasks by title in release
tasks = taskApi.searchTasksByTitle(taskTitle, "", releaseId)

# Find the first task that has not been completed and complete it
for task in tasks:
    if task.isUpdatable():
        print "Completing task {}; id: {}; status: {}\n".format(task.title, task.id, task.status)
        taskApi.completeTask(task.id, Comment("Automatically completed."))
        break;
