


export default class JobModel {
    constructor( id, jobcategory, jobdesignation, joblocation, companyname, salary, applyby, skillsrequired, numberofopenings, jobposted, applicants){
            this.id = id;
            this.jobcategory = jobcategory;
            this.jobdesignation = jobdesignation;
            this.joblocation = joblocation;
            this.companyname = companyname;
            this.salary = salary;
            this.applyby = applyby;
            this.skillsrequired = skillsrequired;
            this.numberofopenings = numberofopenings;
            this.jobposted = jobposted;
            this.applicants = applicants;
    }

    static getAll(){
        return jobs;
    }

    static getJobDetailbyId(id){
        return jobs.find((j)=> j.id == id)
    }

    static postApplicantAdd(id, applicant_det){
        jobs.find((j)=>{
            if(j.id == id){
                j.applicants.push(applicant_det);
            }
        })
        return true; 
    }

    static getApplicants(id){
        const job = jobs.find((j)=> j.id == id)
        return job.applicants;
    }

    static addJob(jobCategory, jobDesignation, jobLocation, companyname, salary, numberofopenings, skillsrequired, applyby){
      let currentdate = new Date().toLocaleDateString();
      // console.log(date);
      jobs.push(
        {
            id: jobs.length + 1,
            jobcategory: jobCategory,
            jobdesignation: jobDesignation,
            joblocation: jobLocation,
            companyname: companyname,
            salary: salary,
            applyby: applyby,
            skillsrequired: skillsrequired,
            numberofopenings: numberofopenings,
            jobposted: currentdate,
            applicants: [],
      }
    )
    }


    static updateJob(id, jobCategory, jobDesignation, jobLocation, companyname, salary, numberofopenings, skillsrequired, applyby){

        const index = jobs.findIndex((j)=> j.id == id);
            jobs[index].jobcategory = jobCategory;
            jobs[index].jobdesignation = jobDesignation;
            jobs[index].joblocation = jobLocation;
            jobs[index].companyname = companyname; 
            jobs[index].salary = salary;
            jobs[index].numberofopenings = numberofopenings;
            jobs[index].skillsrequired = skillsrequired;
            jobs[index].applyby = applyby;
    }

    static deleteJob(id){
        const index = jobs.findIndex(j=>j.id == id);
        jobs.splice(index, 1);
    }
}

var jobs = [
    new JobModel(
        1,
        'Tech',
        'SDE',
        'Gurgaon HR IND Remote',
        'Om iTech World',
        '14-20lpa',
        '30 Aug 2023',
        ['REACT', 'NodeJs', 'JS', 'SQL', 'MongoDB', 'Express', 'AWS'],
        5,
        '10/23/2024, 4:47:41 PM',
        [{
            name: 'Mayur Myatra',
            email: 'max@gmail.com',
            contact: '08469699889',
            resumePath: '/src/uploads/resume.pdf'
          },
          {
            name: 'Pratik Myatra',
            email: 'max@gmail.com',
            contact: '08469699889',
            resumePath: '/src/uploads/resume.pdf'
          }, 
          {
            name: 'Max Myatra',
            email: 'max@gmail.com',
            contact: '08469699889',
            resumePath: '/src/uploads/resume.pdf'
          },],
    ),
    new JobModel(
        2,
        'Tech',
        'SDE',
        'Gurgaon HR IND Remote',
        'Magenta',
        '14-20lpa',
        '30 Aug 2023',
        ['REACT', 'NodeJs', 'JS', 'SQL', 'MongoDB', 'Express', 'AWS'],
        3,
        '10/23/2024, 4:47:41 PM',
        [{
            name: 'Max Ahir',
            email: 'max@gmail.com',
            contact: '08469699889',
            resumePath: '/1729863418935-Resume_with_2_experience_section__Version_5___14___Version_12___Version_11___Shubhangi___15___Version_53_ (3).pdf'
          },
          {
            name: 'Pratik Myatra',
            email: 'max@gmail.com',
            contact: '08469699889',
            resumePath: '/1729863418935-Resume_with_2_experience_section__Version_5___14___Version_12___Version_11___Shubhangi___15___Version_53_ (3).pdf'
          }, 
          {
            name: 'Mayur Myatra',
            email: 'max@gmail.com',
            contact: '08469699889',
            resumePath: '/1729863418935-Resume_with_2_experience_section__Version_5___14___Version_12___Version_11___Shubhangi___15___Version_53_ (3).pdf'
          },],
    ),
    new JobModel(
        3,
        'Tech',
        'SDE',
        'Gurgaon HR IND Remote',
        'Coding Ninjas',
        '14-20lpa',
        '30 Aug 2023',
        ['REACT', 'NodeJs', 'JS', 'SQL', 'MongoDB', 'Express', 'AWS'],
        4,
        '10/23/2024, 4:47:41 PM',
        [{
            name: 'Pratik Myatra',
            email: 'max@gmail.com',
            contact: '08469699889',
            resumePath: '/1729863418935-Resume_with_2_experience_section__Version_5___14___Version_12___Version_11___Shubhangi___15___Version_53_ (3).pdf'
          }, 
          {
            name: 'Mayur Myatra',
            email: 'max@gmail.com',
            contact: '08469699889',
            resumePath: '/1729863418935-Resume_with_2_experience_section__Version_5___14___Version_12___Version_11___Shubhangi___15___Version_53_ (3).pdf'
          },],
    )
]