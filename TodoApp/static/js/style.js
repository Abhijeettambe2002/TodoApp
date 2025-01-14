document.addEventListener('DOMContentLoaded', (event) => {
    const checkboxes = document.querySelectorAll('.task-done');
    checkboxes.forEach((checkbox) => {
        const taskId = checkbox.getAttribute('data-id');
        const isChecked = localStorage.getItem(`taskDone_${taskId}`) === 'true';
        checkbox.checked = isChecked;
        if (isChecked) {
            checkbox.closest('.event').classList.add('highlighted');
        }
    });

    checkboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', (event) => {
            const taskId = event.target.getAttribute('data-id');
            const isChecked = event.target.checked;
            localStorage.setItem(`taskDone_${taskId}`, isChecked);
            if (isChecked) {
                event.target.closest('.event').classList.add('highlighted');
            } else {
                event.target.closest('.event').classList.remove('highlighted');
            }
        });
    });
});

function searchTasks() {
    var input, filter, events, eventTitle, i, txtValue, noMatch = true;
    input = document.getElementById("searchInput");
    filter = input.value.toLowerCase();
    events = document.getElementsByClassName("event");

    for (i = 0; i < events.length; i++) {
        eventTitle = events[i].getElementsByClassName("event-title")[0];
        if (eventTitle) {
            txtValue = eventTitle.textContent || eventTitle.innerText;
            if (txtValue.toLowerCase().indexOf(filter) > -1) {
                events[i].style.display = "";
                noMatch = false;
            } else {
                events[i].style.display = "none";
            }
        }
    }

    // Display no match message
    var noTasksMessage = document.getElementById("noTasksMessage");
    if (noMatch) {
        if (!noTasksMessage) {
            noTasksMessage = document.createElement("div");
            noTasksMessage.id = "noTasksMessage";
            noTasksMessage.className = "no-tasks";
            noTasksMessage.innerHTML = "<p>No such task added yet.</p>";
            document.body.appendChild(noTasksMessage);
        }
        noTasksMessage.style.display = "block";
    } else if (noTasksMessage) {
        noTasksMessage.style.display = "none";
    }
}