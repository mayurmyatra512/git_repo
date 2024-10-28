// import JobController from "../src/controllers/job.controller.js";
// import JobModel from "../src/models/job.model.js";

function deleteJob(id){
    console.log(id);
    const res = confirm('Are You sure that you want to delete this job ?');
    if(res){
        fetch("/job/delete/"+id, {
            method: "POST"
        }).then(res =>{
            if(res.ok){
                location.reload();
            }
        })
    }
}