document.addEventListener("DOMContentLoaded", function () {

    // Confirm before deleting a task
    const deleteForms = document.querySelectorAll(".delete-form");

    deleteForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const confirmed = confirm("Are you sure you want to delete 
this task?");

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

    // Show a message when a task is added
    const taskForm = document.querySelector("#task-form");

    if (taskForm) {
        taskForm.addEventListener("submit", function () {
            console.log("Study task submitted!");
        });
    }

});
