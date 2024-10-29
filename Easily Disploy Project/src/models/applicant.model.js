
export default class ApplicantModel {
    constructor( applicantId, name, email, contact, resumePath){
        this.applicantId = applicantId;
        this.name = name;
        this.email = email;
        this.contact = contact;
        this.resumePath = resumePath;
    }

    static add(name, email, contact, resumePath){
        let newApplicant = new ApplicantModel (
            applicants.length  + 1,
            name,
            email,
            contact,
            resumePath,
        );
        applicants.push(newApplicant);
        console.log(applicants);
    }
    // static getApplicant(name){
    //     const index = applicants.findIndex((appl)=> appl.name == name)
        
    // }

}

var applicants = []