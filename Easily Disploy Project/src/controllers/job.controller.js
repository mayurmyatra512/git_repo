import JobModel from "../models/job.model.js";
import ApplicantModel from "../models/applicant.model.js";
import path from 'path';


class JobController {
    
    getLanding(req, res) {
        if (req.session.userEmail) {
            res.render('landing', { userEmail: req.session.userEmail });

        }
        else {
            res.render('landing', { userEmail: null });
        }
    }

    getJobList(req, res, next) {
        const jobs = JobModel.getAll();
        if (req.session.userEmail) {
            res.render('jobListing', { jobs, userEmail: req.session.userEmail });
        }
        else {
            res.render('jobListing', { jobs, userEmail: null });
        }
    }
    getJobDet(req, res, next) {
        const id = req.params.id;
        const jobFound = JobModel.getJobDetailbyId(id);
        if (jobFound) {
            // userEmail: req.session.userEmail
            if (req.session.userEmail) {
                res.render('jobDetails', { job: jobFound, userEmail: req.session.userEmail });
            }
            else {
                res.render('jobDetails', { job: jobFound, userEmail: null });
            }
        } else {
            res.render('404_page', {
                errorMessage: 'Job Not Found',
            });
        }
    }
    postApply(req, res, next) {
        const id = req.params.id;
        const { name, email, contact } = req.body;
        // let cvLoc = path.join(path.resolve(), 'src', 'uploads');
        const resumePath = '/src/uploads/' + req.file.filename;
        ApplicantModel.add(name, email, contact, resumePath);
        let applicant_det = {
            name,
            email,
            contact,
            resumePath,
        }
        JobModel.postApplicantAdd(id, applicant_det);
        const jobFound = JobModel.getJobDetailbyId(id);
        if (jobFound) {
            if (req.session.userEmail) {
                res.render('jobDetails', { job: jobFound, userEmail: req.session.userEmail });
            }
            else {
                res.render('jobDetails', { job: jobFound, userEmail: null });
            }
        } else {
            res.status(401).send("Job Not Found");
        }
    }

    getApplicants(req, res) {
        const id = req.params.id
        // console.log(id);
        const applicants = JobModel.getApplicants(id);
        if (applicants) {
            if (req.session.userEmail) {
                res.render('applicants_list', { applicants: applicants, userEmail: req.session.userEmail });
            }
            else {
                res.render('404_page', {
                    errorMessage: 'Recruiter needs to login first !!!',
                });
            }
        }
        else {
            res.render('404_page', {
                errorMessage: 'There is no applicants yet !!!',
            });
        }
    }

    getAddJob(req, res){
        res.render('postNewJob', { userEmail: req.session.userEmail, errorMessage: null });
    }


    getUpdateJob(req, res){
        const id = req.params.id;
        const jobFound = JobModel.getJobDetailbyId(id);
        if (jobFound) {
            // userEmail: req.session.userEmail
            if (req.session.userEmail) {
                res.render('updatePostedJob', { job: jobFound, userEmail: req.session.userEmail });
            }
        } else {
            res.render('404_page', {
                errorMessage: 'Job Not Found',
            });
        }
    }

    postAddJob(req, res){
        const { jobCategory, jobDesignation, jobLocation, companyname, salary, numberofopenings, skillsrequired, applyby} = req.body;
        console.log(jobLocation);
        JobModel.addJob(jobCategory, jobDesignation, jobLocation, companyname, salary, numberofopenings, skillsrequired, applyby);

        const jobs = JobModel.getAll();
        // console.log(jobFound)
        if (req.session.userEmail) {
            res.render('jobListing', { jobs, userEmail: req.session.userEmail });
        }
        else {
            res.render('jobListing', { jobs, userEmail: null });
        }
        
    }

    postSearchJob(req,res){
        const { search }  = req.body;
        const jobs = JobModel.getAll();

        const job_list = jobs.filter((j)=>j.companyname == search);
        console.log(job_list);
        if (req.session.userEmail) {
            if(job_list){
                res.render('jobListing', { jobs: job_list, userEmail: req.session.userEmail });
            }
        }
        else {
            res.render('jobListing', { jobs: job_list, userEmail: null });
        }
    }

    postUpdateJob(req, res){
        const { jobCategory, jobDesignation, jobLocation, companyname, salary, numberofopenings, skillsrequired, applyby} = req.body;
        const id = req.params.id;
        // console.log(skillsrequired);
        JobModel.updateJob(id, jobCategory, jobDesignation, jobLocation, companyname, salary, numberofopenings, skillsrequired, applyby);

        const jobFound = JobModel.getJobDetailbyId(id);
        // console.log(jobFound)
        if (jobFound) {
            // userEmail: req.session.userEmail
            if (req.session.userEmail) {
                res.render('jobDetails', { job: jobFound, userEmail: req.session.userEmail });
            }
            else {
                res.render('jobDetails', { job: jobFound, userEmail: null });
            }
        } else {
            res.render('404_page', {
                errorMessage: 'Job Not Found',
            });
        }
    }

    postDeleteJob(req,res){
        const id = req.params.id;
        const jobFound = JobModel.getJobDetailbyId(id);
        if (!jobFound) {
            res.render('404_page', {
                errorMessage: 'Job Not Found',
            });
        }
        JobModel.deleteJob(id);
        var jobs = JobModel.getAll();
        if (req.session.userEmail) {
            res.render('jobListing', { jobs, userEmail: req.session.userEmail });
        }
        else {
            res.render('jobListing', { jobs, userEmail: null });
        }
        

    }

    getFile(req,res, next){
        let location = path.join(path.resolve(), 'src', 'uploads')
        console.log(location);
        return  res.sendFile(location +'/'+ req.params.filename);
    }
}

export default JobController;