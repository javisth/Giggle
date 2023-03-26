function getJobs() {
  var mood = document.getElementById("mood").value;
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/jobs", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var jobs = JSON.parse(xhr.responseText);
      displayJobs(jobs);
    }
  };
  xhr.send(JSON.stringify({"mood": mood}));
}

function displayJobs(jobs) {
  var jobList = document.getElementById("job-list");
  jobList.innerHTML = "";
  jobs.forEach(function(job) {
    var li = document.createElement("li");
    li.innerHTML = "<strong>" + job.title + "</strong><br>" + job.description;
    jobList.appendChild(li);
  });
}


